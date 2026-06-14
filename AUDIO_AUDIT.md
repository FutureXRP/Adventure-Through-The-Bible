# Footsteps — Tier 1 Audio Sync Audit

*Snapshot generated 2026-06-14. Regenerate any time with `python3 verify_audio.py` and `python3 generate_audio.py --list`.*

## Bottom line

- **10 of 50** stories have audio that matches the text **exactly** (every spoken word = highlighted word). These are stories 1–10, fixed by em-dash cleanup — no regeneration.
- **17 stories** have audio that was recorded from an **older draft** of the text and no longer matches (words in the narration are not in the current text). Must be regenerated.
- **3 stories** are linked to an audio file that **does not exist** on disk. Must be generated.
- **20 stories** have **no audio** at all. Must be generated.
- **Total needing generation: 40 of 50** — about **107,372 characters ≈ 214,744 credits** at the premium 2× rate.
- **Blocker:** `api.elevenlabs.io` is not in this environment's network egress allowlist (every request returns 403), so no audio can be generated until it is added.

## Every story

`Match%` is how much of the narration matches the current text. 100% + ALIGNED = perfect sync.

| # | Story | Era | Audio status | Match% | Text words | Audio words | Action |
|---|-------|-----|--------------|-------:|----------:|-----------:|--------|
| 01 | In the Beginning | In the Beginning | ✅ aligned | 100% | 591 | 591 | keep |
| 02 | The First Bad Choice | In the Beginning | ✅ aligned | 100% | 447 | 447 | keep |
| 03 | Two Brothers | In the Beginning | ✅ aligned | 100% | 377 | 377 | keep |
| 04 | The Ark and the Rainbow | The Age of the Patriarchs | ✅ aligned | 100% | 530 | 530 | keep |
| 05 | The Tower of Babel | The Age of the Patriarchs | ✅ aligned | 100% | 406 | 406 | keep |
| 06 | A Promise as Big as the Stars | The Age of the Patriarchs | ✅ aligned | 100% | 634 | 634 | keep |
| 07 | The Dreamer's Long Road | The Age of the Patriarchs | ✅ aligned | 100% | 661 | 661 | keep |
| 08 | The Baby in the River | The Exodus and Wilderness | ✅ aligned | 100% | 515 | 515 | keep |
| 09 | The Burning Bush | The Exodus and Wilderness | ✅ aligned | 100% | 574 | 574 | keep |
| 10 | Through the Sea on Dry Ground | The Exodus and Wilderness | ✅ aligned | 100% | 559 | 559 | keep |
| 11 | The Ten Commandments | The Exodus and Wilderness | ⚠️ stale | 70% | 536 | 546 | generate |
| 12 | Water From the Rock | The Exodus and Wilderness | — none | — | — | — | generate |
| 13 | The Scarlet Thread | The Promised Land | ⚠️ stale | 100% | 515 | 517 | generate |
| 14 | The Walls Come Down | The Promised Land | — none | — | — | — | generate |
| 15 | Three Hundred Men and Torches | The Promised Land | ⚠️ stale | 86% | 504 | 533 | generate |
| 16 | Wherever You Go | The Promised Land | ⚠️ stale | 94% | 566 | 566 | generate |
| 17 | Speak, Lord | The Kingdom Era | ⚠️ stale | 85% | 465 | 549 | generate |
| 18 | One Stone | The Kingdom Era | ⚠️ stale | 42% | 538 | 476 | generate |
| 19 | The Cave and the King | The Kingdom Era | — none | — | — | — | generate |
| 20 | The Lord Is My Shepherd | The Kingdom Era | ⚠️ stale | 27% | 483 | 507 | generate |
| 21 | The Wisest Request | The Kingdom Era | — none | — | — | — | generate |
| 22 | Fire from Heaven | The Kingdom Era | ⚠️ stale | 33% | 557 | 489 | generate |
| 23 | The Man Who Lost Everything | The Kingdom Era | — none | — | — | — | generate |
| 24 | The Servant Who Suffers | The Kingdom Era | — none | — | — | — | generate |
| 25 | The Furnace | Exile and Return | — none | — | — | — | generate |
| 26 | The Lion's Den | Exile and Return | ⚠️ stale | 40% | 590 | 452 | generate |
| 27 | For Such a Time as This | Exile and Return | ⚠️ stale | 47% | 540 | 450 | generate |
| 28 | The Man Who Ran From God | Exile and Return | — none | — | — | — | generate |
| 29 | The Wall Goes Up | Exile and Return | — none | — | — | — | generate |
| 30 | Impossible News | The Life of Jesus | ⚠️ stale | 20% | 531 | 1044 | generate |
| 31 | Left Behind in Jerusalem | The Life of Jesus | ⚠️ stale | 23% | 459 | 900 | generate |
| 32 | The Upside-Down Kingdom | The Life of Jesus | ⚠️ stale | 23% | 636 | 1140 | generate |
| 33 | The Woman at the Well | The Life of Jesus | — none | — | — | — | generate |
| 34 | Five Loaves and Two Fish | The Life of Jesus | — none | — | — | — | generate |
| 35 | Stepping Out | The Life of Jesus | — none | — | — | — | generate |
| 36 | The One Who Stopped | The Life of Jesus | — none | — | — | — | generate |
| 37 | The Man in the Tree | The Life of Jesus | — none | — | — | — | generate |
| 38 | The King Rides In | The Life of Jesus | — none | — | — | — | generate |
| 39 | The Man Who Walked Away | The Life of Jesus | — none | — | — | — | generate |
| 40 | The Boy Who Came Home | The Life of Jesus | ⚠️ stale | 39% | 609 | 1067 | generate |
| 41 | Come Out | The Life of Jesus | ⚠️ stale | 41% | 576 | 480 | generate |
| 42 | The Night Before | Death, Resurrection and the Early Church | — none | — | — | — | generate |
| 43 | The Darkest Friday | Death, Resurrection and the Early Church | ❌ broken link | — | — | — | generate |
| 44 | The Empty Tomb | Death, Resurrection and the Early Church | ❌ broken link | — | — | — | generate |
| 45 | The Stranger on the Road | Death, Resurrection and the Early Church | — none | — | — | — | generate |
| 46 | The Day Everything Changed | Death, Resurrection and the Early Church | ⚠️ stale | 39% | 511 | 441 | generate |
| 47 | The First Martyr | Death, Resurrection and the Early Church | — none | — | — | — | generate |
| 48 | The Man Who Hunted Christians | Death, Resurrection and the Early Church | ⚠️ stale | 52% | 613 | 487 | generate |
| 49 | Singing at Midnight | Death, Resurrection and the Early Church | ❌ broken link | — | — | — | generate |
| 50 | The Purple Merchant | Death, Resurrection and the Early Church | — none | — | — | — | generate |

## Stories to generate (40)

| # | id | chars | ~credits (2×) | why |
|---|----|------:|-------------:|-----|
| 11 | ten-commandments | 2,920 | 5,840 | audio is from an older draft |
| 12 | moses-water | 1,930 | 3,860 | never generated |
| 13 | rahab | 2,742 | 5,484 | audio is from an older draft |
| 14 | jericho | 2,198 | 4,396 | never generated |
| 15 | gideon | 2,871 | 5,742 | audio is from an older draft |
| 16 | ruth | 3,006 | 6,012 | audio is from an older draft |
| 17 | samuel | 2,389 | 4,778 | audio is from an older draft |
| 18 | david-goliath | 2,827 | 5,654 | audio is from an older draft |
| 19 | david-saul | 2,298 | 4,596 | never generated |
| 20 | psalm23 | 2,630 | 5,260 | audio is from an older draft |
| 21 | solomon-wisdom | 2,660 | 5,320 | never generated |
| 22 | elijah | 2,950 | 5,900 | audio is from an older draft |
| 23 | job | 2,689 | 5,378 | never generated |
| 24 | isaiah-servant | 2,616 | 5,232 | never generated |
| 25 | shadrach | 2,384 | 4,768 | never generated |
| 26 | daniel | 3,303 | 6,606 | audio is from an older draft |
| 27 | esther | 2,976 | 5,952 | audio is from an older draft |
| 28 | jonah | 2,849 | 5,698 | never generated |
| 29 | nehemiah | 2,425 | 4,850 | never generated |
| 30 | annunciation | 2,769 | 5,538 | audio is from an older draft |
| 31 | boy-temple | 2,604 | 5,208 | audio is from an older draft |
| 32 | sermon-mount | 3,415 | 6,830 | audio is from an older draft |
| 33 | woman-at-well | 2,851 | 5,702 | never generated |
| 34 | feeding-5000 | 2,372 | 4,744 | never generated |
| 35 | walk-on-water | 2,049 | 4,098 | never generated |
| 36 | good-samaritan | 2,079 | 4,158 | never generated |
| 37 | zacchaeus | 2,138 | 4,276 | never generated |
| 38 | triumphal-entry | 2,539 | 5,078 | never generated |
| 39 | rich-young-ruler | 1,990 | 3,980 | never generated |
| 40 | prodigal | 3,143 | 6,286 | audio is from an older draft |
| 41 | lazarus | 2,966 | 5,932 | audio is from an older draft |
| 42 | last-supper | 2,384 | 4,768 | never generated |
| 43 | crucifixion | 3,288 | 6,576 | linked file missing |
| 44 | resurrection | 3,654 | 7,308 | linked file missing |
| 45 | road-emmaus | 2,755 | 5,510 | never generated |
| 46 | pentecost | 2,835 | 5,670 | audio is from an older draft |
| 47 | stephen | 2,321 | 4,642 | never generated |
| 48 | paul-conversion | 3,400 | 6,800 | audio is from an older draft |
| 49 | paul-jail | 2,827 | 5,654 | linked file missing |
| 50 | lydia | 2,330 | 4,660 | never generated |

**Total: 40 stories · 107,372 characters · ~214,744 credits**

## How this was verified

The check mirrors the real highlighting code in `index.html`: the audio's character-level
timestamps are tokenized exactly like `buildWordTimings()` and the on-screen text exactly like
`wrapStoryWords()`. The app highlights word *i* of the text when spoken word *i* plays, so the
two streams must match 1:1. `verify_audio.py` reproduces this; `generate_audio.py` runs it after
every generation and refuses to link audio that would mis-highlight.

