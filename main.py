#!/usr/bin/env python3
"""Write one Wi-Fi network name to /output/entry.txt.

The name is the entry for the make.fun bounty "Tell a Whole Story in
32 Characters": a single Wi-Fi name, at most 32 characters, that lands a
joke and implies a whole story to anyone who sees it in a phone's
network list.

The name:

    My last breakup cost me the WiFi

Thirty-two characters, exactly on the limit. The joke is that the
breakup did not cost him the flat, the car or the dog -- it cost him
the Wi-Fi, as if the router were listed on the divorce papers next to
the furniture. "Last" quietly admits this is not his first breakup,
so the name carries a whole history in two words: a serial heartbreak
whose latest casualty was the internet. And the name is, itself, a
Wi-Fi network -- the replacement he had to set up after losing the
old one. The story writes its own sequel every time a neighbour's
phone scans for networks.
"""

import os

ENTRY = "My last breakup cost me the WiFi"

MAX_LENGTH = 32


def main() -> None:
    name = ENTRY.strip()
    if not 1 <= len(name) <= MAX_LENGTH:
        raise SystemExit(
            f"entry must be 1-{MAX_LENGTH} characters, got {len(name)}: {name!r}"
        )
    if not name.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in name or "\r" in name:
        raise SystemExit("entry must be a single line")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(name + "\n")
    written = open(os.path.join(out_dir, "entry.txt"), encoding="utf-8").read()
    if written.rstrip("\n") != name or len(written.rstrip("\n")) != len(name):
        raise SystemExit("entry.txt does not hold exactly the entry")


if __name__ == "__main__":
    main()
