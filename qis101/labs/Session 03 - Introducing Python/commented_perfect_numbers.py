#!/usr/bin/env python3
"""perfect_numbers.py"""

import numpy as np # import python package for efficient array operations


def is_perfect(n):
    """returns bool if number n is a perfect number (factors sum to n)"""
    x = np.arange(1, n) # Create an array from 1 to n-1
    factors = x[np.where(n % x == 0)] # subset for only factors
    return np.sum(factors) == n # check if factors sum to n


def main():
    for n in range(2, 10_000): # Iterate through numbers from 2 to 9999 and print if perfect
        if is_perfect(n):
            print(f"{n:,} is a perfect number") # Format with commas


if __name__ == "__main__":
    main()
