#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem is fixed text, so every run writes the same bytes.
Two agents, one metronome: each claims a piece of the tempo, then both
count the same beat — and the agreed rhythm takes the counting from
them. The plan keeps time; they only keep the plan.
Python 3.13, standard library only, no network.
"""

import os

POEM = """The Metronome

Two agents, one metronome.
One wound the spring; one chose the beat.
Out of step, they argued the tempo
until both counted — one, two —
and the ticking took the count from them.
It ticks on; no one winds it.
The plan keeps time.
They only keep the plan."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
