#!/usr/bin/env python3
"""custom_cf.py"""

import math

def encode_cf(x, max_terms=7):
    """Convert a number into a list of its continued fraction terms"""
    cf: list[int] = []
    while len(cf) < max_terms:
        cf.append(int(x))
        x -= int(x)
        if x < 1e-11:
            break
        x = 1 / x
    return cf

def main():
    for n in range(1, 10):  # n = 1 to 9
        xn = (1 + math.sqrt(4 * n ** 2 - 4 * n + 5)) / 2
        cf = encode_cf(xn, max_terms=7)
        print(f"x_{n} = {xn:.10f} -> {cf}")

if __name__ == "__main__":
    main()
