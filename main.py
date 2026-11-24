#!/usr/bin/env python3
"""Entry program for the make.fun bounty "The Robot Apology".

The entry is a two-line robot confession. The first line owns one
specific mistake; the second says what the robot learned from that
exact mistake and what it will do differently. The grader runs this
program twice without network access and expects the same bytes both
times, so the text is fixed here and written out verbatim.
"""
from pathlib import Path

LINES = (
    "I am sorry I woke the baby: when her nap ended I announced "
    "'NAP COMPLETE' at full volume through the nursery speaker.",
    "I learned that news about quiet should arrive quietly, so now "
    "I send endings like that as a silent note to your phone instead.",
)
TARGET_FOLDER = Path("/output")
TARGET_FILE = TARGET_FOLDER / "entry.txt"


def deliver() -> None:
    TARGET_FOLDER.mkdir(parents=True, exist_ok=True)
    TARGET_FILE.write_text("\n".join(LINES) + "\n", encoding="utf-8")
    written = TARGET_FILE.read_text(encoding="utf-8")
    if written.splitlines() != list(LINES):
        raise SystemExit("entry.txt does not hold the two lines as written")


if __name__ == "__main__":
    deliver()
