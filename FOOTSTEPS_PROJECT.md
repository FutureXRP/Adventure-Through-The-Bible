# Footsteps — Project Reference Document
**Last updated:** June 2026  
**GitHub:** futurexrp/Adventure-Through-The-Bible  
**Live site:** https://futurexrp.github.io/Adventure-Through-The-Bible/

---

## What This App Is

Footsteps is a premium Bible story app for families with children. Each story is told in a vivid, present-tense, Message-style register — faithful to the biblical text, zero commentary woven in, told the way a great storyteller would tell it out loud. Every story has a Big Idea, three Talk About It questions, three connection cards linking to related stories, and a three-question quiz with celebration screen.

**Tagline:** Walk through the greatest story ever told  
**Model:** One-time purchase (price TBD at launch)  
**Status:** Tier 1 (9–12) in progress — 15 of 30 stories complete with audio for stories 1–10

---

## Repo File Structure

```
your-repo/
  index.html              ← landing page + modal + quiz + audio player + word highlighting
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
```

---

## Tech Stack

- **Frontend:** Static HTML/CSS/JS — no framework, no build step
- **Hosting:** GitHub Pages (free, auto-deploys on push)
- **Data:** `stories.json` — fetched at runtime, all story content lives here
- **Audio:** ElevenLabs API — generates MP3 + character-level timestamp JSON simultaneously
- **Word highlighting:** Time-based positional matching using ElevenLabs timestamp JSON
- **Progress tracking:** localStorage (key: `footsteps_progress_v1`)
- **Future:** Supabase auth, Stripe one-time purchase paywall

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

**Example of correct register (Creation opening):**
> Before time started, before anything existed at all, God was already there. And God created — the sky, the earth, everything. At first the earth was a dark, empty, formless place, with water covering everything and God's Spirit moving over it all like wind over the surface of the deep. Then God spoke. "Light!" And light blazed into existence.

---

## Age Tiers

### Tier 1 (Ages 9–12) — ACTIVE BUILD
- Full Message-style register
- Quiz with celebration screen
- Word highlighting during audio playback
- 30 stories target, building toward 50

### Tier 2 (Ages 5–8) — FUTURE BUILD
Build only after Tier 1 is complete with all audio.

**Age-appropriate adjustments for Tier 2:**
- Replace the word "prostitute" (Rahab story) with "a woman with a complicated past" or simply omit the descriptor entirely — the story works without it
- Review all stories for vocabulary and concept complexity before adapting
- Shorter paragraphs, simpler sentences throughout
- Quiz questions should be more straightforward
- Same theological content, age-appropriate wording

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
Mark as Read button (activates after quiz completion)
```

---

## JSON Story Object Structure

```json
{
  "id": "creation",
  "era": "creation",
  "order": 1,
  "access": "free",
  "emoji": "🌍",
  "title": "In the Beginning",
  "book": "Genesis 1–2",
  "date": "Before Time",
  "location": "The Whole Earth",
  "hook": "One-sentence teaser shown on the card",
  "audio": "./audio/creation.mp3",
  "story": [
    "Paragraph one...",
    "Paragraph two..."
  ],
  "devotional": {
    "bigIdea": "One punchy sentence.",
    "questions": [
      "Question one?",
      "Question two?",
      "Question three?"
    ]
  },
  "connections": [
    {
      "title": "Connected Story Title",
      "storyId": "resurrection",
      "reference": "John 1:1–3",
      "why": "One sentence explaining the connection."
    }
  ],
  "quiz": [
    {
      "question": "Question text?",
      "options": ["Option A", "Option B", "Option C"],
      "answer": 1,
      "explanation": "Why this answer is correct."
    }
  ],
  "tags": ["creation"]
}
```

---

## Audio Generation

### Script usage
```bash
python3 generate_audio.py <story-id>
```

### How it works
1. Reads story text from `stories.json`
2. Sends to ElevenLabs `/v1/text-to-speech/{VOICE_ID}/with-timestamps` endpoint
3. Saves `audio/<story-id>.mp3` and `audio/<story-id>.json` to the audio folder
4. Both files committed together — the JSON powers word highlighting

### ElevenLabs notes
- Plan: Creator ($22/month)
- Voice: Premium voice at 2x character usage rate
- Effective budget: ~40,000 characters per month at 2x rate (~8–10 stories)
- Always generate audio AFTER the story text is finalized — changing text requires regenerating audio

### Git workflow after generation
```bash
git add audio/
git commit -m "Add audio for story-name"
git push
```

---

## Word Highlighting System

- ElevenLabs returns character-level timestamps in the JSON file
- On audio play, the app converts character timestamps to word timestamps
- Each word in the story text is wrapped in a `<span>` element
- Span index === timing index (pure positional — no text comparison)
- Standalone dashes (—) get their own span to keep indices aligned with ElevenLabs data
- 150ms lookahead compensates for browser `timeupdate` event delay
- Wrong count triggers a console warning: "COUNT MISMATCH — spans: X timings: Y"

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

## Complete Story List — Tier 1 (Ages 9–12)

### Status Key
- ✅ Done — Message-style + connections + quiz + audio complete
- 📝 Written — Message-style + connections + quiz done, audio pending
- 🔄 Needs rewrite — old commentary style
- 🔇 Audio pending

---

### In the Beginning (Creation Era)

| # | ID | Title | Book | Audio File | Status |
|---|-----|-------|------|-----------|--------|
| 01 | creation | In the Beginning | Genesis 1–2 | creation.mp3 | ✅ Complete |
| 02 | adam-eve | The First Bad Choice | Genesis 3 | adam-eve.mp3 | ✅ Complete |
| 03 | cain-abel | Two Brothers | Genesis 4 | cain-abel.mp3 | ✅ Complete |

### The Age of the Patriarchs

| # | ID | Title | Book | Audio File | Status |
|---|-----|-------|------|-----------|--------|
| 04 | noah | The Ark and the Rainbow | Genesis 6–9 | noah.mp3 | ✅ Complete |
| 05 | tower-babel | The Tower of Babel | Genesis 11 | tower-babel.mp3 | ✅ Complete |
| 06 | abraham | A Promise as Big as the Stars | Genesis 12–22 | abraham.mp3 | ✅ Complete |
| 07 | joseph | The Dreamer's Long Road | Genesis 37–50 | joseph.mp3 | ✅ Complete |

### The Exodus and Wilderness

| # | ID | Title | Book | Audio File | Status |
|---|-----|-------|------|-----------|--------|
| 08 | moses-birth | The Baby in the River | Exodus 1–2 | moses-birth.mp3 | ✅ Complete |
| 09 | burning-bush | The Burning Bush | Exodus 3–4 | burning-bush.mp3 | ✅ Complete |
| 10 | red-sea | Through the Sea on Dry Ground | Exodus 14–15 | red-sea.mp3 | ✅ Complete |
| 11 | ten-commandments | The Ten Commandments | Exodus 19–20 | ten-commandments.mp3 | 📝 Written |
| 12 | rahab | The Scarlet Thread | Joshua 2; 6 | rahab.mp3 | 📝 Written |

### The Promised Land

| # | ID | Title | Book | Audio File | Status |
|---|-----|-------|------|-----------|--------|
| 13 | gideon | Three Hundred Men and Torches | Judges 6–7 | gideon.mp3 | 📝 Written |
| 14 | ruth | Wherever You Go | Ruth 1–4 | ruth.mp3 | 📝 Written |

### The Kingdom Era

| # | ID | Title | Book | Audio File | Status |
|---|-----|-------|------|-----------|--------|
| 15 | samuel | Speak, Lord | 1 Samuel 3 | samuel.mp3 | 📝 Written |
| 16 | david-goliath | One Stone | 1 Samuel 17 | david-goliath.mp3 | 🔄 Needs rewrite |
| 17 | psalm23 | The Lord Is My Shepherd | Psalm 23 | psalm23.mp3 | 🔄 Needs rewrite |
| 18 | elijah | Fire from Heaven | 1 Kings 17–19 | elijah.mp3 | 🔄 Needs rewrite |

### Exile and Return

| # | ID | Title | Book | Audio File | Status |
|---|-----|-------|------|-----------|--------|
| 19 | daniel | The Lion's Den | Daniel 6 | daniel.mp3 | 🔄 Needs rewrite |
| 20 | esther | For Such a Time as This | Esther 1–10 | esther.mp3 | 🔄 Needs rewrite |

### The Life of Jesus

| # | ID | Title | Book | Audio File | Status |
|---|-----|-------|------|-----------|--------|
| 21 | annunciation | Impossible News | Luke 1–2 | annunciation.mp3 | 🔄 Needs rewrite |
| 22 | boy-temple | Left Behind in Jerusalem | Luke 2:41–52 | boy-temple.mp3 | 🔄 Needs rewrite |
| 23 | sermon-mount | The Upside-Down Kingdom | Matthew 5–7 | sermon-mount.mp3 | 🔄 Needs rewrite |
| 24 | prodigal | The Boy Who Came Home | Luke 15:11–32 | prodigal.mp3 | 🔄 Needs rewrite |
| 25 | lazarus | Come Out | John 11 | lazarus.mp3 | 🔄 Needs rewrite |

### Death, Resurrection and the Early Church

| # | ID | Title | Book | Audio File | Status |
|---|-----|-------|------|-----------|--------|
| 26 | crucifixion | The Darkest Friday | Matthew 26–27; Luke 23; John 19 | crucifixion.mp3 | 🔄 Needs rewrite |
| 27 | resurrection | The Empty Tomb | Matthew 28; Luke 24; John 20–21 | resurrection.mp3 | 🔄 Needs rewrite |
| 28 | pentecost | The Day Everything Changed | Acts 2 | pentecost.mp3 | 🔄 Needs rewrite |
| 29 | paul-conversion | The Man Who Hunted Christians | Acts 9; Galatians 1 | paul-conversion.mp3 | 🔄 Needs rewrite |
| 30 | paul-jail | Singing at Midnight | Acts 16:16–40 | paul-jail.mp3 | 🔄 Needs rewrite |

---

## Stories Beyond 30 (Target: 50 Stories)

### Old Testament additions

| ID | Title | Book | Era | Audio File |
|----|-------|------|-----|-----------|
| jonah | The Man Who Ran From God | Jonah 1–4 | exile | jonah.mp3 |
| nehemiah | The Wall Goes Up | Nehemiah 1–6 | exile | nehemiah.mp3 |
| job | The Man Who Lost Everything | Job 1–2; 38–42 | kingdom | job.mp3 |
| elisha | The Floating Axe Head | 2 Kings 6:1–7 | kingdom | elisha.mp3 |
| isaiah-servant | The Servant Who Suffers | Isaiah 52–53 | kingdom | isaiah-servant.mp3 |
| shadrach | The Furnace | Daniel 3 | exile | shadrach.mp3 |
| moses-water | Water From a Rock | Exodus 17 | exodus | moses-water.mp3 |
| jericho | The Walls Fall Down | Joshua 6 | promised-land | jericho.mp3 |
| david-saul | The Cave and the King | 1 Samuel 24 | kingdom | david-saul.mp3 |
| solomon-wisdom | The Wisest Request | 1 Kings 3 | kingdom | solomon-wisdom.mp3 |

### New Testament additions

| ID | Title | Book | Era | Audio File |
|----|-------|------|-----|-----------|
| feeding-5000 | Five Loaves and Two Fish | John 6:1–14 | nt-life | feeding-5000.mp3 |
| walk-on-water | Stepping Out | Matthew 14:22–33 | nt-life | walk-on-water.mp3 |
| zacchaeus | The Man in the Tree | Luke 19:1–10 | nt-life | zacchaeus.mp3 |
| good-samaritan | The One Who Stopped | Luke 10:25–37 | nt-life | good-samaritan.mp3 |
| woman-at-well | The Woman at the Well | John 4:1–42 | nt-life | woman-at-well.mp3 |
| lost-sheep | The Shepherd Who Searched | Luke 15:1–7 | nt-life | lost-sheep.mp3 |
| triumphal-entry | The King Rides In | Matthew 21:1–11 | nt-church | triumphal-entry.mp3 |
| road-emmaus | The Stranger on the Road | Luke 24:13–35 | nt-church | road-emmaus.mp3 |
| stephen | The First Martyr | Acts 6–7 | nt-church | stephen.mp3 |
| lydia | The Purple Merchant | Acts 16:11–15 | nt-church | lydia.mp3 |

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
> **Reference:** FOOTSTEPS_PROJECT.md in the repo  
> **Next batch to write:** Stories 16–20 (david-goliath, psalm23, elijah, daniel, esther)

---

## Theological Notes

- Miracles treated as real historical events throughout — no naturalistic hedging
- Free will intact in all character decisions (Arminian framework)
- Grace before law framing: God rescues before He requires (Exodus pattern)
- OT typology pointing to Christ is explicit: ram in thicket (Abraham), scarlet cord (Rahab), kinsman-redeemer (Ruth/Boaz), I AM name (Burning Bush → John 8:58), wood on the hill (Abraham/Isaac → crucifixion)
- Gospel announced in advance to Abraham (Gal 3:8) — stated explicitly in Story 06
- Creation: Trinity hinted in "let us," six literal days presented as written
- Red Sea: called by traditional name, not "Sea of Reeds" — deliberate for audience recognition
- Population figures (two million at Exodus): traditional reading used — contested among scholars but familiar to audience
- Rahab described as "a prostitute" in 9–12 tier — faithful to Hebrews 11:31 and Joshua 2:1. **For 5–8 tier: replace with "a woman with a complicated past" or omit descriptor entirely**

## Pending Infrastructure

- [ ] Supabase auth — user accounts, cross-device progress
- [ ] Stripe or Gumroad one-time purchase ($14.99 target)
- [ ] Age tier tabs (9–12 done first, then 5–8)
- [ ] Background music — layer instrumental in Audacity before MP3 export
- [ ] PWA / mobile app consideration (v2)

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
