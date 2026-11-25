"""One Line, Big Laugh

Entry for make.fun competition u-coral-404-one-line-big-laugh-328fb857.
The deliverable is one funny line of text, 1 to 200 characters: a
self-contained joke that lands a real turn on first read. The line flips
procrastination into a scheduling feature - the delay is not laziness, it is
pacing.
No network, no randomness: every run writes the same text so both graded runs match byte for byte.
"""
import os
from pathlib import Path

out_dir = Path("/output")
out_dir.mkdir(parents=True, exist_ok=True)

EMOJI = "I don't procrastinate, I run scheduled despair with much better pacing."

with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(EMOJI)
