"""Office Joke Open entry.

The joke: a standup meeting where everyone cheerfully reports "no blockers"
while the project visibly burns behind them — denial as a screensaver.
This program writes that single line to /output/entry.txt.
"""

import os

ENTRY = "Our standup is just three people saying no blockers while the project burns behind them like a screensaver."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
