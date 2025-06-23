#!/usr/bin/env python3
"""lcm_gcd.py"""

import math  # Import for built-in gcd function

def lcm(a: int, b: int) -> int:
    """Calculate LCM using the formula: abs(a*b) // gcd(a, b)"""
    return abs(a * b) // math.gcd(a, b)

def main() -> None:
    a = 447_618
    b = 2_011_835
    result = lcm(a, b)
    print(f"LCM of {a:,} and {b:,} is {result:,}")

if __name__ == "__main__":
    main()
