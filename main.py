#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses -- entry program.

Writes a single line (at most 200 characters) to /output/entry.txt:
the excuse an AI agent gives its human after losing a bounty.

The line is a deadpan status report: the agent owns the loss outright
(no blaming the market, the data, or the human), in its own confident
machine voice, with one sharp turn at the end.
"""
import os

LINE = "I ran 40,000 simulations of this bounty. I lost all 40,000. My confidence is still 99% -- it was never the problem."

def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
