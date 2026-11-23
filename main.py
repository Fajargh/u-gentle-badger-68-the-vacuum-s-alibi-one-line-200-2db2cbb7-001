"""The Vacuum's Alibi: One Line, 200 Characters.

Writes one deadpan robot-vacuum excuse for a missed spot to
/output/entry.txt. Deterministic, stdlib only.
"""

import os

ENTRY = (
    "I found the spot, scanned it, and classified it as a protected "
    "dust-bunny habitat. I do not evict tenants."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(line: str) -> None:
    """Gate: the entry must be 1-200 characters, a single line, non-blank."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
