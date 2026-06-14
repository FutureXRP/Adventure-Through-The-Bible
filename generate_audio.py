#!/usr/bin/env python3
"""
generate_audio.py — Generate ElevenLabs narration + word timestamps for Tier 1
stories and guarantee the audio stays in perfect sync with the on-screen text.

What it does for each story:
  1. Reads the canonical text from stories.json  (' '.join of the story paragraphs,
     exactly how index.html concatenates them for highlighting).
  2. Calls the ElevenLabs with-timestamps endpoint (same premium voice + model
     used for stories 1-10, so the whole tier sounds identical).
  3. Saves audio/<id>.mp3 and audio/<id>.json.
  4. Immediately verifies, with the SAME tokenization the app uses, that every
     spoken word lines up 1:1 with a highlightable word on screen.
       * On PASS  -> sets "audio": "./audio/<id>.mp3" in stories.json.
       * On FAIL  -> leaves the audio field unset and prints the divergence,
                     so a broken/stale file is never wired into the app.

Usage:
  python3 generate_audio.py <story-id>          generate one story
  python3 generate_audio.py --list              show every story's audio status
  python3 generate_audio.py --all-missing       plan: every story needing audio
  python3 generate_audio.py --all-missing --yes generate them all (uses credits!)
  python3 generate_audio.py <id-a> <id-b> --yes generate a specific set

The API key is read from the ELEVENLABS_API_KEY environment variable. (A key was
previously hard-coded here and committed to a public repo — rotate it and export
the new one instead:  export ELEVENLABS_API_KEY=sk_...)
"""

import base64
import json
import os
import sys
import urllib.request
import urllib.error

# Reuse the EXACT tokenization the app and the verifier use, so "generated" and
# "verified clean" mean the same thing everywhere.
from verify_audio import display_tokens, audio_tokens, clean_word

STORIES_FILE = 'stories.json'
AUDIO_DIR = 'audio'
VOICE_ID = "1wg2wOjdEWKA7yQD8Kca"          # same premium voice as stories 1-10
MODEL_ID = "eleven_multilingual_v2"         # same model as stories 1-10
VOICE_SETTINGS = {"stability": 0.5, "similarity_boost": 0.75, "style": 0.0, "use_speaker_boost": True}
PREMIUM_MULTIPLIER = 2                       # premium voice bills at 2x characters

API_BASE = "https://api.elevenlabs.io/v1/text-to-speech"


def load_data():
    with open(STORIES_FILE, encoding='utf-8') as f:
        return json.load(f)


def find_story(data, story_id):
    return next((s for s in data['stories'] if s['id'] == story_id), None)


def story_text(story):
    """Exactly what index.html narrates and concatenates for highlighting."""
    return ' '.join(story['story'])


def check_alignment(story, alignment):
    """Return (ok, message) using the app's real tokenization."""
    disp = display_tokens(story)
    audio = audio_tokens(alignment)
    div = None
    for i in range(min(len(disp), len(audio))):
        if clean_word(disp[i]) != clean_word(audio[i]):
            div = i
            break
    if len(disp) == len(audio) and div is None:
        return True, f"{len(disp)} words line up 1:1"
    if div is not None:
        a = max(0, div - 3)
        return False, (f"display={len(disp)} audio={len(audio)}; first divergence at word #{div + 1}\n"
                       f"      highlighted: ...{' '.join(disp[a:div + 2])}...\n"
                       f"      spoken     : ...{' '.join(audio[a:div + 2])}...")
    return False, f"display={len(disp)} audio={len(audio)}; counts differ at the tail"


def set_audio_field(story_id, audio_path):
    """Byte-safely set/insert the audio field (insert after 'connections' for a clean diff)."""
    data = load_data()
    stories = data['stories']
    idx = next(i for i, s in enumerate(stories) if s['id'] == story_id)
    s = stories[idx]
    if 'audio' in s:
        s['audio'] = audio_path
    else:
        rebuilt = {}
        for k, v in s.items():
            rebuilt[k] = v
            if k == 'connections':
                rebuilt['audio'] = audio_path
        if 'audio' not in rebuilt:
            rebuilt['audio'] = audio_path
        stories[idx] = rebuilt
    with open(STORIES_FILE, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=2))  # no trailing newline -> byte-stable


def generate(story_id, api_key):
    data = load_data()
    story = find_story(data, story_id)
    if not story:
        print(f"  Story '{story_id}' not found in {STORIES_FILE}")
        return False

    text = story_text(story)
    print(f"  Generating '{story['title']}' ({len(text):,} chars, ~{len(text) * PREMIUM_MULTIPLIER:,} credits)...")

    payload = json.dumps({"text": text, "model_id": MODEL_ID, "voice_settings": VOICE_SETTINGS}).encode('utf-8')
    req = urllib.request.Request(
        f"{API_BASE}/{VOICE_ID}/with-timestamps",
        data=payload,
        headers={"xi-api-key": api_key, "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            result = json.load(resp)
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors='replace')
        print(f"  ERROR {e.code}: {body[:300]}")
        if 'allowlist' in body:
            print("  -> Add api.elevenlabs.io to your environment's network egress allowlist.")
        return False
    except Exception as e:
        print(f"  ERROR contacting ElevenLabs: {type(e).__name__}: {e}")
        return False

    alignment = result['alignment']
    os.makedirs(AUDIO_DIR, exist_ok=True)
    mp3_path = os.path.join(AUDIO_DIR, f"{story_id}.mp3")
    json_path = os.path.join(AUDIO_DIR, f"{story_id}.json")
    with open(mp3_path, 'wb') as f:
        f.write(base64.b64decode(result['audio_base64']))
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(alignment, f, indent=2)

    ok, msg = check_alignment(story, alignment)
    if ok:
        set_audio_field(story_id, f"./{AUDIO_DIR}/{story_id}.mp3")
        print(f"  PASS  {msg}  ->  saved + linked in stories.json")
        return True
    print(f"  FAIL  audio saved but NOT linked (would mis-highlight):\n      {msg}")
    return False


def audio_status(story):
    sid = story['id']
    have_files = os.path.exists(os.path.join(AUDIO_DIR, f"{sid}.mp3")) and \
        os.path.exists(os.path.join(AUDIO_DIR, f"{sid}.json"))
    linked = bool(story.get('audio'))
    if have_files and linked:
        from verify_audio import verify_story
        st, _ = verify_story(story)
        return 'OK (aligned)' if st == 'match' else 'STALE (misaligned)'
    if have_files and not linked:
        return 'files present, not linked'
    if linked and not have_files:
        return 'BROKEN (linked, file missing)'
    return 'needs audio'


def stories_needing_audio(data):
    out = []
    for s in sorted(data['stories'], key=lambda s: s.get('order', 0)):
        st = audio_status(s)
        if st != 'OK (aligned)':
            out.append(s['id'])
    return out


def cmd_list(data):
    total = 0
    for s in sorted(data['stories'], key=lambda s: s.get('order', 0)):
        st = audio_status(s)
        chars = len(story_text(s))
        if st != 'OK (aligned)':
            total += chars
        print(f"  {s.get('order', 0):02d}. {s['id']:<18} {st:<32} ({chars:,} chars)")
    print(f"\n  Characters to (re)generate: {total:,}  ->  ~{total * PREMIUM_MULTIPLIER:,} credits at premium 2x")


def main():
    args = sys.argv[1:]
    confirm = '--yes' in args
    ids = [a for a in args if not a.startswith('--')]
    data = load_data()

    if '--list' in args:
        cmd_list(data)
        return

    if '--all-missing' in args:
        ids = stories_needing_audio(data)

    if not ids:
        print(__doc__)
        return

    total_chars = sum(len(story_text(find_story(data, i))) for i in ids if find_story(data, i))
    print(f"Stories to generate ({len(ids)}): {', '.join(ids)}")
    print(f"Estimated cost: {total_chars:,} chars  ->  ~{total_chars * PREMIUM_MULTIPLIER:,} credits at premium 2x\n")

    if not confirm:
        print("This will spend ElevenLabs credits. Re-run with --yes to proceed.")
        return

    api_key = os.environ.get('ELEVENLABS_API_KEY')
    if not api_key:
        print("ELEVENLABS_API_KEY is not set. Export it first:  export ELEVENLABS_API_KEY=sk_...")
        sys.exit(2)

    done = failed = 0
    for sid in ids:
        if generate(sid, api_key):
            done += 1
        else:
            failed += 1
    print(f"\nGenerated {done} story(ies); {failed} failed/needs attention.")
    print("Run  python3 verify_audio.py  to confirm the whole tier is in sync.")


if __name__ == '__main__':
    main()
