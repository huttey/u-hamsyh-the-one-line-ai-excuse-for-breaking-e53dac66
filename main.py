#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production entry.

Writes a single excuse line to /output/entry.txt.
"""

import os

ENTRY = "I told the cache to remember everything forever, and it believed me — production has served Tuesday's homepage ever since."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
