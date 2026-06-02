// supabase/functions/create-checkout/index.ts
// Creates a Stripe Checkout session and returns the URL.
// Called from the frontend when user clicks a purchase button.

import { serve } from 'https://deno.land/std@0.168.0/http/server.ts';
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2';
import Stripe from 'https://esm.sh/stripe@13.11.0?target=deno';

const stripe = new Stripe(Deno.env.get('STRIPE_SECRET_KEY')!, {
  apiVersion: '2023-10-16',
  httpClient: Stripe.createFetchHttpClient(),
});

const PRICE_ONE_TIME = 'price_1TdxaVLhNi71Q1IHxg3M9vIX';
const PRICE_MONTHLY  = 'price_1Tdxb2LhNi71Q1IHq8OmNGt6';
const SITE_URL       = 'https://futurexrp.github.io/Adventure-Through-The-Bible';

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
};

serve(async (req) => {
  // Handle CORS preflight
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders });
  }

  try {
    // Get authenticated user from JWT
    const authHeader = req.headers.get('Authorization');
    if (!authHeader) throw new Error('Missing authorization header');

    const sb = createClient(
      Deno.env.get('SUPABASE_URL')!,
      Deno.env.get('SUPABASE_ANON_KEY')!,
      { global: { headers: { Authorization: authHeader } } }
    );

    const { data: { user }, error: userError } = await sb.auth.getUser();
    if (userError || !user) throw new Error('Not authenticated');

    // Get plan from request body
    const { plan } = await req.json(); // 'one_time' or 'monthly'
    if (!plan || !['one_time', 'monthly'].includes(plan)) {
      throw new Error('Invalid plan — must be one_time or monthly');
    }

    // Get or create Stripe customer
    const sbAdmin = createClient(
      Deno.env.get('SUPABASE_URL')!,
      Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
    );

    const { data: profile } = await sbAdmin
      .from('profiles')
      .select('stripe_customer_id, display_name')
      .eq('id', user.id)
      .single();

    let customerId = profile?.stripe_customer_id;

    if (!customerId) {
      const customer = await stripe.customers.create({
        email: user.email,
        name: profile?.display_name || '',
        metadata: { supabase_user_id: user.id },
      });
      customerId = customer.id;

      // Save customer ID to profile
      await sbAdmin
        .from('profiles')
        .update({ stripe_customer_id: customerId })
        .eq('id', user.id);
    }

    // Build checkout session
    const sessionParams: Stripe.Checkout.SessionCreateParams = {
      customer: customerId,
      success_url: `${SITE_URL}/index.html?checkout=success`,
      cancel_url:  `${SITE_URL}/index.html?checkout=cancelled`,
      metadata: { supabase_user_id: user.id, plan },
    };

    if (plan === 'one_time') {
      sessionParams.mode = 'payment';
      sessionParams.line_items = [{ price: PRICE_ONE_TIME, quantity: 1 }];
    } else {
      sessionParams.mode = 'subscription';
      sessionParams.line_items = [{ price: PRICE_MONTHLY, quantity: 1 }];
      sessionParams.subscription_data = {
        metadata: { supabase_user_id: user.id },
      };
    }

    const session = await stripe.checkout.sessions.create(sessionParams);

    return new Response(
      JSON.stringify({ url: session.url }),
      { headers: { ...corsHeaders, 'Content-Type': 'application/json' }, status: 200 }
    );

  } catch (err) {
    console.error('create-checkout error:', err.message);
    return new Response(
      JSON.stringify({ error: err.message }),
      { headers: { ...corsHeaders, 'Content-Type': 'application/json' }, status: 400 }
    );
  }
});
