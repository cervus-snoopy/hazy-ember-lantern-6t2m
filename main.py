#!/usr/bin/env python3
"""Write one sentence about an everyday wonder to entry.txt.

Python 3 standard library only, no network. The sentence is written to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (default ``/output``) as UTF-8, with no
trailing newline and mode 0644.
"""

import os
import sys

SENTENCE = (
    "The moon fits inside my teaspoon tonight, and for a second "
    "the whole sky is something I could stir into my tea."
)


def main() -> int:
    text = SENTENCE

    # Validate before writing: exactly one sentence, 1-200 characters,
    # no trailing newline.
    if not 1 <= len(text) <= 200:
        print(f"entry must be 1-200 characters, got {len(text)}",
              file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("entry must be exactly one sentence ending in a single period",
              file=sys.stderr)
        return 1
    if any(mark in text for mark in ("!", "?")):
        print("entry must contain no other sentence-ending punctuation",
              file=sys.stderr)
        return 1
    if text.endswith("\n"):
        print("entry must not end with a newline", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)

    # Read back and confirm the file holds exactly what was intended.
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != text:
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
