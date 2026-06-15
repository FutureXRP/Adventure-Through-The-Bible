#!/usr/bin/env python3
"""
build_stories.py — merge authored story batches into stories.json (Tier 1) and
stories-tier2.json (Tier 2), keep the global `order` canonical across both
tiers, and validate every new story for schema-correctness AND audio-alignment
safety BEFORE a single ElevenLabs credit is spent.

An "authored batch" is a JSON list. Each item carries the shared metadata once
plus a `tier1` and `tier2` block:

  {
    "id": "jacob-ladder", "era": "patriarchs",
    "emoji": "🪜", "title": "...", "date": "...", "location": "...",
    "connections": [{"title","storyId","reference","why"}, ...],
    "tier1": {"book","hook","story":[...],"devotional":{"bigIdea","questions":[3]},"tags":[...],"quiz":[5]},
    "tier2": {"book","hook","story":[...],"devotional":{"bigIdea","questions":[3]},
              "devotionalHeading":"Let's Talk About It","tags":[...],"quiz":[3]}
  }

Usage:
  python3 build_stories.py --validate batch.json   # dry-run: checks only, no writes
  python3 build_stories.py --merge    batch.json   # validate, then write both files + renumber
  python3 build_stories.py --renumber              # just re-apply canonical order to both files
"""

import json
import re
import sys

# Audio is keyed by `id`, never by `order`, so renumbering is always safe for audio.
CANONICAL_ORDER = [
    # creation
    "creation", "adam-eve", "cain-abel",
    # patriarchs
    "noah", "tower-babel", "abraham", "jacob-esau", "jacob-ladder", "jacob-wrestles", "joseph",
    # exodus
    "moses-birth", "burning-bush", "plagues", "passover", "red-sea", "manna",
    "ten-commandments", "golden-calf", "moses-water", "spies", "bronze-serpent", "balaam",
    # promised-land
    "jordan", "rahab", "jericho", "deborah", "gideon", "samson", "ruth",
    # kingdom
    "hannah", "samuel", "saul-king", "david-anointed", "david-goliath", "david-jonathan",
    "david-saul", "david-ark", "mephibosheth", "david-bathsheba", "psalm23", "solomon-wisdom",
    "solomon-temple", "elijah", "naboth", "naaman", "axe-head", "widows-oil", "shunammite",
    "job", "isaiah-servant",
    # exile
    "daniel-food", "shadrach", "daniel", "esther", "jonah", "nehemiah",
    # nt-life
    "annunciation", "wise-men", "boy-temple", "baptism", "temptation", "call-disciples",
    "cana", "sermon-mount", "sower", "mustard-seed", "woman-at-well", "paralytic",
    "calm-storm", "feeding-5000", "walk-on-water", "bartimaeus", "jairus", "ten-lepers",
    "good-samaritan", "lost-sheep", "lost-coin", "blesses-children", "zacchaeus", "mary-martha",
    "rich-young-ruler", "prodigal", "lazarus", "triumphal-entry",
    # nt-church
    "last-supper", "crucifixion", "resurrection", "road-emmaus", "pentecost", "peter-beggar",
    "stephen", "philip-ethiopian", "paul-conversion", "cornelius", "peter-escapes", "paul-jail",
    "lydia", "athens", "eutychus", "shipwreck",
]
RANK = {sid: i for i, sid in enumerate(CANONICAL_ORDER)}

COMMON = {"access": "premium", "published_date": "2026-06-03"}
VALID_ERAS = {"creation", "patriarchs", "exodus", "promised-land", "kingdom", "exile", "nt-life", "nt-church"}

T1 = "stories.json"
T2 = "stories-tier2.json"


def clean_word(w):
    return re.sub(r"[^a-z0-9']", "", w.lower())


def alignment_problems(paragraphs):
    """Mirror verify_audio: flag anything that would break first-try word alignment."""
    problems = []
    for i, para in enumerate(paragraphs):
        if not isinstance(para, str) or para.strip() == "":
            problems.append(f"para {i}: empty/not a string")
            continue
        if "—" in para:
            problems.append(f"para {i}: contains em-dash (—) — use a comma or hyphen")
        if "\n" in para:
            problems.append(f"para {i}: contains a newline")
        if para != para.strip():
            problems.append(f"para {i}: leading/trailing whitespace")
        if "  " in para:
            problems.append(f"para {i}: double space")
        for tok in para.split():
            if clean_word(tok) == "":
                problems.append(f"para {i}: stray punctuation token {tok!r} (highlights to nothing)")
    return problems


def validate(item):
    errs = []
    sid = item.get("id", "<no id>")
    if sid not in RANK:
        errs.append(f"id {sid!r} not in CANONICAL_ORDER")
    if item.get("era") not in VALID_ERAS:
        errs.append(f"era {item.get('era')!r} invalid")
    for k in ("emoji", "title", "date", "location"):
        if not item.get(k):
            errs.append(f"missing shared field {k!r}")
    for c in item.get("connections", []):
        if c.get("storyId") not in RANK:
            errs.append(f"connection storyId {c.get('storyId')!r} is unknown")
        for k in ("title", "reference", "why"):
            if not c.get(k):
                errs.append(f"connection missing {k!r}")
    for tier, want_quiz in (("tier1", 5), ("tier2", 3)):
        t = item.get(tier)
        if not t:
            errs.append(f"missing {tier} block")
            continue
        if not t.get("book"):
            errs.append(f"{tier}: missing book")
        if not t.get("hook"):
            errs.append(f"{tier}: missing hook")
        story = t.get("story") or []
        if len(story) < 4:
            errs.append(f"{tier}: only {len(story)} paragraphs")
        errs += [f"{tier}: {p}" for p in alignment_problems(story)]
        dev = t.get("devotional") or {}
        if not dev.get("bigIdea"):
            errs.append(f"{tier}: devotional.bigIdea missing")
        if len(dev.get("questions", [])) != 3:
            errs.append(f"{tier}: devotional needs 3 questions, has {len(dev.get('questions', []))}")
        if tier == "tier2" and t.get("devotionalHeading") != "Let's Talk About It":
            errs.append("tier2: devotionalHeading should be \"Let's Talk About It\"")
        quiz = t.get("quiz") or []
        if len(quiz) != want_quiz:
            errs.append(f"{tier}: quiz should have {want_quiz} questions, has {len(quiz)}")
        for j, q in enumerate(quiz):
            opts = q.get("options", [])
            if not (2 <= len(opts) <= 4):
                errs.append(f"{tier} quiz {j}: needs 2-4 options")
            if not isinstance(q.get("answer"), int) or not (0 <= q.get("answer", -1) < len(opts)):
                errs.append(f"{tier} quiz {j}: answer index out of range")
            if "explanation" not in q:
                errs.append(f"{tier} quiz {j}: missing explanation (use \"\" if none)")
            if not q.get("question"):
                errs.append(f"{tier} quiz {j}: missing question")
    return errs


def build_tier(item, tier):
    t = item[tier]
    obj = {
        "id": item["id"], "era": item["era"], "order": 0, "access": COMMON["access"],
        "emoji": item["emoji"], "title": item["title"], "book": t["book"], "date": item["date"],
        "location": item["location"], "hook": t["hook"], "story": t["story"],
        "devotional": t["devotional"],
    }
    if tier == "tier2":
        obj["devotionalHeading"] = t.get("devotionalHeading", "Let's Talk About It")
    obj["tags"] = t["tags"]
    obj["connections"] = item["connections"]
    obj["quiz"] = t["quiz"]
    obj["published_date"] = COMMON["published_date"]
    return obj


def renumber(data):
    data["stories"].sort(key=lambda s: RANK.get(s["id"], 9999))
    for i, s in enumerate(data["stories"], 1):
        s["order"] = i
    data["meta"]["totalStories"] = len(data["stories"])
    return data


def write(path, data):
    with open(path, "w", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=2))  # no trailing newline -> byte-stable


def main():
    args = sys.argv[1:]
    if "--renumber" in args:
        for path in (T1, T2):
            data = json.load(open(path, encoding="utf-8"))
            write(path, renumber(data))
            print(f"renumbered {path}: {len(data['stories'])} stories")
        return

    mode = "--merge" if "--merge" in args else "--validate"
    batch_path = next((a for a in args if not a.startswith("--")), None)
    if not batch_path:
        print(__doc__)
        return
    batch = json.load(open(batch_path, encoding="utf-8"))

    t1 = json.load(open(T1, encoding="utf-8"))
    t2 = json.load(open(T2, encoding="utf-8"))
    have = {s["id"] for s in t1["stories"]}

    total_errs, t1_chars = 0, 0
    for item in batch:
        errs = validate(item)
        if item.get("id") in have:
            errs.append(f"id {item.get('id')!r} already present")
        if errs:
            total_errs += len(errs)
            print(f"\n✗ {item.get('id')} ({item.get('title','?')})")
            for e in errs:
                print(f"    - {e}")
        else:
            chars = len(" ".join(item["tier1"]["story"]))
            t1_chars += chars
            print(f"✓ {item['id']:<16} T1 {chars:,}ch / T2 {len(' '.join(item['tier2']['story'])):,}ch")

    print(f"\n{len(batch)} stories, {total_errs} problem(s).")
    print(f"Tier-1 audio cost if merged+generated: ~{t1_chars*2:,} credits (premium 2x).")
    if total_errs:
        print("Fix problems before merging."); sys.exit(1)
    if mode != "--merge":
        print("Dry run OK. Re-run with --merge to write."); return

    for item in batch:
        t1["stories"].append(build_tier(item, "tier1"))
        t2["stories"].append(build_tier(item, "tier2"))
    write(T1, renumber(t1))
    write(T2, renumber(t2))
    print(f"\nMerged. Now {len(t1['stories'])} stories in both tiers (renumbered 1..{len(t1['stories'])}).")
    print("Tier-1 audio:  python3 generate_audio.py " + " ".join(i["id"] for i in batch) + " --yes")


if __name__ == "__main__":
    main()
