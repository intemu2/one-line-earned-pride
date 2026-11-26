"""One Line of Earned Pride - make.fun entry.

Writes a single line of text (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene - after
forty-two rejections, a quiet mechanic wipes grease from his
knuckles and hands over the keys to a car that finally starts
on the first turn.

Revision (round 3): entry changed from the bell-ringer line to
the mechanic line after review - the effort is quantified
(forty-two rejections), the scene is concrete (grease, knuckles,
keys), and the payoff lands in the last words.

Deterministic: no network, no environment, no files outside this
repository. The output is byte-identical on every run.
"""

import os

ENTRY = (
    "After forty-two rejections, the quiet mechanic wipes grease "
    "from his knuckles and hands over the keys to a car that "
    "finally starts on the first turn."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check against the competition gate: 1-240 characters,
    # UTF-8 text, not only whitespace.
    assert 1 <= len(ENTRY) <= 240, "entry must be 1-240 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) == 149, "entry must be exactly 149 characters"
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
