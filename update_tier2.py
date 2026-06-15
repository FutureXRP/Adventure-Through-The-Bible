#!/usr/bin/env python3
"""
update_tier2.py — apply enriched Tier-2 story text to stories-tier2.json in
place, replacing only the "story" array for the given ids. Validates that the
new text stays audio-alignment-safe (no em-dashes, no stray punctuation tokens,
no double spaces) so it can be narrated later without rework.

Used by the enrich_*.py scripts:  import update_tier2; update_tier2.apply({...})
"""
import json
import re
import sys

FILE = "stories-tier2.json"


def clean_word(w):
    return re.sub(r"[^a-z0-9']", "", w.lower())


def check(paras):
    probs = []
    for i, p in enumerate(paras):
        if not isinstance(p, str) or not p.strip():
            probs.append(f"p{i} empty"); continue
        if "—" in p: probs.append(f"p{i} em-dash")
        if "\n" in p: probs.append(f"p{i} newline")
        if "  " in p: probs.append(f"p{i} double-space")
        if p != p.strip(): probs.append(f"p{i} edge-space")
        for t in p.split():
            if clean_word(t) == "":
                probs.append(f"p{i} stray {t!r}")
    return probs


def apply(updates, target=1462):
    d = json.load(open(FILE, encoding="utf-8"))
    idx = {s["id"]: s for s in d["stories"]}
    errs = 0
    for sid, paras in updates.items():
        if sid not in idx:
            print(f"  ! {sid} not found"); errs += 1; continue
        pr = check(paras)
        if pr:
            print(f"  ✗ {sid}: {pr}"); errs += 1; continue
        c = len(" ".join(paras))
        idx[sid]["story"] = paras
        flag = "" if c >= target else f"  (still {c}, under {target})"
        print(f"  ✓ {sid}: {c}ch{flag}")
    if errs:
        print(f"{errs} error(s) — NOT writing."); sys.exit(1)
    with open(FILE, "w", encoding="utf-8") as f:
        f.write(json.dumps(d, ensure_ascii=False, indent=2))
    print(f"Updated {len(updates)} stories in {FILE}.")


def expand(additions, target=1462):
    """Insert extra paragraph(s) just before each story's final paragraph."""
    d = json.load(open(FILE, encoding="utf-8"))
    idx = {s["id"]: s for s in d["stories"]}
    errs = 0
    for sid, extra in additions.items():
        if sid not in idx:
            print(f"  ! {sid} not found"); errs += 1; continue
        pr = check(extra)
        if pr:
            print(f"  ✗ {sid}: {pr}"); errs += 1; continue
        story = idx[sid]["story"]
        idx[sid]["story"] = story[:-1] + list(extra) + story[-1:]
        c = len(" ".join(idx[sid]["story"]))
        flag = "" if c >= target else f"  (still {c}, under {target})"
        print(f"  ✓ {sid}: {c}ch{flag}")
    if errs:
        print(f"{errs} error(s) — NOT writing."); sys.exit(1)
    with open(FILE, "w", encoding="utf-8") as f:
        f.write(json.dumps(d, ensure_ascii=False, indent=2))
    print(f"Expanded {len(additions)} stories in {FILE}.")
