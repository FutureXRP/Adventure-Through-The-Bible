// Supabase Edge Function: process-refund
// Deploy to: supabase/functions/process-refund/index.ts
//
// What it does:
//   1. Authenticates the requesting user
//   2. Loads their profile (plan type, Stripe customer/payment IDs)
//   3. Counts total stories opened across ALL profiles on the account
//   4. Checks against refund thresholds:
//        Monthly:   < 5 stories → eligible
//        One-time:  < 8 stories → eligible
//   5. If eligible: calls Stripe to issue a full refund, marks account as refunded in DB
//   6. If ineligible: returns clear denial with story count and threshold
//
// Thresholds (change these constants to adjust policy):
const MONTHLY_STORY_THRESHOLD = 5;   // must have opened FEWER than this
const ONETIME_STORY_THRESHOLD = 8;   // must have opened FEWER than this

import { serve } from 'https://deno.land/std@0.177.0/http/server.ts';
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2';
import Stripe from 'https://esm.sh/stripe@13';

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
};

serve(async (req) => {
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders });
  }

  try {
    // ── Auth ──────────────────────────────────────────────────────────
    const authHeader = req.headers.get('Authorization');
    if (!authHeader) {
      return json({ error: 'Unauthorized' }, 401);
    }

    const supabase = createClient(
      Deno.env.get('SUPABASE_URL')!,
      Deno.env.get('SUPABASE_ANON_KEY')!,
      { global: { headers: { Authorization: authHeader } } }
    );

    const { data: { user }, error: userError } = await supabase.auth.getUser();
    if (userError || !user) {
      return json({ error: 'Unauthorized' }, 401);
    }

    // ── Load profile ──────────────────────────────────────────────────
    const { data: profile, error: profileError } = await supabase
      .from('profiles')
      .select('is_paid, plan_type, stripe_customer_id, stripe_payment_intent_id, stripe_subscription_id, refund_issued_at')
      .eq('id', user.id)
      .single();

    if (profileError || !profile) {
      return json({ error: 'Profile not found.' }, 404);
    }

    // ── Already refunded? ─────────────────────────────────────────────
    if (profile.refund_issued_at) {
      return json({
        error: 'A refund has already been issued for this account.',
        already_refunded: true,
      }, 400);
    }

    // ── Must be a paid account ────────────────────────────────────────
    if (!profile.is_paid) {
      return json({ error: 'No paid subscription found on this account.' }, 400);
    }

    const planType = profile.plan_type; // 'monthly' | 'one_time' | 'monthly_cancelling'
    if (!planType || (planType !== 'monthly' && planType !== 'one_time' && planType !== 'monthly_cancelling')) {
      return json({ error: 'No refundable plan found on this account.' }, 400);
    }

    // ── Count stories opened across ALL profiles on this account ──────
    // Get child profile IDs first
    const { data: children } = await supabase
      .from('child_profiles')
      .select('id')
      .eq('parent_id', user.id);

    const childIds = (children || []).map((c: { id: string }) => c.id);

    // Count unique story_ids opened (parent + all children)
    let totalStoriesOpened = 0;

    // Parent progress
    const { data: parentProgress } = await supabase
      .from('story_progress')
      .select('story_id')
      .eq('profile_id', user.id)
      .eq('profile_type', 'user');

    const parentStoryIds = new Set((parentProgress || []).map((p: { story_id: string }) => p.story_id));

    // Children progress
    const childStoryIds = new Set<string>();
    if (childIds.length > 0) {
      const { data: childProgress } = await supabase
        .from('story_progress')
        .select('story_id')
        .in('profile_id', childIds)
        .eq('profile_type', 'child');

      (childProgress || []).forEach((p: { story_id: string }) => childStoryIds.add(p.story_id));
    }

    // Union of all unique story IDs across all profiles
    const allStoryIds = new Set([...parentStoryIds, ...childStoryIds]);
    totalStoriesOpened = allStoryIds.size;

    // ── Check threshold ───────────────────────────────────────────────
    const isMonthly = planType === 'monthly' || planType === 'monthly_cancelling';
    const threshold = isMonthly ? MONTHLY_STORY_THRESHOLD : ONETIME_STORY_THRESHOLD;
    const eligible = totalStoriesOpened < threshold;

    if (!eligible) {
      return json({
        error: 'Refund not eligible.',
        eligible: false,
        stories_opened: totalStoriesOpened,
        threshold,
        plan_type: planType,
        message: `Your account has opened ${totalStoriesOpened} ${totalStoriesOpened === 1 ? 'story' : 'stories'}. Refunds are available only when fewer than ${threshold} stories have been accessed. If you believe this is an error, please contact us at hello@squareonecompassion.org.`,
      }, 200);
    }

    // ── Process refund via Stripe ─────────────────────────────────────
    const stripe = new Stripe(Deno.env.get('STRIPE_SECRET_KEY')!, {
      apiVersion: '2023-10-16',
    });

    let refundId: string | null = null;
    let amountRefunded: number | null = null;

    if (isMonthly && profile.stripe_subscription_id) {
      // Cancel the subscription immediately
      await stripe.subscriptions.cancel(profile.stripe_subscription_id);

      // Find the most recent invoice payment to refund
      const invoices = await stripe.invoices.list({
        customer: profile.stripe_customer_id,
        limit: 1,
      });

      const latestInvoice = invoices.data[0];
      if (latestInvoice?.payment_intent) {
        const refund = await stripe.refunds.create({
          payment_intent: latestInvoice.payment_intent as string,
          reason: 'requested_by_customer',
        });
        refundId = refund.id;
        amountRefunded = refund.amount;
      }

    } else if (!isMonthly && profile.stripe_payment_intent_id) {
      // Refund the one-time payment
      const refund = await stripe.refunds.create({
        payment_intent: profile.stripe_payment_intent_id,
        reason: 'requested_by_customer',
      });
      refundId = refund.id;
      amountRefunded = refund.amount;
    } else {
      return json({
        error: 'Could not locate the original payment to refund. Please contact hello@squareonecompassion.org.',
      }, 400);
    }

    // ── Update profile in DB ──────────────────────────────────────────
    // Use service role client for the update (bypasses RLS)
    const adminClient = createClient(
      Deno.env.get('SUPABASE_URL')!,
      Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
    );

    await adminClient
      .from('profiles')
      .update({
        is_paid: false,
        plan_type: null,
        refund_issued_at: new Date().toISOString(),
        stripe_refund_id: refundId,
      })
      .eq('id', user.id);

    // Log the refund event
    await adminClient.from('refund_log').insert({
      user_id: user.id,
      plan_type: planType,
      stories_opened: totalStoriesOpened,
      stripe_refund_id: refundId,
      amount_refunded_cents: amountRefunded,
      requested_at: new Date().toISOString(),
    });

    return json({
      success: true,
      eligible: true,
      refund_id: refundId,
      amount_refunded_cents: amountRefunded,
      stories_opened: totalStoriesOpened,
      message: 'Your refund has been processed. It will appear on your card within 5–10 business days. Your account has been returned to the free tier.',
    });

  } catch (err) {
    console.error('Refund error:', err);
    return json({
      error: 'An unexpected error occurred. Please contact hello@squareonecompassion.org.',
    }, 500);
  }
});

function json(data: unknown, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { ...corsHeaders, 'Content-Type': 'application/json' },
  });
}
