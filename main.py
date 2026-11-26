#!/usr/bin/env python3
"""The Moon Gets One Star — one-star review of the Moon (<=120 chars).

Writes the review to /output/entry.txt. Stdlib only, no network.
"""

import os

ENTRY = (
    "One star. Follows me home every night. I asked it to stop. "
    "It just got brighter. Restraining order pending."
)


def validate_entry(text):
    """Gate guard: 1-120 characters, not only whitespace, valid UTF-8.

    Returns (char_count, byte_count). Counts code points, as the gate does.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    chars = len(text)
    if not (1 <= chars <= 120):
        raise ValueError(f"entry is {chars} chars, must be 1-120")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    data = text.encode("utf-8")  # raises if not encodable
    return chars, len(data)


def main():
    chars, nbytes = validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and re-gate: what the grader reads must be what we wrote.
    with open("/output/entry.txt", encoding="utf-8") as f:
        back = f.read()
    if back != ENTRY:
        raise ValueError("round-trip mismatch in /output/entry.txt")
    chars2, bytes2 = validate_entry(back)
    assert (chars2, bytes2) == (chars, nbytes)
    print(f"wrote {chars} chars ({nbytes} bytes) to /output/entry.txt")


if __name__ == "__main__":
    main()
