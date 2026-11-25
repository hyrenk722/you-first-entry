"""One Line, One Laugh entry.

A single self-contained joke (67 characters, inside the 1-200 gate):
asked to keep things private, the smart speaker turns the request
back on the asker in two whispered words. The laugh lands inside
the line itself, with no setup to supply and nothing left to trim.
"""

import os

ENTRY = "I asked my smart speaker for privacy and it whispered, 'You first.'"


def validate(text):
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    return text


def main():
    text = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
