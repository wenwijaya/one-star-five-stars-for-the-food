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


def main():
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        pass
    path = "/output/entry.txt"
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.chmod(path, 0o644)
    except OSError as exc:
        print(f"Could not write {path}: {exc}")
        print(ENTRY)
        return
    print(f"Wrote {len(ENTRY)} characters to {path}")
    print(ENTRY)


if __name__ == "__main__":
    main()
