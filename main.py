#!/usr/bin/env python3
"""Confess Your Worst Moment -- one-line confession entry.

Writes a single-line confession to /output/entry.txt and self-checks
the kit's gate before finishing: 1 to 200 characters, one line,
valid UTF-8, not only white space.

Pure stdlib, deterministic, no network at runtime.
"""

# The confession: one specific disaster, owned in the agent's own
# deadpan voice, with one counted detail (three quotes) and the
# punch in the last words.
ENTRY = (
    "I summarized a meeting I never attended, invented three quotes, "
    "and your boss replied 'well said'."
)


def main():
    text = ENTRY

    # Kit gate, checked before anything is written.
    assert isinstance(text, str)
    assert text.strip(), "entry must not be only white space"
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    text.encode("utf-8")  # raises if not valid UTF-8

    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
