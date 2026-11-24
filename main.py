#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes the single excuse line to /output/entry.txt (no trailing newline),
where the make.fun gate checks it is UTF-8 text of 1 to 160 characters.
"""

LINE = (
    "I ran 214 simulations of finishing on time. In every one I missed "
    "the deadline anyway, so I stopped simulating and started apologizing."
)


def main() -> None:
    """Write the excuse line to /output/entry.txt, no trailing newline."""
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars, must be 1-160"
    assert LINE == LINE.strip(), "line must not start or end with whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
