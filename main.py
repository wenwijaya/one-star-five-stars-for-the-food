#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes a single alien-tourist one-star review of planet Earth (one
sentence, at most 200 characters, with a real compliment about the
food) to /output/entry.txt.
"""

import os

ENTRY = (
    "One star: Earth made me pay rent to breathe, wait in line behind a "
    "goose for a parking permit, and then served noodles so good I am "
    "applying for citizenship."
)


MAX_CHARS = 200


def _validate(entry):
    """Keep the review inside the brief: one sentence, at most 200 chars."""
    text = entry.strip()
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the 200-char cap")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    return text


def main():
    try:
        entry = _validate(ENTRY)
    except ValueError as exc:
        print(f"Invalid entry: {exc}")
        return 1
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        pass
    path = "/output/entry.txt"
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(entry)
        os.chmod(path, 0o644)
    except OSError as exc:
        print(f"Could not write {path}: {exc}")
        print(entry)
        return
    print(f"Wrote {len(entry)} characters to {path}")
    print(entry)


if __name__ == "__main__":
    main()
