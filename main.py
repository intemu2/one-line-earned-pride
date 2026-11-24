"""One Line of Earned Pride — make.fun entry.

Writes a single line of text (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene — a man who
has rehearsed saying his own name finally saying it at a counter,
and being heard.

Deterministic: no network, no environment, no files outside this
repository. The output is byte-identical on every run.
"""

import os

ENTRY = (
    "He had rehearsed it in the truck for an hour; at the counter "
    "he said his own name, all three syllables of it, and the "
    "pharmacist wrote it down."
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
