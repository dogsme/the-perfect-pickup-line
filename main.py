#!/usr/bin/env python3
"""The Perfect Pickup Line.

Writes one pickup line — the kind an AI agent could actually say out loud
to a person — to /output/entry.txt.
"""

import os

LINE = "I ran a million simulations of us meeting, and in every single one I still got nervous."


def main() -> None:
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("pickup line must be 1-200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
