# Footsteps — Project Reference Document
**Last updated:** June 2026
**GitHub:** futurexrp/Adventure-Through-The-Bible
**Live site:** https://futurexrp.github.io/Adventure-Through-The-Bible/

---

## What This App Is

Footsteps is a premium Bible story app for families with children. Each story is told in a vivid, present-tense, Message-style register — faithful to the biblical text, zero commentary woven in, told the way a great storyteller would tell it out loud. Every story has a Big Idea, three Talk About It questions, three connection cards linking to related stories, and a five-question quiz with celebration screen.

**Tagline:** Walk through the greatest story ever told
**Model:** One-time purchase ($49.99) or monthly subscription ($4.99/month)
**Status:** 50 stories complete, audio for stories 1–10, ready for launch after audio generation

---

## Repo File Structure

```
Adventure-Through-The-Bible/
  index.html                    ← main app
  login.html                    ← sign in / sign up
  account.html                  ← account management
  stories.json                  ← ALL story content lives here
  header.png                    ← watercolor banner
  generate_audio.py             ← ElevenLabs audio script
  FOOTSTEPS_PROJECT.md          ← this file
  audio/
    creation.mp3 + .json        ← stories 1-10 have audio
    adam-eve.mp3 + .json
    cain-abel.mp3 + .json
    noah.mp3 + .json
    tower-babel.mp3 + .json
    abraham.mp3 + .json
    joseph.mp3 + .json
    moses-birth.mp3 + .json
    burning-bush.mp3 + .json
    red-sea.mp3 + .json
    (stories 11-50 pending)
  supabase/
    config.toml
    functions/
      create-checkout/index.ts
      stripe-webhook/index.ts
      cancel-subscription/index.ts
  .github/
    workflows/
      deploy-functions.yml
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Static HTML/CSS/JS, no framework, no build step |
| Hosting | GitHub Pages — auto-deploys on push to main |
| Data | stories.json — fetched at runtime |
| Auth | Supabase Auth — email/password |
| Database | Supabase Postgres |
| Payments | Stripe — one-time + monthly subscription |
| Edge Functions | Supabase Edge Functions (Deno) |
| Audio | ElevenLabs API — MP3 + character-level timestamps |
| Word Highlighting | requestAnimationFrame loop + binary search against ElevenLabs timestamp array |
| Progress | Supabase (logged in) or localStorage (guest) |

---

## Supabase Configuration

**Project URL:** https://bqyysvjnitbeimvaxkao.supabase.co
**Project Ref:** bqyysvjnitbeimvaxkao
**Auth Site URL:** https://futurexrp.github.io/Adventure-Through-The-Bible
**Auth Redirect URLs:** https://futurexrp.github.io/Adventure-Through-The-Bible/**

### Database Tables

| Table | Purpose |
|-------|---------|
| `profiles` | One row per auth user |
| `child_profiles` | Children under parent accounts |
| `story_progress` | Completed stories per profile |
| `quiz_attempts` | Quiz scores per story per profile |
| `badges` | Earned badges with story count at earn time |
| `mastery_attempts` | Hero Quiz scores and pass/fail |

### Key Profile Columns

| Column | Type | Purpose |
|--------|------|---------|
| `account_type` | text | `parent` or `individual` |
| `avatar_emoji` | text | Chosen emoji avatar |
| `is_paid` | bool | Active access (monthly or one-time) |
| `has_lifetime` | bool | Permanent access to stories at purchase date — NEVER reset by cancellation |
| `plan_type` | text | `one_time`, `monthly`, `monthly_cancelling`, null |
| `stripe_customer_id` | text | Stripe customer reference |
| `stripe_subscription_id` | text | For monthly subscribers |
| `paid_at` | timestamptz | When purchase was made |
| `story_count_at_purchase` | int | Story count when one-time purchase made |
| `last_seen_story_count` | int | For new story notifications |

### Key Badge Columns

| Column | Type | Purpose |
|--------|------|---------|
| `badge_id` | text | Badge identifier |
| `story_count_at_earn` | int | Era story count when badge earned — used for revocation detection |

### Access Logic

```
Monthly subscriber       → access to ALL stories (current and future)
One-time buyer           → access to stories where published_date <= paid_at
One-time buyer cancelled → is_paid may drop but has_lifetime stays true
Guest                    → stories 1-3 only
```

### Edge Function Secrets (Supabase dashboard)

| Secret | Description |
|--------|-------------|
| `STRIPE_SECRET_KEY` | Stripe secret key (sk_test_ or sk_live_) |
| `STRIPE_WEBHOOK_SECRET` | Stripe webhook signing secret (whsec_) |
| `SB_SERVICE_ROLE_KEY` | Supabase service role key — named without SUPABASE_ prefix |

---

## Stripe Configuration

**Mode:** Test (not yet live)
**Test publishable key:** pk_test_51THwruLh...

### Products

| Product | Price ID | Amount | Type |
|---------|----------|--------|------|
| Footsteps Full Access | price_1TdxaVLhNi71Q1IHxg3M9vIX | $49.99 | One-time |
| Footsteps Monthly | price_1Tdxb2LhNi71Q1IHq8OmNGt6 | $4.99/mo | Recurring |

**Webhook:** Footsteps Webhook → https://bqyysvjnitbeimvaxkao.supabase.co/functions/v1/stripe-webhook
**Webhook events:** checkout.session.completed, invoice.payment_succeeded, invoice.payment_failed, customer.subscription.deleted, customer.subscription.updated

---

## Story Release Process — New Batches

### How it works

Every story has a `published_date` field in stories.json. This is the control mechanism for what each account type can access:

- **Monthly subscribers** see all stories automatically
- **One-time buyers** can only access stories where `published_date <= their paid_at date`
- New stories with a future `published_date` are automatically locked for one-time buyers

### To release a new batch

1. Write new stories (new Claude session, follow register rules below)
2. Set `published_date` to today's date on new stories only
3. Commit `stories.json` — everything else is automatic

### One-time buyer options for new stories

When new stories are released after a buyer's purchase date, they see a dismissible banner:

**Option A — Subscribe monthly ($4.99/mo):** Gets all new stories plus every future story. Managed in account.html.

**Option B — Story Pack purchase ($9.99 one-time):** Gets access to the specific batch of new stories permanently. Still needs to be built — see Pending Infrastructure below.

### Story Pack (still to build)

- New Stripe product: `Footsteps Story Pack` at $9.99 one-time
- Add `story_packs` table in Supabase tracking which packs a user has purchased
- Add `pack_id` field to stories.json (e.g. `pack_1`, `pack_2`)
- Update `storyIsLocked` to check both `paid_at` and owned packs
- Add pack purchase option to paywall modal and account.html
- New Edge Function: `purchase-pack`

---

## Paywall System

### Feature flag
```javascript
const PAYWALL_ENABLED = true; // in index.html
```
Set to `false` to disable all locking for development.

### Access tiers
- Stories 1–3: Free, no login required
- Stories 4+: Requires paid access

### Welcome splash
- First visit only (localStorage flag: `footsteps_seen_welcome`)
- Explains 3 free stories + both pricing options

### Notifications
- **One-time buyer new story banner** — dismissible gold strip when stories exist after purchase date
- **Badge revocation banner** — warm notification when new stories added to a completed era
- **Paywall modal** — triggered by locked story click or Next from story 3

---

## Badge System

### Era Badges (9 total)

| Badge ID | Emoji | Name | Era | Revocable |
|----------|-------|------|-----|-----------|
| creation | 🌍 | In the Beginning | creation | Yes |
| patriarchs | ⛺ | The Patriarchs | patriarchs | Yes |
| exodus | 🔥 | The Deliverer | exodus | Yes |
| promised-land | ⚔️ | The Warrior | promised-land | Yes |
| kingdom | 👑 | The Kingdom | kingdom | Yes |
| exile | 📜 | The Remnant | exile | Yes |
| nt-life | ✨ | The Witness | nt-life | Yes |
| nt-church | ⚡ | The Sent Ones | nt-church | Yes |
| complete | 🏆 | Footsteps Complete | all | No |
| hero | 🌟 | Hero | all | No |

### Badge Revocation
- On app load, compares `story_count_at_earn` on each badge against current era story count
- If new stories added to era, badge is revoked in Supabase and a warm banner shows
- Banner: "New stories added to [Era] — your badge is waiting to be reclaimed!"
- Badge stays displayed until new story is completed, then re-awards naturally with full celebration

### Hero Quiz
- Unlocks in Journey modal after ALL stories are read
- 25 questions drawn randomly from existing quiz banks, spread across eras
- Requires 80% to pass (20/25)
- Awards 🌟 Hero badge on first pass
- Retakeable — only celebrate on first perfect pass
- Score saved to `mastery_attempts` table

---

## Auth System

### Account Types
- **Family:** Parent email/password, adds child profiles (name + age + emoji avatar, no email needed)
- **Individual:** Single profile, email/password

### Profile Switcher
- Dropdown in auth bar, switch between parent and child profiles
- Each profile has independent progress, badges, and quiz history

### Pages
- `login.html` — sign in/create account, account type picker, emoji avatar picker
- `account.html` — plan status, cancel subscription, family profiles with progress, avatar editing

---

## Story Register — CRITICAL

Every story must follow this exact style:

- **Message-style** — vivid, present-tense, told out loud like a great storyteller around a fire
- **Faithful to the biblical text** — no invented dialogue or scenes beyond what Scripture gives
- **Zero commentary** — no "here's why this matters" woven into story paragraphs
- **No verse numbers** — flows as narrative
- **No em dashes (`—`) in story paragraphs** — use commas or rewrite. Em dashes cause word highlighting drift. Stories 1–10 already have audio so leave existing dashes. Apply to all new stories.
- **Conservative Protestant theology** — free will (Arminian), high view of Scripture, miracles real, OT typology pointing to Christ
- Big Idea: one punchy sentence
- Talk About It: exactly 3 questions, age 9–12 appropriate
- Connections: exactly 3 cards, each with storyId + reference + one-sentence why
- Quiz: exactly 5 questions, correct answers spread evenly across A/B/C/D

---

## Complete 50-Story List

### In the Beginning (Creation Era)
| # | ID | Title | Book | Audio | Status |
|---|---|---|---|---|---|
| 01 | creation | In the Beginning | Genesis 1–2 | ✅ | Complete |
| 02 | adam-eve | The First Bad Choice | Genesis 3 | ✅ | Complete |
| 03 | cain-abel | Two Brothers | Genesis 4 | ✅ | Complete |

### The Age of the Patriarchs
| # | ID | Title | Book | Audio | Status |
|---|---|---|---|---|---|
| 04 | noah | The Ark and the Rainbow | Genesis 6–9 | ✅ | Complete |
| 05 | tower-babel | The Tower of Babel | Genesis 11 | ✅ | Complete |
| 06 | abraham | A Promise as Big as the Stars | Genesis 12–22 | ✅ | Complete |
| 07 | joseph | The Dreamer's Long Road | Genesis 37–50 | ✅ | Complete |

### The Exodus and Wilderness
| # | ID | Title | Book | Audio | Status |
|---|---|---|---|---|---|
| 08 | moses-birth | The Baby in the River | Exodus 1–2 | ✅ | Complete |
| 09 | burning-bush | The Burning Bush | Exodus 3–4 | ✅ | Complete |
| 10 | red-sea | Through the Sea on Dry Ground | Exodus 14–15 | ✅ | Complete |
| 11 | ten-commandments | The Ten Commandments | Exodus 19–20 | 🔇 | Written |
| 12 | moses-water | Water From the Rock | Exodus 17 | 🔇 | Written |

### The Promised Land
| # | ID | Title | Book | Audio | Status |
|---|---|---|---|---|---|
| 13 | rahab | The Scarlet Thread | Joshua 2; 6 | 🔇 | Written |
| 14 | jericho | The Walls Come Down | Joshua 6 | 🔇 | Written |
| 15 | gideon | Three Hundred Men and Torches | Judges 6–7 | 🔇 | Written |
| 16 | ruth | Wherever You Go | Ruth 1–4 | 🔇 | Written |

### The Kingdom Era
| # | ID | Title | Book | Audio | Status |
|---|---|---|---|---|---|
| 17 | samuel | Speak, Lord | 1 Samuel 3 | 🔇 | Written |
| 18 | david-goliath | One Stone | 1 Samuel 17 | 🔇 | Written |
| 19 | david-saul | The Cave and the King | 1 Samuel 24 | 🔇 | Written |
| 20 | psalm23 | The Lord Is My Shepherd | Psalm 23 | 🔇 | Written |
| 21 | solomon-wisdom | The Wisest Request | 1 Kings 3 | 🔇 | Written |
| 22 | elijah | Fire from Heaven | 1 Kings 17–19 | 🔇 | Written |
| 23 | job | The Man Who Lost Everything | Job 1–2; 38–42 | 🔇 | Written |
| 24 | isaiah-servant | The Servant Who Suffers | Isaiah 52–53 | 🔇 | Written |

### Exile and Return
| # | ID | Title | Book | Audio | Status |
|---|---|---|---|---|---|
| 25 | shadrach | The Furnace | Daniel 3 | 🔇 | Written |
| 26 | daniel | The Lion's Den | Daniel 6 | 🔇 | Written |
| 27 | esther | For Such a Time as This | Esther 1–10 | 🔇 | Written |
| 28 | jonah | The Man Who Ran From God | Jonah 1–4 | 🔇 | Written |
| 29 | nehemiah | The Wall Goes Up | Nehemiah 1–6 | 🔇 | Written |

### The Life of Jesus
| # | ID | Title | Book | Audio | Status |
|---|---|---|---|---|---|
| 30 | annunciation | Impossible News | Luke 1–2 | 🔇 | Written |
| 31 | boy-temple | Left Behind in Jerusalem | Luke 2:41–52 | 🔇 | Written |
| 32 | sermon-mount | The Upside-Down Kingdom | Matthew 5–7 | 🔇 | Written |
| 33 | woman-at-well | The Woman at the Well | John 4:1–42 | 🔇 | Written |
| 34 | feeding-5000 | Five Loaves and Two Fish | John 6:1–14 | 🔇 | Written |
| 35 | walk-on-water | Stepping Out | Matthew 14:22–33 | 🔇 | Written |
| 36 | good-samaritan | The One Who Stopped | Luke 10:25–37 | 🔇 | Written |
| 37 | zacchaeus | The Man in the Tree | Luke 19:1–10 | 🔇 | Written |
| 38 | triumphal-entry | The King Rides In | Matthew 21:1–11 | 🔇 | Written |
| 39 | rich-young-ruler | The Man Who Walked Away | Mark 10:17–27 | 🔇 | Written |
| 40 | prodigal | The Boy Who Came Home | Luke 15:11–32 | 🔇 | Written |
| 41 | lazarus | Come Out | John 11 | 🔇 | Written |

### Death, Resurrection and the Early Church
| # | ID | Title | Book | Audio | Status |
|---|---|---|---|---|---|
| 42 | last-supper | The Night Before | Matthew 26:17–30; John 13 | 🔇 | Written |
| 43 | crucifixion | The Darkest Friday | Matthew 26–27; Luke 23; John 19 | 🔇 | Written |
| 44 | resurrection | The Empty Tomb | Matthew 28; Luke 24; John 20–21 | 🔇 | Written |
| 45 | road-emmaus | The Stranger on the Road | Luke 24:13–35 | 🔇 | Written |
| 46 | pentecost | The Day Everything Changed | Acts 2 | 🔇 | Written |
| 47 | stephen | The First Martyr | Acts 6–7 | 🔇 | Written |
| 48 | paul-conversion | The Man Who Hunted Christians | Acts 9; Galatians 1 | 🔇 | Written |
| 49 | paul-jail | Singing at Midnight | Acts 16:16–40 | 🔇 | Written |
| 50 | lydia | The Purple Merchant | Acts 16:11–15 | 🔇 | Written |

---

## Audio Generation

### Script usage
```bash
python3 generate_audio.py <story-id>
```

Generates `audio/<story-id>.mp3` and `audio/<story-id>.json` simultaneously.

### ElevenLabs notes
- Plan: Creator ($22/month)
- Voice: Premium voice at 2x character usage rate
- Effective budget: ~40,000 characters per month (~8–10 stories)
- Always write story first, generate audio after — changing text requires regenerating
- Stories 1–10: audio complete, do not change story text without regenerating
- Stories 11–50: ready for audio generation

### Audio pending (stories 11–50)
Generate in order. Each story costs approximately 2,000–4,000 characters at 2x rate.

### Git workflow after generation
```bash
git add audio/
git commit -m "Add audio for story-name"
git push
```

---

## Design System

### Fonts
| Element | Font |
|---------|------|
| Era labels | Cinzel 600 |
| Story titles | Cinzel 700 |
| Big Idea | Cinzel 600 |
| Body text | Lora 400, line height 1.85 |
| Hook / italic | Lora italic |
| Labels / meta | Source Sans 3 600 |

### Colors
| Token | Value | Use |
|-------|-------|-----|
| --parchment | #fdf6e3 | Background |
| --ink | #2c1a0e | Primary text |
| --ink-light | #5c3d1e | Secondary text |
| --gold | #c9a227 | Accents, labels |
| --gold-bright | #f0c040 | Buttons, progress bar |
| --crimson | #8b1a1a | Drop caps, Read button |

### Era Colors
| Era ID | Color |
|--------|-------|
| creation | #7c3aed |
| patriarchs | #b45309 |
| exodus | #b91c1c |
| promised-land | #065f46 |
| kingdom | #1e40af |
| exile | #831843 |
| nt-life | #0369a1 |
| nt-church | #065f46 |

---

## Age Tiers

### Tier 1 (Ages 9–12) — COMPLETE
50 stories, full quiz system, word highlighting, badge system, Hero Quiz.

### Tier 2 (Ages 5–8) — IN PROGRESS

**Separate file:** `stories-tier2.json` — same structure as `stories.json` but with age-appropriate content. The app loads the correct file based on the active profile's tier setting.

**Tier switching:**
- Parent toggles between Tier 1 and Tier 2 per child profile in account.html
- No date of birth required — age field remains optional and informational only
- Active tier stored on `child_profiles` table as `tier` column (1 or 2, default 1)
- Progress tracked separately per tier per profile — switching tiers preserves progress in both
- Parent can switch freely at any time based on readiness, not age

**SQL needed:**
```sql
alter table public.child_profiles
  add column if not exists tier int not null default 1 check (tier in (1, 2));
```

**Index.html changes needed:**
- On profile switch, check `activeProfile.tier`
- Load `stories-tier2.json` instead of `stories.json` when tier = 2
- Tier toggle button in profile dropdown and account.html

**Age-appropriate adjustments for Tier 2:**
- Shorter paragraphs, simpler sentences, no complex theological vocabulary
- 3 quiz questions instead of 5 (simpler format)
- Talk About It questions aimed at 5–8 year olds
- Replace "prostitute" in Rahab with "a woman with a complicated past"
- Same theological content and OT typology — just accessible wording
- No em dashes in any paragraphs (audio rule same as Tier 1)
- Same story register rules otherwise: vivid, present-tense, zero commentary

---

## Pending Infrastructure

### Before launch (required)
- [ ] Generate audio for stories 11–50 via ElevenLabs
- [ ] Switch Stripe from test to live mode
- [ ] Create live Stripe products with same names and prices
- [ ] Update price IDs in `create-checkout/index.ts`
- [ ] Update `STRIPE_SECRET_KEY` and `STRIPE_WEBHOOK_SECRET` in Supabase secrets
- [ ] Create live Stripe webhook endpoint pointing to same Edge Function URL
- [ ] Update publishable key in `index.html` (search for `pk_test_`)
- [ ] Update Edge Functions in Supabase editor (stripe-webhook.ts and create-checkout.ts have pending changes for story_count_at_purchase — deploy when going live)
- [ ] Turn on email confirmation in Supabase Auth → Providers → Email
- [ ] Test full purchase flow end to end with live keys before announcing

### Tier 2 system (partially built — stories in progress)
- [ ] Run SQL: `alter table public.child_profiles add column if not exists tier int not null default 1 check (tier in (1, 2));`
- [ ] Add tier toggle to profile dropdown in index.html
- [ ] Add tier toggle to account.html child profile cards
- [ ] Update loadProgressForActiveProfile to load stories-tier2.json when tier = 2
- [ ] Audio generation for Tier 2 stories via ElevenLabs

### Story Pack system (next build)
For one-time buyers to purchase new story batches at $9.99:
- [ ] New Stripe product: `Footsteps Story Pack` at $9.99 one-time
- [ ] Add `story_packs` table in Supabase: `(id, profile_id, profile_type, pack_id, purchased_at)`
- [ ] Add `pack_id` field to stories.json (e.g. `pack_1` for launch batch, `pack_2` for next)
- [ ] Update `storyIsLocked` in index.html to check owned packs in addition to paid_at
- [ ] Add pack purchase button to paywall modal and account.html
- [ ] New Edge Function: `purchase-pack`
- [ ] Webhook handler for pack purchases in stripe-webhook.ts
- [ ] Update account.html to show owned packs

### Future features
- [ ] Tier 2 (Ages 5–8) stories — after Tier 1 launch
- [ ] Background music — layer instrumental in Audacity before MP3 export
- [ ] PWA / mobile app (v2)
- [ ] Stories 51+ (next batch after launch)
- [ ] Parallelize Supabase fetches on load to reduce perceived load time

---

## GitHub Actions

`.github/workflows/deploy-functions.yml` — deploys Edge Functions on push when `supabase/functions/**` changes.

**Required GitHub Secrets:**
- `SUPABASE_ACCESS_TOKEN`
- `STRIPE_SECRET_KEY`
- `SUPABASE_SERVICE_ROLE_KEY`
- `STRIPE_WEBHOOK_SECRET`

Note: Functions were also deployed manually via Supabase dashboard editor. Either method works.

---

## New Session Prompt

Paste at the top of every new Claude session:

---

> **Project:** Footsteps — Bible story app, ages 9–12
> **GitHub:** futurexrp/Adventure-Through-The-Bible
> **Live:** https://futurexrp.github.io/Adventure-Through-The-Bible/
> **Supabase:** bqyysvjnitbeimvaxkao.supabase.co
>
> **Story register:** Message-style — vivid, present-tense, told out loud, faithful to biblical text, zero commentary. Conservative Protestant (Arminian, high view of Scripture, miracles real, OT typology pointing to Christ). No em dashes in story paragraphs. 5 quiz questions per story, answers spread evenly across A/B/C/D. 3 connections per story.
>
> **50 stories complete.** Stories 1–10 have audio. Stories 11–50 need audio generation.
>
> **Paywall:** PAYWALL_ENABLED = true. Stripe in test mode — not yet live.
>
> **Next priorities:**
> 1. Generate audio for stories 11–50 (ElevenLabs, run in batches per credit reset)
> 2. Build story pack system ($9.99 one-time for new story batches)
> 3. Switch Stripe to live mode when ready to charge
> 4. Tier 2 (Ages 5–8) — `stories-tier2.json` in progress, tier toggle UI still needed
>
> **Reference:** FOOTSTEPS_PROJECT.md in the repo for full details.

---

## Theological Notes

- Miracles treated as real historical events — no naturalistic hedging
- Free will intact in all character decisions (Arminian framework)
- Grace before law: God rescues before He requires (Exodus pattern)
- OT typology pointing to Christ is explicit throughout
- Creation: Trinity hinted in "let us," six literal days presented as written
- Red Sea: traditional name used, not "Sea of Reeds"
- Rahab: described as "a prostitute" in 9–12 tier — faithful to Hebrews 11:31. For 5–8 tier: replace with "a woman with a complicated past"
