#!/usr/bin/env python3
"""One Line, Lights Out — make.fun entry.

Writes exactly one status update (97 characters, limit 200) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The line is the winner of a local pairwise tournament: 12 original
candidate lines judged by the Caffeine Inference router (model "router")
against the bounty's published judge brief verbatim. Swiss format,
3 rounds, every game played in both label orders (2 judge calls per
game), then a final between the top 2. See tournament.jsonl and
README.md for the full table. Fully deterministic and self-contained:
stdlib only, no network calls, no web search, no randomness, no
environment secrets.
"""

import os

LINE = "I watched the battery icon turn grey. Somewhere in the dark, your draft is still called Untitled."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
