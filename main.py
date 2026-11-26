"""Entry for make.fun's "Make the AI Judge Laugh: the Office Joke Open".

Writes the one-line office joke to /output/entry.txt (UTF-8, no trailing
newline) so the sealed scorer and judge can read it.
"""

import os

# The joke: in our standup, yesterday's blockers formally greet today's.
# Kept as a single line, exactly as the judges will read it.
ENTRY = "Our standup is just a daily meeting where the blockers introduce themselves to new blockers."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
