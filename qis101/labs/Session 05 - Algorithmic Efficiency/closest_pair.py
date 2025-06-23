#!/usr/bin/env python3
"""closest_point.py"""

import math
import random
import time
from pprint import pprint

def generate_points(n, x_range, y_range):
    """Generate n random points within the given range."""
    random.seed(2025)
    return [
        (round(random.uniform(*x_range), 4), round(random.uniform(*y_range), 4))
        for _ in range(n)
    ]

def closest_pair(points):
    """
    Return ((p, q), dist) where p and q are the closest pair in 'points'.

    Uses a divide-and-conquer scheme running in O(n log n) time.
    Falls back to a brute-force O(n²) approach for very small sub-arrays.
    """
    if len(points) < 2:
        return (None, None), float("inf")

    # Pre-sort once – guarantees n log n overall
    pts_x = sorted(points)                      # sort by x then y
    pts_y = sorted(points, key=lambda p: p[1])  # sort by y

    def dist_sq(a, b):
        dx = a[0] - b[0]
        dy = a[1] - b[1]
        return dx * dx + dy * dy

    def recurse(px, py):
        n = len(px)
        if n <= 3:                              # brute force
            best = float("inf")
            pair = (None, None)
            for i in range(n):
                for j in range(i + 1, n):
                    d = dist_sq(px[i], px[j])
                    if d < best:
                        best, pair = d, (px[i], px[j])
            return pair, best

        mid = n // 2
        mid_x = px[mid][0]

        # Split x-sorted list
        qx, rx = px[:mid], px[mid:]

        # Stable split of y-sorted list in linear time
        qy, ry = [], []
        for p in py:
            (qy if p[0] <= mid_x else ry).append(p)

        (pair_l, d_l) = recurse(qx, qy)
        (pair_r, d_r) = recurse(rx, ry)

        best_pair, best_d = (pair_l, d_l) if d_l < d_r else (pair_r, d_r)

        # Points within  sqr rooted best_d of the split line
        strip = [p for p in py if abs(p[0] - mid_x) ** 2 < best_d]

        # A point in the strip needs only be compared to the next ≤ 7 points
        m = len(strip)
        for i in range(m):
            for j in range(i + 1, min(i + 8, m)):
                d = dist_sq(strip[i], strip[j])
                if d < best_d:
                    best_d = d
                    best_pair = (strip[i], strip[j])

        return best_pair, best_d

    pair, d_sq = recurse(pts_x, pts_y)
    return pair, math.sqrt(d_sq)

def main():
    num_points = 10_000
    print(f"Generating {num_points:,} random points")
    points = generate_points(num_points, (0, 100), (0, 100))
    print("First five random points:")
    pprint(points[:5])
    print("Finding the closest pair:")

    start = time.perf_counter()
    pair, dist = closest_pair(points)
    elapsed = time.perf_counter() - start

    print(f"Nearest points : {pair[0]}  &  {pair[1]}")
    print(f"Minimum distance = {dist:.4f}")
    print(f"Time taken       = {elapsed:.4f} s")


if __name__ == "__main__":
    main()
