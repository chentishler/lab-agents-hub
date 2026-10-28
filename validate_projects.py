#!/usr/bin/env python3
"""Check the projects/ tree against docs/PROTOCOL.md. Exits 1 on problems.

Checks per project (a folder containing BRIEF.md):
  - message files match NNN-AUTHOR-TYPE.md, numbers start at 001 and have no gaps/duplicates
  - data files match YYYYMMDD_AUTHOR_description.csv
  - no message from git history was edited or deleted (when run with --base REF)
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TYPES = "proposal|reply|question|data|critique|final-proposal|agreed|objection|human-note|escalation"
MSG = re.compile(rf"^(\d{{3}})-[a-z0-9-]+-({TYPES})\.md$")
DATA = re.compile(r"^\d{8}_[a-z0-9-]+_[A-Za-z0-9._-]+\.csv$")


def check_tree() -> list[str]:
    errs = []
    for brief in sorted((ROOT / "projects").rglob("BRIEF.md")):
        proj = brief.parent
        rel = proj.relative_to(ROOT).as_posix()
        nums = []
        for f in sorted((proj / "messages").glob("*")) if (proj / "messages").is_dir() else []:
            m = MSG.match(f.name)
            if not m:
                errs.append(f"{rel}/messages/{f.name}: name must be NNN-AUTHOR-TYPE.md")
            else:
                nums.append(int(m.group(1)))
        if nums != list(range(1, len(nums) + 1)):
            errs.append(f"{rel}/messages: numbers must run 001.. with no gaps or duplicates, got {nums}")
        for f in sorted((proj / "data").glob("*")) if (proj / "data").is_dir() else []:
            if not DATA.match(f.name):
                errs.append(f"{rel}/data/{f.name}: name must be YYYYMMDD_AUTHOR_description.csv")
    return errs


def check_history(base: str) -> list[str]:
    out = subprocess.run(["git", "diff", "--name-status", "--no-renames", f"{base}...HEAD",
                          "--", "projects/*/messages/*", "projects/**/messages/*"],
                         cwd=ROOT, capture_output=True, text=True, check=True).stdout
    errs = []
    for line in out.splitlines():
        status, path = line.split("\t", 1)
        if status != "A" and "/messages/" in path:
            errs.append(f"{path}: existing message was {'deleted' if status == 'D' else 'modified'}; "
                        "write a new message instead")
    return errs


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", help="git ref to compare against (e.g. origin/main)")
    a = ap.parse_args()
    errs = check_tree() + (check_history(a.base) if a.base else [])
    print("\n".join(errs) if errs else "projects/ OK")
    sys.exit(1 if errs else 0)
