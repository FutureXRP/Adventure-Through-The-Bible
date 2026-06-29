# Footsteps — Meta (Facebook / Instagram) Campaign Setup

## 1. Objective: Traffic vs. Sales

| | **Traffic** (optimize for *Landing Page Views*) | **Sales** (optimize for *Purchase*) |
|---|---|---|
| What Meta does | Finds people likely to **click and load** the page | Finds people likely to **buy** |
| Needs the Pixel? | Helpful, not required | **Required**, plus ~50 purchase events/week to exit "learning" |
| Cost per click | Lowest | Higher CPC, but higher-quality traffic |
| Best for | Cold start, seeding the Pixel, cheap awareness | Once you have conversion data and a real checkout |
| Risk | Optimizes for *clickers*, not *buyers* | Starves early when there's little/no purchase data |

**Recommendation — run it in two phases:**

1. **Weeks 1–2 — Traffic → Landing Page Views.** Cheapest way to get real
   visitors, prove which *angle* and *audience* win, and let the Pixel collect
   data (PageView + CompleteRegistration are already wired — see note below).
2. **Week 3+ — Sales → Purchase** (or **Leads → CompleteRegistration** if the
   product stays free). Once the Pixel has fired ~50 conversions in a week,
   switch the winning creative into a conversion-optimized campaign for the best
   cost-per-result.

> **Pixel status:** The Meta Pixel is installed on the site (`pixel.js`) and
> fires `PageView`, `CompleteRegistration` (on sign-up), and a custom
> `StoryComplete`. Paste your Pixel ID into the first line of `pixel.js` to turn
> it on. Without it you can't run the Sales phase, retarget, or build
> lookalikes — so do this first.

**Campaign structure:** Start with **Advantage+ / CBO** at the campaign level,
~$20–30/day total, 2–3 ad sets. Let each ad set run **3–5 days untouched**
(editing resets the learning phase). Kill anything well above your target
cost-per-result; scale winners 20–30% every few days.

---

## 2. Placements

Use **Advantage+ Placements** (let Meta distribute) for the cold launch — it's
almost always cheaper than hand-picking. Just make sure you upload all three
aspect ratios so every placement looks intentional:

- **1:1 / 4:5** → Facebook + Instagram Feed (the `ad-creative.html` cards)
- **9:16** → Stories + Reels (most inventory and the cheapest CPMs right now)
- Keep critical text in the middle 80% so Stories/Reels UI doesn't cover it.

Once you have a winner, you *can* split Feed vs. Reels into separate ad sets to
control budget by surface — but only after Advantage+ tells you where it's working.

---

## 3. Audiences

> **Important targeting limitation:** Meta removed most **religion-based**
> detailed targeting — you generally **cannot** target "Christianity" or
> "Bible" as an interest anymore. Use the adjacent **brands, media, and
> behaviors** below, lean **broad + strong creative**, and graduate to
> **Lookalikes** as soon as the Pixel has data. Also: by policy your ad copy
> must not *imply you know the viewer's religion* ("As a Christian, you…" = a
> violation). Keep it about the product and the kids.

### A. Homeschool families
- **Age/parents:** 28–55 · Parents (with children 03–12)
- **Interests/brands:** Homeschooling · The Old Schoolhouse · Abeka ·
  Sonlight Curriculum · Classical Conversations · The Good and the Beautiful ·
  Charlotte Mason · Apologia
- **Why:** these brand interests survive Meta's restrictions and skew
  intentional-faith + education.

### B. Christian parents (broad)
- **Age/parents:** 27–50 · Parents (with children 03–12)
- **Interests/brands/media:** YouVersion · Bible Gateway · K‑LOVE · Air1 ·
  VeggieTales · Focus on the Family · Compassion International · Hillsong ·
  Christian contemporary music
- **Why:** faith-media + ministry brands are the cleanest proxy for
  practicing Christian households now that interest targeting is limited.
- **Tip:** also run a **no-targeting "broad" ad set** (just age + parents) —
  with good creative it frequently beats interest stacks and scales further.

### C. Gift-buyers (grandparents)
- **Age:** 50–70+
- **Interests/behaviors:** Grandparents · Grandchildren · LifeWay Christian
  Stores · Mardel · Hobby Lobby · Christian bookstores · Engaged Shoppers ·
  seasonal layering (Christmas, birthdays)
- **Why:** matches Angle 4 (the gift). Run this heaviest **Oct–Dec** and around
  major gift seasons.

### D. (Add once the Pixel has data) Retargeting + Lookalikes
- **Retarget:** site visitors who didn't sign up / didn't purchase (last 30 days).
- **Lookalike 1–3%** off your strongest source: purchasers > sign-ups > all
  visitors. Lookalikes off real customers are usually your **best** audience —
  they just need the Pixel to mature first.

---

## 4. What to A/B test first (in order)

1. **Angle, not wording.** Biggest lever by far. Run **Angle 1 (whole story in
   order)** vs **Angle 2 (screen-time guilt)** vs **Angle 5 (one-time
   purchase)** to the *same* broad audience, one ad each. Decide on
   cost-per-landing-page-view (or per result), not on which you personally like.
2. **Creative format.** Static Feed card (`ad-creative.html`) vs a simple
   screen-recording/video of the app with narration playing. Video usually wins
   cold traffic on Reels — but test it; static often wins on cost.
3. **Audience: broad vs. interest stacks.** One ad set targeting only age +
   parents (broad, Advantage+) vs the interest stacks in §3. Modern Meta often
   rewards broad + great creative; let the data, not assumptions, decide.

**Secondary tests** (only after the above): headline/hook line, CTA button
(*Learn More* vs *Shop Now*), and first 3 seconds of any video.

**Read results on:** cost per landing-page view and **link CTR** in Phase 1;
cost per **CompleteRegistration / Purchase** in Phase 2. Ignore likes/comments —
they don't pay the bills.
