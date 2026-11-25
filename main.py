#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off — one joke about office life.

The entry is a single fixed joke, written for make.fun
u-suzy-one-line-office-joke-laugh-off-f574ac73: one original one-line
joke about office life, at most 200 characters. This program writes
that joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
outside the grader's container):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. The joke is fixed text: the same
bytes on every run, no network.
"""

import os
import sys
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = (
    "The office plant has outlasted three managers, two "
    "restructures, and one fire drill — it's the only one here with "
    "job security."
)


def abort(message):
    """Stop with the reason on stderr and a non-zero exit."""
    print(f"main.py: {message}", file=sys.stderr)
    return 1


def deliver():
    """Validate the joke against the gate, then write it out."""
    if not 1 <= len(LINE) <= 200:
        return abort(f"joke is {len(LINE)} characters, the gate allows 1-200")
    if not LINE.strip():
        return abort("joke is only white space, the gate refuses it")
    target = Path(OUTPUT_DIR) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {target}: {len(LINE)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver())
