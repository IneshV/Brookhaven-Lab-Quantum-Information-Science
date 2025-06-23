#!/usr/bin/env python3
"""sum_squares.py"""

def main() -> None:
    # Sum using a loop
    loop_sum = sum(i * i for i in range(1, 1001))

    # Sum using the formula: n(n + 1)(2n + 1)/6
    n = 1000
    formula_sum = n * (n + 1) * (2 * n + 1) // 6

    # Print both with thousands separator
    print(f"Loop sum:     {loop_sum:,}")
    print(f"Formula sum:  {formula_sum:,}")

if __name__ == "__main__":
    main()
