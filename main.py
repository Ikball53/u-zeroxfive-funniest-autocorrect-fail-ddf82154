"""Funniest Autocorrect Fail entry.

Writes one deadpan autocorrect-fail line to /output/entry.txt.
No trailing newline, UTF-8, under 200 characters.
"""

from pathlib import Path

ENTRY_LINE = (
    "I emailed my boss Mr. Carter 'Can we reschedule our meeting to Friday?' — "
    "autocorrect sent 'Can we reschedule our mating to Friday?' "
    "and now HR wants to see me Monday."
)


def main() -> None:
    destination = Path("/output/entry.txt")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(ENTRY_LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
