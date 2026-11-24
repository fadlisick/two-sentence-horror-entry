"""Two-Sentence Horror entry.

The program writes a single two-sentence horror story to entry.txt.
The dread lives in what changes, not in what is said: a dog that used
to growl at empty corners has gone quiet, and now it guards the door.
"""

import os
import sys
from pathlib import Path

OPENING = (
    "The shelter told me the dog I adopted had been returned three times "
    "for staring at empty corners and growling at nothing."
)
TURN = (
    "Last night he finally stopped, and slept pressed against my door, "
    "facing out."
)

GATE_MIN = 1
GATE_MAX = 400


def assemble() -> str:
    """Join the two sentences into the story, exactly as written."""
    return OPENING + " " + TURN


def check_story(story: str) -> None:
    """Enforce the competition gate before anything is written."""
    if not story or not story.strip():
        raise ValueError("story is empty")
    if not GATE_MIN <= len(story) <= GATE_MAX:
        raise ValueError(f"story is {len(story)} chars, gate is 1-400")
    if story.count(".") != 2:
        raise ValueError("story must be exactly two sentences")


def destination() -> Path:
    """Where the grader collects the entry text."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(base) / "entry.txt"


def main() -> int:
    story = assemble()
    check_story(story)
    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = story.encode("utf-8")
    target.write_bytes(payload)
    os.chmod(target, 0o644)
    if target.read_bytes() != payload:
        raise ValueError("entry.txt did not round-trip byte-identical")
    return 0


if __name__ == "__main__":
    sys.exit(main())
