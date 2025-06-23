#!/usr/bin/env python3
"""board_encoding.py"""

from typing import List

SYMBOL = {0: " ", 1: "X", 2: "O"}


def to_base3(n: int, length: int = 9) -> List[int]:
    """Return *length* base-3 digits of *n* (MSD first), zero-padded."""
    digits: List[int] = [0] * length
    i = length - 1
    while n > 0 and i >= 0:
        n, rem = divmod(n, 3)
        digits[i] = rem
        i -= 1
    return digits


def print_board(code: int) -> None:
    """Decode *code* and print the 3×3 board."""
    trits = to_base3(code, 9)
    cells = [SYMBOL[d] for d in trits]

    print(f"Encoded integer: {code}")
    for r in range(0, 9, 3):
        print(" " + " | ".join(cells[r : r + 3]) + " ")
        if r < 6:
            print("---+---+---")
    print()


def main() -> None:
    for encoded in (2271, 1638, 12065):
        print_board(encoded)


if __name__ == "__main__":
    main()
