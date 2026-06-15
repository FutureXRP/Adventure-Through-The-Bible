#!/usr/bin/env python3
"""
verify_audio.py — Verify that every word the narrator speaks is the exact word
the app will highlight, for each story that has audio.

This mirrors the REAL highlighting logic in index.html so a PASS here means the
on-screen word highlighting will track the narration perfectly:

  * AUDIO side  — buildWordTimings(): walks the ElevenLabs character stream and
                  splits words on space, newline and em dash ("—"). The em
                  dash is a separator that produces NO word of its own.
  * DISPLAY side — wrapStoryWords(): renders each paragraph and splits its text
                  on whitespace only, turning every non-space run into one
                  highlightable <span>. (A lone "—" therefore becomes its
                  own span — which is exactly what used to break the sync.)

The app highlights allWordSpans[i] for audio word i, so the two token streams
must line up 1:1. We compare them index-by-index (punctuation/case ignored,
since the app highlights by position, not by text).

Usage:
  python3 verify_audio.py            # check every story that has audio
  python3 verify_audio.py creation   # check one story
  python3 verify_audio.py --strict   # also fail on audio-field/file problems
Exit code is non-zero if any checked story is misaligned.
"""

import json
import sys
import os
import re

AUDIO_DIR = 'audio'
STORIES_FILE = 'stories.json'
SUFFIX = ''                         # '-t2' for Tier 2 audio files
WORD_SEPARATORS = (' ', '\n', '—')  # exactly what buildWordTimings() splits on


def clean_word(w):
    """Lowercase and strip everything but letters/digits/apostrophe (matches by position, not punctuation)."""
    return re.sub(r"[^a-z0-9']", '', w.lower())


def display_tokens(story):
    """Mirror wrapStoryWords(): per paragraph, split textContent on whitespace, keep non-space runs."""
    tokens = []
    for para in story['story']:
        for tok in re.split(r'(\s+)', para):
            if tok.strip() != '':
                tokens.append(tok)
    return tokens


def audio_tokens(alignment):
    """Mirror buildWordTimings(): walk characters, break on space/newline/em-dash, em-dash yields no word."""
    chars = alignment['characters']
    words, cur = [], ''
    for c in chars:
        if c in WORD_SEPARATORS:
            if cur:
                words.append(cur)
                cur = ''
        else:
            cur += c
    if cur:
        words.append(cur)
    return words


def verify_story(story):
    """Return (status, message). status in {'match','mismatch','missing','unlinked'}."""
    sid = story['id']
    json_path = os.path.join(AUDIO_DIR, f"{sid}{SUFFIX}.json")
    mp3_path = os.path.join(AUDIO_DIR, f"{sid}{SUFFIX}.mp3")
    linked = bool(story.get('audio'))

    if not os.path.exists(json_path) or not os.path.exists(mp3_path):
        if linked:
            return 'missing', f"audio field is set to {story['audio']!r} but the file is missing on disk"
        return 'absent', "no audio yet"

    with open(json_path, encoding='utf-8') as f:
        alignment = json.load(f)

    disp = display_tokens(story)
    audio = audio_tokens(alignment)

    # First index where the highlighted word would differ from the spoken word.
    first_div = None
    for i in range(min(len(disp), len(audio))):
        if clean_word(disp[i]) != clean_word(audio[i]):
            first_div = i
            break

    if len(disp) == len(audio) and first_div is None:
        note = '' if linked else '  (NOTE: aligned, but "audio" field not set in stories.json — app will not play it)'
        return 'match', f"{len(disp)} words{note}"

    # Build a helpful divergence report.
    lines = [f"display words={len(disp)}  audio words={len(audio)}  (gap={len(disp) - len(audio):+d})"]
    if first_div is not None:
        a = max(0, first_div - 3)
        lines.append(f"    first divergence at word #{first_div + 1}:")
        lines.append(f"      highlighted: ...{' '.join(disp[a:first_div + 2])}...")
        lines.append(f"      spoken     : ...{' '.join(audio[a:first_div + 2])}...")
    else:
        n = min(len(disp), len(audio))
        lines.append(f"    streams agree for {n} words, then one runs longer:")
        lines.append(f"      extra highlighted tail: {disp[n:n + 4]}")
        lines.append(f"      extra spoken tail     : {audio[n:n + 4]}")
    return 'mismatch', '\n'.join(lines)


def main():
    global STORIES_FILE, SUFFIX
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    strict = '--strict' in sys.argv
    if '--tier2' in sys.argv:
        STORIES_FILE, SUFFIX = 'stories-tier2.json', '-t2'

    with open(STORIES_FILE, encoding='utf-8') as f:
        data = json.load(f)
    stories = sorted(data['stories'], key=lambda s: s.get('order', 0))

    if args:
        target = args[0]
        stories = [s for s in stories if s['id'] == target]
        if not stories:
            print(f"Story '{target}' not found")
            sys.exit(2)

    print("FOOTSTEPS AUDIO SYNC VERIFICATION")
    print("=" * 64)

    matched = mism = missing = absent = 0
    for s in stories:
        status, msg = verify_story(s)
        tag = f"{s.get('order', 0):02d}. {s['title']}"
        if status == 'match':
            matched += 1
            print(f"PASS  {tag:<44} {msg}")
        elif status == 'mismatch':
            mism += 1
            print(f"FAIL  {tag}")
            for line in msg.splitlines():
                print(f"      {line}")
        elif status == 'missing':
            missing += 1
            print(f"BROKEN {tag:<43} {msg}")
        else:  # absent
            absent += 1
            if args:  # only mention when a specific story was requested
                print(f"----  {tag:<44} {msg}")

    print("=" * 64)
    print(f"{matched} aligned   {mism} misaligned   {missing} linked-but-missing   {absent} no-audio")
    problems = mism + (missing if strict else 0)
    if mism:
        print("Some stories are misaligned. Regenerate their audio from the current text,")
        print("or fix the text so it matches the existing audio.")
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main()
