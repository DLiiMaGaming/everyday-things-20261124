#!/usr/bin/env python3
"""Everyday Things, Two Lines — make.fun entry.

Writes one two-line explanation to /output/entry.txt:
line 1 explains one everyday thing (a traffic jam) to a 10-year-old
in a single vivid sentence built on an analogy; line 2 says in one
sentence why that analogy works: what it maps and what it leaves out.

The entry text is a plain constant below. The program validates the
gate itself before writing: UTF-8 text, 1-400 characters, exactly
two non-empty lines.
"""

import os
import sys

# The entry: exactly two lines. Line 1 is the analogy, line 2 is the
# honest account of what the analogy maps and what it leaves out.
ENTRY = """A traffic jam is the school corridor when the bell rings and a hundred kids all try to leave through the same door at once, so everybody shuffles and nobody moves.
It maps the squeeze — too many people, one narrow way out, everyone in a hurry — but it leaves out that cars can't slip sideways between each other or turn around and walk back the way they came."""


def main() -> int:
    lines = ENTRY.split("\n")
    if len(lines) != 2:
        print(f"ERROR: entry must be exactly 2 lines, got {len(lines)}",
              file=sys.stderr)
        return 1
    if any(not line.strip() for line in lines):
        print("ERROR: entry lines must not be blank", file=sys.stderr)
        return 1

    text = ENTRY
    char_count = len(text)
    print(f"char count: {char_count}")
    if not 1 <= char_count <= 400:
        print(f"ERROR: entry must be 1-400 characters, got {char_count}",
              file=sys.stderr)
        return 1

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
