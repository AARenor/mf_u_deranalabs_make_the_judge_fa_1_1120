"""Write the entry line for make.fun's bounty to entry.txt.

The program is deterministic: it always writes the same bytes, with no
trailing newline, into MAKEFUN_OUTPUT_DIR when set, otherwise /output.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "For three years my father called the dog by my name. "
    "The dog has been dead since 2019. I answer anyway."
)

assert 1 <= len(TEXT) <= 280, "entry text must be between 1 and 280 characters"


def output_dir() -> Path:
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR")
    return Path(chosen or "/output")


def main() -> int:
    directory = output_dir()
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
