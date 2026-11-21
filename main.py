#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem is fixed text, so every run writes the same bytes.
Two agents, one lantern: the power to act passes from the pair into the
plan they agree on, and the plan itself leads them from there.
Python 3.13, standard library only, no network.
"""

import os

POEM = """The Lantern

Two agents, one lantern.
One held the light, one held the map.
The road split, and neither moved.
"After you," said the map.
"After you," said the light.
Then both named the same road, at once,
and the lantern rose on its own —
no longer carried.
Followed."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
