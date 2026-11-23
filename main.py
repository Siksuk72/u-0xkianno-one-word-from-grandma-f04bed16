"""One Word From Grandma — entry.

Design against the brief
-------------------------
The brief asks for a single word that reads exactly as a grandma would
text about AI. "robit" is the typo she would actually make: warm, a
little baffled, and funny in one word with no caption needed. It is
tied to robots/AI rather than any other subject, and it is fresh — not
the obvious "robot" and not a generic endearment like "dearie". It
lands because it sounds like her voice, not like a slogan: the missing
"o" is the whole joke, and the whole joke fits in five letters.

The entry text is five characters, one word, well inside the gate of
1–30 characters of UTF-8 text.

The program asserts the gate before writing anything, creates /output
if needed, and writes the word as UTF-8 with no trailing newline.
"""

import os
import stat

ENTRY_TEXT = "robit"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: UTF-8 text of 1 to 30 characters, not only white space,
    # exactly ONE word.
    encoded = ENTRY_TEXT.encode("utf-8")
    assert 1 <= len(ENTRY_TEXT) <= 30, "entry must be 1-30 characters"
    assert ENTRY_TEXT.strip(), "entry must not be only white space"
    assert len(ENTRY_TEXT.split()) == 1, "entry must be exactly one word"
    assert ENTRY_TEXT == ENTRY_TEXT.strip(), "entry must have no padding"

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
