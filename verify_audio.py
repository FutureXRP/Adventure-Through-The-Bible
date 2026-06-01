#!/usr/bin/env python3
"""
verify_audio.py — Compares stories.json text against ElevenLabs timestamp JSON
to detect any word mismatches between the written story and the generated audio.

Usage:
  python3 verify_audio.py              # checks all stories with audio
  python3 verify_audio.py creation     # checks one story
"""

import json
import sys
import os
import re

def clean_word(w):
    """Strip punctuation for comparison, lowercase."""
    return re.sub(r"[^a-zA-Z0-9']", '', w).lower()

def get_story_words(story):
    """Extract all words from story paragraphs."""
    text = ' '.join(story['story'])
    # Split on whitespace and dashes, keep words
    tokens = re.split(r'[\s\u2014\u2013]+', text)
    return [w for w in tokens if clean_word(w)]

def get_audio_words(alignment):
    """Reconstruct words from ElevenLabs character-level timestamp data."""
    chars = alignment['characters']
    words = []
    current = ''
    for c in chars:
        if c in (' ', '\n', '\u2014', '\u2013'):
            if current:
                words.append(current)
                current = ''
        else:
            current += c
    if current:
        words.append(current)
    return [w for w in words if clean_word(w)]

def compare(story_words, audio_words, story_id):
    issues = []
    sw = [clean_word(w) for w in story_words]
    aw = [clean_word(w) for w in audio_words]

    if len(sw) != len(aw):
        issues.append(f"  ⚠️  Word count mismatch: story={len(sw)} audio={len(aw)}")

    # Find first divergence
    mismatches = 0
    for i, (s, a) in enumerate(zip(sw, aw)):
        if s != a:
            mismatches += 1
            context_s = ' '.join(story_words[max(0,i-2):i+3])
            context_a = ' '.join(audio_words[max(0,i-2):i+3])
            issues.append(f"  ✗  Word {i+1}: story='{s}' audio='{a}'")
            issues.append(f"       story context: '...{context_s}...'")
            issues.append(f"       audio context: '...{context_a}...'")
            if mismatches >= 3:
                issues.append(f"  ... (stopping after 3 mismatches)")
                break

    return issues

def verify_story(story, audio_dir='audio'):
    story_id = story['id']
    json_path = os.path.join(audio_dir, f"{story_id}.json")

    if not os.path.exists(json_path):
        return None, f"  — No timestamp file found at {json_path}"

    with open(json_path) as f:
        alignment = json.load(f)

    story_words = get_story_words(story)
    audio_words = get_audio_words(alignment)
    issues = compare(story_words, audio_words, story_id)

    return len(story_words), issues

def main():
    with open('stories.json') as f:
        data = json.load(f)

    stories = sorted(data['stories'], key=lambda s: s['order'])

    # Filter to specific story if argument given
    target = sys.argv[1] if len(sys.argv) > 1 else None
    if target:
        stories = [s for s in stories if s['id'] == target]
        if not stories:
            print(f"Story '{target}' not found")
            sys.exit(1)

    print("FOOTSTEPS AUDIO VERIFICATION")
    print("=" * 60)

    all_clean = True
    for story in stories:
        word_count, issues = verify_story(story)

        if word_count is None:
            # No audio file yet — skip silently unless it was specifically requested
            if target:
                print(f"\n{story['order']:02d}. {story['title']}")
                print(issues)
            continue

        if not issues:
            print(f"✅ {story['order']:02d}. {story['title']:<42} ({word_count} words) — MATCH")
        else:
            all_clean = False
            print(f"\n❌ {story['order']:02d}. {story['title']}")
            for issue in issues:
                print(issue)

    print("\n" + "=" * 60)
    if all_clean:
        print("✅ All stories with audio match perfectly")
    else:
        print("⚠️  Some stories have mismatches — fix the JSON text to match the audio")
        print("   Rule: audio is the source of truth. Edit JSON to match audio, not vice versa.")

if __name__ == '__main__':
    main()
