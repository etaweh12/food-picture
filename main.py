#!/usr/bin/env python3
"""Make the best-looking food picture — make.fun bounty food-picture-01.

The entry image is a food photograph bundled in this repository
(food.png). This program deterministically copies it to
/output/entry.png, as the brief allows ("the simplest program
copies an image the repository holds").

No network access. Running it twice writes identical bytes.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "food.png")
DST = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.png")


def main() -> int:
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    print(f"wrote {DST} ({os.path.getsize(DST)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
