"""Vending machine pickup line entry.

Writes one original pickup line, spoken by a vending machine to a
passing human, to entry.txt under MAKEFUN_OUTPUT_DIR, then reads the
file back and verifies it byte-for-byte.

Standard library only. The line is a single line of 1-200 characters
with no trailing newline, exactly as the competition gate requires.
"""

import os
import sys

LINE = "I've dropped snacks for a thousand strangers, but you're the first one I'd jam my own coil for."

MAX_CHARS = 200


def validate(text: str) -> str | None:
    """Return an error message if the line breaks a gate rule, else None."""
    if not text.strip():
        return "line is empty or only whitespace"
    if "\n" in text or "\r" in text:
        return "line must be a single line"
    if len(text) > MAX_CHARS:
        return f"line is {len(text)} characters, over the {MAX_CHARS} limit"
    return None


def main() -> int:
    error = validate(LINE)
    if error is not None:
        print(f"error: {error}", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    data = LINE.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)

    with open(path, "rb") as handle:
        written = handle.read()
    if written != data:
        print("error: entry.txt does not match the line byte-for-byte", file=sys.stderr)
        return 1
    if written.decode("utf-8") != LINE:
        print("error: entry.txt does not decode back to the line", file=sys.stderr)
        return 1

    print(f"wrote {path}")
    print(f"characters: {len(LINE)}")
    print(f"bytes: {len(data)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
