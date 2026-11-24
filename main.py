"""Funniest Autocorrect Fail — one-line entry writer.

Writes a single hilarious autocorrect fail to /output/entry.txt:
one line, under 200 chars, no trailing newline, UTF-8.
"""

from pathlib import Path

TEXT_MESSAGE = (
    "Sarah, I just finished wrapping your wedding gift \u2014 "
    "the toaster looks perfect in its gift casket "
    "with the big red bow, see you Saturday at the church!"
)

DESTINATION = Path("/output/entry.txt")
MAX_LENGTH = 200


def sanity_check(payload: str) -> None:
    """Reject anything that is not exactly one short line."""
    assert "\n" not in payload, "entry must be a single line"
    assert "\r" not in payload, "entry must contain no carriage returns"
    assert len(payload) > 0, "entry must not be empty"
    assert len(payload) < MAX_LENGTH, f"entry is {len(payload)} chars, over limit"


def persist(payload: str, target: Path) -> int:
    """Write the line as UTF-8 bytes with no trailing newline."""
    target.parent.mkdir(parents=True, exist_ok=True)
    encoded = payload.encode("utf-8")
    target.write_bytes(encoded)
    return len(encoded)


def run() -> None:
    sanity_check(TEXT_MESSAGE)
    byte_count = persist(TEXT_MESSAGE, DESTINATION)
    print(f"Wrote {len(TEXT_MESSAGE)} chars ({byte_count} bytes) to {DESTINATION}")
    print(TEXT_MESSAGE)


if __name__ == "__main__":
    run()
