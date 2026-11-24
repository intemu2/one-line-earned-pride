"""One Line of Earned Pride — make.fun entry.

Writes a single line of text (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene — a girl
lighter than the bell rope who leans her whole weight into it
until the tenor bell above her turns over and speaks.

Revision (round 2): entry changed from the rehearsed-name line to
the bell-ringer line after blind-duel verification found the bell
line stronger (difficulty self-evident in one read, freshest image).

Deterministic: no network, no environment, no files outside this
repository. The output is byte-identical on every run.
"""

import os

ENTRY = (
    "The rope was heavier than she was, so she leaned back and let "
    "her whole weight go, and the tenor bell above her turned over "
    "and spoke."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check against the competition gate: 1-240 characters,
    # UTF-8 text, not only whitespace.
    assert 1 <= len(ENTRY) <= 240, "entry must be 1-240 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    ENTRY.encode("utf-8")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Read-back check: what landed on disk must be byte-identical
    # to the validated entry, so a silent write fault cannot pass.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    assert written == ENTRY.encode("utf-8"), "output differs from entry"
    assert len(written) == len(ENTRY), "output byte length changed"

    print(f"characters: {len(ENTRY)}")
    print(f"bytes written: {len(written)}")
    print(ENTRY)


if __name__ == "__main__":
    main()
