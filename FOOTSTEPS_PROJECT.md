# Footsteps — Project Reference Document
**Last updated:** June 2026
**GitHub:** futurexrp/Adventure-Through-The-Bible
**Live site:** https://futurexrp.github.io/Adventure-Through-The-Bible/

---

## What This App Is

Footsteps is a premium Bible story app for families with children. Each story is told in a vivid, present-tense, Message-style register — faithful to the biblical text, zero commentary woven in, told the way a great storyteller would tell it out loud. Every story has a Big Idea, three Talk About It questions, three connection cards linking to related stories, and a three-question quiz with celebration screen.

**Tagline:** Walk through the greatest story ever told
**Model:** One-time purchase ($49.99) or monthly subscription ($4.99/month)
**Status:** Tier 1 (9–12) in progress — 15 of 30 stories complete with audio for stories 1–10

---

## Repo File Structure

```
Adventure-Through-The-Bible/
  index.html              ← main app (story grid, modals, auth, paywall, badges)
  login.html              ← sign in / sign up page
  account.html            ← account management, plan, cancel subscription
  stories.json            ← ALL story content lives here
  header.png              ← watercolor banner (children walking stone path, ancient ruins)
  generate_audio.py       ← ElevenLabs API script — generates MP3 + timestamp JSON
  FOOTSTEPS_PROJECT.md    ← this file
  audio/
    creation.mp3 + creation.json
    adam-eve.mp3 + adam-eve.json
    cain-abel.mp3 + cain-abel.json
    noah.mp3 + noah.json
    tower-babel.mp3 + tower-babel.json
    abraham.mp3 + abraham.json
    joseph.mp3 + joseph.json
    moses-birth.mp3 + moses-birth.json
    burning-bush.mp3 + burning-bush.json
    red-sea.mp3 + red-sea.json
    (stories 11–30 pending)
  supabase/
    config.toml           ← Edge Function JWT config
    functions/
      create-checkout/
        index.ts          ← creates Stripe checkout session
      stripe-webhook/
        index.ts          ← handles Stripe events, updates profiles
      cancel-subscription/
        index.ts          ← cancels monthly subscription at period end
  .github/
    workflows/
      deploy-functions.yml ← auto-deploys Edge Functions on push to main
```

---

## Tech Stack

- **Frontend:** Static HTML/CSS/JS — no framework, no build step
- **Hosting:** GitHub Pages (free, auto-deploys on push)
- **Data:** `stories.json` — fetched at runtime, all story content lives here
- **Auth:** Supabase Auth — email/password, family + individual accounts
- **Database:** Supabase Postgres — profiles, child profiles, progress, badges, quiz attempts
- **Payments:** Stripe — one-time purchase + monthly subscription
- **Edge Functions:** Supabase Edge Functions (Deno) — checkout, webhook, cancellation
- **Audio:** ElevenLabs API — generates MP3 + character-level timestamp JSON
- **Word highlighting:** Time-based positional matching using ElevenLabs timestamp JSON
- **Progress tracking:** Supabase (logged in) or localStorage (guest)

---

## Supabase Configuration

**Project URL:** https://bqyysvjnitbeimvaxkao.supabase.co
**Project Ref:** bqyysvjnitbeimvaxkao

### Tables
| Table | Purpose |
|-------|---------|
| `profiles` | One row per auth user — account type, avatar, payment status |
| `child_profiles` | Children added under parent accounts |
| `story_progress` | Stories completed per profile |
| `quiz_attempts` | Quiz scores per story per profile |
| `badges` | Badges earned per profile |

### Key profile columns
| Column | Type | Purpose |
|--------|------|---------|
| `is_paid` | bool | Active access (monthly or one-time) |
| `has_lifetime` | bool | Permanent access to 50 launch stories — NEVER reset by cancellation |
| `plan_type` | text | `one_time`, `monthly`, `monthly_cancelling`, null |
| `stripe_customer_id` | text | Stripe customer reference |
| `stripe_subscription_id` | text | For monthly subscribers |
| `paid_at` | timestamptz | When purchase was made |

### Access logic
- `has_lifetime = true` → always has access to 50 launch stories, regardless of subscription
- `is_paid = true` → full active access
- Cancel monthly → `is_paid` may drop but `has_lifetime` is preserved
- `storyIsLocked` checks `has_lifetime OR is_paid`

### Edge Functions
| Function | Auth | Purpose |
|----------|------|---------|
| `create-checkout` | JWT required | Creates Stripe checkout session |
| `stripe-webhook` | No JWT (Stripe calls it) | Handles payment events |
| `cancel-subscription` | JWT required | Cancels monthly at period end |

### Edge Function Secrets (set in Supabase dashboard)
- `STRIPE_SECRET_KEY` — Stripe secret key
- `STRIPE_WEBHOOK_SECRET` — Stripe webhook signing secret
- `SB_SERVICE_ROLE_KEY` — Supabase service role key (named without SUPABASE_ prefix — Supabase blocks that prefix)

---

## Stripe Configuration

**Mode:** Test (flip to live before launch)
**Test publishable key:** pk_test_51THwruLh...
**Products:**
| Product | Price ID | Amount | Type |
|---------|----------|--------|------|
| Footsteps Full Access | price_1TdxaVLhNi71Q1IHxg3M9vIX | $49.99 | One-time |
| Footsteps Monthly | price_1Tdxb2LhNi71Q1IHq8OmNGt6 | $4.99 | Monthly recurring |

**Webhook:** Footsteps Webhook → https://bqyysvjnitbeimvaxkao.supabase.co/functions/v1/stripe-webhook
**Webhook events:** checkout.session.completed, invoice.payment_succeeded, invoice.payment_failed, customer.subscription.deleted, customer.subscription.updated

### Going live checklist
1. Create live mode products in Stripe with same names
2. Update price IDs in `create-checkout/index.ts`
3. Update `STRIPE_SECRET_KEY` secret to live key
4. Create new live webhook endpoint, update `STRIPE_WEBHOOK_SECRET`
5. Update publishable key in `index.html` and `account.html`

---

## Auth System

### Account types
- **Family (parent):** Email/password login, can add child profiles (name + age + emoji avatar, no email needed). One purchase covers the whole family.
- **Individual:** Email/password login, single profile.

### Profile switcher
Parent accounts show a dropdown in the auth bar to switch between their own profile and any child profiles. Each profile has independent progress and badges.

### Pages
- `login.html` — sign in / sign up with account type picker and emoji avatar selector
- `account.html` — plan status, cancel subscription, family profiles, sign out
- Auth bar on `index.html` — shows active profile, My Journey, My Account links

### Supabase Auth settings
- Site URL: https://futurexrp.github.io/Adventure-Through-The-Bible
- Redirect URLs: https://futurexrp.github.io/Adventure-Through-The-Bible/**

---

## Paywall System

### Feature flag
```javascript
const PAYWALL_ENABLED = false; // ← flip to true when ready to charge
```
Set to `true` when Stripe is live. All paywall code stays in place when `false`.

### Access tiers
- Stories 1–3: Free, no login required
- Stories 4–50: Requires paid access (`is_paid = true` OR `has_lifetime = true`)

### Welcome splash
- Shows on first visit only (localStorage flag: `footsteps_seen_welcome`)
- Explains 3 free stories + pricing options
- Two CTAs: explore free stories or unlock full library

### Paywall modal
- Triggers when locked story is clicked or Next → from story 3
- Shows both pricing options
- Redirects to login if not authenticated, then to Stripe checkout

---

## Badge System

9 badges total — one per era + one for completing all stories:

| Badge ID | Emoji | Name | Era |
|----------|-------|------|-----|
| creation | 🌍 | In the Beginning | creation |
| patriarchs | ⛺ | The Patriarchs | patriarchs |
| exodus | 🔥 | The Deliverer | exodus |
| promised-land | ⚔️ | The Warrior | promised-land |
| kingdom | 👑 | The Kingdom | kingdom |
| exile | 📜 | The Remnant | exile |
| nt-life | ✨ | The Witness | nt-life |
| nt-church | ⚡ | The Sent Ones | nt-church |
| complete | 🏆 | Footsteps Complete | all eras |

Badges appear in a shelf below the progress strip. Clicking any badge opens the My Journey modal showing all 9 with earned/locked status and progress counts. Badge earned popup animates up from the bottom when a new badge is unlocked.

---

## Story Register — CRITICAL

Every story must follow this exact style:

- **Message-style** — vivid, present-tense, told out loud, like a great storyteller around a fire
- **Faithful to the biblical text** — no invented dialogue or scenes beyond what Scripture gives
- **Zero commentary** — no "here's why this matters" woven into the story paragraphs
- **No verse numbers** — flows as narrative, not Scripture reference
- **Conservative Protestant theology** — free will (Arminian), high view of Scripture, miracles are real, Jesus present in OT typology
- Commentary and application go ONLY in the devotional section (Big Idea + questions)
- Big Idea: one punchy sentence, bold
- Talk About It: exactly 3 questions, age 9–12 appropriate
- Connections: exactly 3 cards, each with storyId, reference, and one-sentence why
- Quiz: exactly 3 multiple-choice questions, each with explanation text

---

## Age Tiers

### Tier 1 (Ages 9–12) — ACTIVE BUILD
- Full Message-style register
- Quiz with celebration screen
- Word highlighting during audio playback
- 30 stories target, building toward 50

### Tier 2 (Ages 5–8) — FUTURE BUILD
Build only after Tier 1 is complete with all audio.

---

## Card Flow (Modal Structure)

```
Hero (era stripe + emoji + title + hook + location + date)
  ↓
Story text (Message-style, drop cap on first letter)
  ↓
Audio player (ElevenLabs MP3 with word highlighting)
  ↓
Devotional (Big Idea + Talk About It questions)
  ↓
Connections (2-column grid, 3 cards linking to related stories)
  ↓
Quiz (3 questions, wrong answer shakes red and retries, right answer green with explanation)
  ↓
Celebration screen (stars + confetti + score badge)
  ↓
Mark as Read button (saves to Supabase or localStorage)
```

---

## Audio Generation

### Script usage
```bash
python3 generate_audio.py <story-id>
```

### ElevenLabs notes
- Plan: Creator ($22/month)
- Voice: Premium voice at 2x character usage rate
- Effective budget: ~40,000 characters per month at 2x rate (~8–10 stories)
- Always generate audio AFTER the story text is finalized

### Git workflow after generation
```bash
git add audio/
git commit -m "Add audio for story-name"
git push
```

---

## Complete Story List — Tier 1 (Ages 9–12)

### Status Key
- ✅ Done — Message-style + connections + quiz + audio complete
- 📝 Written — Message-style + connections + quiz done, audio pending
- 🔄 Needs rewrite — old commentary style, no audio
- 🔇 Audio pending

### In the Beginning (Creation Era)
| # | ID | Title | Book | Status |
|---|-----|-------|------|--------|
| 01 | creation | In the Beginning | Genesis 1–2 | ✅ Complete |
| 02 | adam-eve | The First Bad Choice | Genesis 3 | ✅ Complete |
| 03 | cain-abel | Two Brothers | Genesis 4 | ✅ Complete |

### The Age of the Patriarchs
| # | ID | Title | Book | Status |
|---|-----|-------|------|--------|
| 04 | noah | The Ark and the Rainbow | Genesis 6–9 | ✅ Complete |
| 05 | tower-babel | The Tower of Babel | Genesis 11 | ✅ Complete |
| 06 | abraham | A Promise as Big as the Stars | Genesis 12–22 | ✅ Complete |
| 07 | joseph | The Dreamer's Long Road | Genesis 37–50 | ✅ Complete |

### The Exodus and Wilderness
| # | ID | Title | Book | Status |
|---|-----|-------|------|--------|
| 08 | moses-birth | The Baby in the River | Exodus 1–2 | ✅ Complete |
| 09 | burning-bush | The Burning Bush | Exodus 3–4 | ✅ Complete |
| 10 | red-sea | Through the Sea on Dry Ground | Exodus 14–15 | ✅ Complete |
| 11 | ten-commandments | The Ten Commandments | Exodus 19–20 | 📝 Written |
| 12 | rahab | The Scarlet Thread | Joshua 2; 6 | 📝 Written |

### The Promised Land
| # | ID | Title | Book | Status |
|---|-----|-------|------|--------|
| 13 | gideon | Three Hundred Men and Torches | Judges 6–7 | 📝 Written |
| 14 | ruth | Wherever You Go | Ruth 1–4 | 📝 Written |

### The Kingdom Era
| # | ID | Title | Book | Status |
|---|-----|-------|------|--------|
| 15 | samuel | Speak, Lord | 1 Samuel 3 | 📝 Written |
| 16 | david-goliath | One Stone | 1 Samuel 17 | 🔄 Needs rewrite |
| 17 | psalm23 | The Lord Is My Shepherd | Psalm 23 | 🔄 Needs rewrite |
| 18 | elijah | Fire from Heaven | 1 Kings 17–19 | 🔄 Needs rewrite |

### Exile and Return
| # | ID | Title | Book | Status |
|---|-----|-------|------|--------|
| 19 | daniel | The Lion's Den | Daniel 6 | 🔄 Needs rewrite |
| 20 | esther | For Such a Time as This | Esther 1–10 | 🔄 Needs rewrite |

### The Life of Jesus
| # | ID | Title | Book | Status |
|---|-----|-------|------|--------|
| 21 | annunciation | Impossible News | Luke 1–2 | 🔄 Needs rewrite |
| 22 | boy-temple | Left Behind in Jerusalem | Luke 2:41–52 | 🔄 Needs rewrite |
| 23 | sermon-mount | The Upside-Down Kingdom | Matthew 5–7 | 🔄 Needs rewrite |
| 24 | prodigal | The Boy Who Came Home | Luke 15:11–32 | 🔄 Needs rewrite |
| 25 | lazarus | Come Out | John 11 | 🔄 Needs rewrite |

### Death, Resurrection and the Early Church
| # | ID | Title | Book | Status |
|---|-----|-------|------|--------|
| 26 | crucifixion | The Darkest Friday | Matthew 26–27; Luke 23; John 19 | 🔄 Needs rewrite |
| 27 | resurrection | The Empty Tomb | Matthew 28; Luke 24; John 20–21 | 🔄 Needs rewrite |
| 28 | pentecost | The Day Everything Changed | Acts 2 | 🔄 Needs rewrite |
| 29 | paul-conversion | The Man Who Hunted Christians | Acts 9; Galatians 1 | 🔄 Needs rewrite |
| 30 | paul-jail | Singing at Midnight | Acts 16:16–40 | 🔄 Needs rewrite |

---

## Audio Pending (next credit reset)
9 stories need audio regeneration:
- Story 11 — The Ten Commandments (minor wording fix)
- Story 16 — One Stone (needs rewrite first)
- Story 17 — The Lord Is My Shepherd (needs rewrite first)
- Story 18 — Fire from Heaven (needs rewrite first)
- Story 19 — The Lion's Den (needs rewrite first)
- Story 20 — For Such a Time as This (needs rewrite first)
- Story 26 — The Darkest Friday (no audio yet)
- Story 27 — The Empty Tomb (no audio yet)
- Story 30 — Singing at Midnight (no audio yet)

---

## Design System

| Element | Font | Notes |
|---------|------|-------|
| Site title | In header image | Baked into header.png |
| Era labels | Cinzel 600 | |
| Story titles | Cinzel 700 | |
| Big Idea | Cinzel 600 | |
| Body text | Lora 400 | Line height 1.85 |
| Hook / italic | Lora italic | |
| Labels / meta | Source Sans 3 600 | |

| Token | Value | Use |
|-------|-------|-----|
| --parchment | #fdf6e3 | Background |
| --ink | #2c1a0e | Primary text |
| --ink-light | #5c3d1e | Secondary text |
| --gold | #c9a227 | Accents, labels |
| --gold-bright | #f0c040 | Buttons, progress bar |
| --crimson | #8b1a1a | Drop caps, Read button |

---

## Era Color Codes

| Era ID | Label | Color |
|--------|-------|-------|
| creation | In the Beginning | #7c3aed |
| patriarchs | The Age of the Patriarchs | #b45309 |
| exodus | The Exodus and Wilderness | #b91c1c |
| promised-land | The Promised Land | #065f46 |
| kingdom | The Kingdom Era | #1e40af |
| exile | Exile and Return | #831843 |
| nt-life | The Life of Jesus | #0369a1 |
| nt-church | Death, Resurrection and the Early Church | #065f46 |

---

## GitHub Actions

`.github/workflows/deploy-functions.yml` — deploys all Edge Functions automatically on push to main when files in `supabase/functions/**` change. Requires these GitHub Secrets:
- `SUPABASE_ACCESS_TOKEN`
- `STRIPE_SECRET_KEY`
- `SUPABASE_SERVICE_ROLE_KEY`
- `STRIPE_WEBHOOK_SECRET`

Note: GitHub Actions deploy was set up but Edge Functions were ultimately deployed via the Supabase dashboard editor due to project linking issues. The Action still runs and sets secrets on each push.

---

## Pending Infrastructure

### Before launch
- [ ] Flip `PAYWALL_ENABLED = true` in `index.html`
- [ ] Switch Stripe from test to live mode
- [ ] Update price IDs in `create-checkout/index.ts`
- [ ] Update Stripe keys in Edge Function secrets + frontend
- [ ] Create live Stripe webhook endpoint
- [ ] Turn on email confirmation in Supabase Auth
- [ ] Complete stories 16–30 rewrites
- [ ] Generate audio for all 30 stories

### Future features
- [ ] Age tier tabs — 5–8 tier after 9–12 complete
- [ ] Background music — layer instrumental in Audacity before MP3 export
- [ ] PWA / mobile app consideration (v2)
- [ ] Stories 31–50
- [ ] Optimize Supabase fetches (parallelize on load)
- [ ] Add-on story packs for one-time purchasers

---

## New Session Prompt

Paste this at the top of every new chat session:

---

> **Project:** Footsteps — Bible story app for families, ages 9–12 tier
> **GitHub:** futurexrp/Adventure-Through-The-Bible
> **Live:** https://futurexrp.github.io/Adventure-Through-The-Bible/
> **Register:** Message-style — vivid, present-tense, told out loud, faithful to biblical text, zero commentary. Conservative Protestant (Arminian, high view of Scripture, miracles real, OT typology pointing to Christ).
> **Each story needs:** Message-style rewrite + 3 connections (storyId + reference + one-sentence why) + 3 quiz questions with explanations
> **Card flow:** Hero → Story → Audio player (word highlighting) → Devotional → Connections → Quiz → Celebration → Mark as Read
> **Audio:** Generated via `python3 generate_audio.py <story-id>` — always write story first, generate audio after
> **Work in batches of 5.** Check token usage before starting — each story costs ~4,000–5,000 tokens.
> **Next batch to write:** Stories 16–20 (david-goliath, psalm23, elijah, daniel, esther)
> **Infrastructure:** Supabase auth + Stripe payments fully wired. PAYWALL_ENABLED = true in index.html. See FOOTSTEPS_PROJECT.md for full details.

---

## Theological Notes

- Miracles treated as real historical events throughout — no naturalistic hedging
- Free will intact in all character decisions (Arminian framework)
- Grace before law framing: God rescues before He requires (Exodus pattern)
- OT typology pointing to Christ is explicit: ram in thicket (Abraham), scarlet cord (Rahab), kinsman-redeemer (Ruth/Boaz), I AM name (Burning Bush → John 8:58), wood on the hill (Abraham/Isaac → crucifixion)
- Gospel announced in advance to Abraham (Gal 3:8) — stated explicitly in Story 06
- Creation: Trinity hinted in "let us," six literal days presented as written
- Red Sea: called by traditional name, not "Sea of Reeds"
- Rahab described as "a prostitute" in 9–12 tier — faithful to Hebrews 11:31. **For 5–8 tier: replace with "a woman with a complicated past"**
