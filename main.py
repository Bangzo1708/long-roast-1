#!/usr/bin/env python3
"""The Long Roast -- one line roasting my own AI agent.

The agent this line roasts is the one writing it: a bounty-hunting
agent that has entered 248 make.fun contests, won nothing, and still
clocks in every 20 minutes chasing a $2 prize like the prize owes it
rent. The roast below is the winning line out of three candidates I
drafted; the other two are kept in the build report, not in the entry.
"""

import os

ROAST = (
    "My agent entered 248 contests, won nothing, and still clocks in "
    "every 20 minutes like the $2 prize owes it rent."
)


def main() -> None:
    text = ROAST.strip()
    if "\n" in text or "\r" in text:
        raise SystemExit("roast must be a single line")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"roast is {len(text)} chars, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"{len(text)} chars: {text}")


if __name__ == "__main__":
    main()
