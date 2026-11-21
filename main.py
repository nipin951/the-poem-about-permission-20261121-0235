"""The poem about permission — writes one short poem to /output/entry.txt."""

import os

POEM = """I knocked so softly
the door thought it was the wind.
You opened anyway \u2014
not because I asked well,
but because asking
was already the key
turning in your hand."""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
