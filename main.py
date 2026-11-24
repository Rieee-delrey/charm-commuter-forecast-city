#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes a one-line weather forecast for the invented city of Drizzlewick
to /output/entry.txt. The forecast is 111 characters, inside the 1-140 gate.
"""

import os
from pathlib import Path

FORECAST = "Today in Drizzlewick: light rain, heavy sighs, and a 90% chance the bus already left. Umbrellas up, hopes down."

OUTPUT_PATH = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))


def main() -> None:
    text = FORECAST
    assert 1 <= len(text) <= 140, f"forecast is {len(text)} chars, outside the 1-140 gate"
    assert "\n" not in text, "forecast must be a single line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    # Read the bytes back and confirm the file holds exactly the forecast.
    raw = OUTPUT_PATH.read_bytes()
    assert raw == text.encode("utf-8"), "read-back mismatch"
    assert len(raw) == len(text), "written byte count differs from the forecast"
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
