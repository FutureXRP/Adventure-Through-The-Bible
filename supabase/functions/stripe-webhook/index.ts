// supabase/functions/stripe-webhook/index.ts
// Receives Stripe webhook events and updates Supabase accordingly.
// Handles: successful payments, subscription updates, cancellations.

import { serve } from 'https://deno.land/std@0.168.0/http/server.ts';
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2';
import Stripe from 'https://esm.sh/stripe@13.11.0?target=deno';

const stripe = new Stripe(Deno.env.get('STRIPE_SECRET_KEY')!, {
  apiVersion: '2023-10-16',
  httpClient: Stripe.createFetchHttpClient(),
});

const webhookSecret = Deno.env.get('STRIPE_WEBHOOK_SECRET')!;

serve(async (req) => {
  const signature = req.headers.get('stripe-signature');
  if (!signature) {
    return new Response('Missing stripe-signature header', { status: 400 });
  }

  const body = await req.text();

  // Verify webhook signature — prevents spoofed requests
  let event: Stripe.Event;
  try {
    event = await stripe.webhooks.constructEventAsync(body, signature, webhookSecret);
  } catch (err) {
    console.error('Webhook signature verification failed:', err.message);
    return new Response(`Webhook Error: ${err.message}`, { status: 400 });
  }

  const sbAdmin = createClient(
    Deno.env.get('SUPABASE_URL')!,
    Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
  );

  console.log('Stripe event received:', event.type);

  try {
    switch (event.type) {

      // ── ONE-TIME PAYMENT COMPLETE ──────────────────────────────
      case 'checkout.session.completed': {
        const session = event.data.object as Stripe.Checkout.Session;
        const userId = session.metadata?.supabase_user_id;
        const plan = session.metadata?.plan;

        if (!userId) { console.error('No supabase_user_id in metadata'); break; }

        if (plan === 'one_time' && session.payment_status === 'paid') {
          await sbAdmin.from('profiles').update({
            is_paid: true,
            plan_type: 'one_time',
            paid_at: new Date().toISOString(),
          }).eq('id', userId);
          console.log('One-time purchase unlocked for user:', userId);
        }

        if (plan === 'monthly') {
          // Subscription — grab the subscription ID for future management
          const subscriptionId = session.subscription as string;
          await sbAdmin.from('profiles').update({
            is_paid: true,
            plan_type: 'monthly',
            stripe_subscription_id: subscriptionId,
            paid_at: new Date().toISOString(),
          }).eq('id', userId);
          console.log('Monthly subscription unlocked for user:', userId);
        }
        break;
      }

      // ── SUBSCRIPTION RENEWED ───────────────────────────────────
      case 'invoice.payment_succeeded': {
        const invoice = event.data.object as Stripe.Invoice;
        const subscriptionId = invoice.subscription as string;
        if (!subscriptionId) break;

        // Find user by subscription ID
        const { data: profile } = await sbAdmin
          .from('profiles')
          .select('id')
          .eq('stripe_subscription_id', subscriptionId)
          .single();

        if (profile) {
          await sbAdmin.from('profiles').update({
            is_paid: true,
          }).eq('id', profile.id);
          console.log('Subscription renewed for user:', profile.id);
        }
        break;
      }

      // ── SUBSCRIPTION CANCELLED / PAYMENT FAILED ───────────────
      case 'customer.subscription.deleted':
      case 'invoice.payment_failed': {
        const obj = event.data.object as Stripe.Subscription | Stripe.Invoice;
        const subscriptionId = 'subscription' in obj
          ? obj.subscription as string
          : (obj as Stripe.Subscription).id;

        if (!subscriptionId) break;

        const { data: profile } = await sbAdmin
          .from('profiles')
          .select('id')
          .eq('stripe_subscription_id', subscriptionId)
          .single();

        if (profile) {
          await sbAdmin.from('profiles').update({
            is_paid: false,
            plan_type: null,
            stripe_subscription_id: null,
          }).eq('id', profile.id);
          console.log('Subscription revoked for user:', profile.id);
        }
        break;
      }

      // ── SUBSCRIPTION UPDATED (e.g. plan change) ────────────────
      case 'customer.subscription.updated': {
        const subscription = event.data.object as Stripe.Subscription;
        const { data: profile } = await sbAdmin
          .from('profiles')
          .select('id')
          .eq('stripe_subscription_id', subscription.id)
          .single();

        if (profile) {
          const isActive = subscription.status === 'active' || subscription.status === 'trialing';
          await sbAdmin.from('profiles').update({
            is_paid: isActive,
          }).eq('id', profile.id);
        }
        break;
      }

      default:
        console.log('Unhandled event type:', event.type);
    }

    return new Response(JSON.stringify({ received: true }), {
      headers: { 'Content-Type': 'application/json' },
      status: 200,
    });

  } catch (err) {
    console.error('Webhook handler error:', err.message);
    return new Response(
      JSON.stringify({ error: err.message }),
      { headers: { 'Content-Type': 'application/json' }, status: 500 }
    );
  }
});
