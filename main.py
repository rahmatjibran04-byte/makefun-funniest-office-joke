#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head - make.fun entry.

Writes a single one-line office joke (at most 200 characters) to
/output/entry.txt. Deterministic: the same bytes on every run. No network,
no randomness, no input read from anywhere - the joke is baked into this file.
"""
import os

JOKE = "They replaced the water cooler with a Slack channel, so now the office gossip has a search function."

# Why this joke: the water cooler is the classic office-gossip spot, so the
# setup is instantly recognisable to anyone who has worked in an office.
# The turn swaps it for a Slack channel, and the punchline - the gossip now
# has a search function - lands last, is genuinely new, and is not a plain
# complaint. One line, every word earns its place. Wording kept to 100 bytes:
# the rules break an exact tie on win rate toward the smaller text, so five
# wasted bytes ("We" + "office") were cut without losing any meaning.

OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # Leave the file readable by every user (the grader collects it as
    # another user). Never chmod the output directory itself.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
