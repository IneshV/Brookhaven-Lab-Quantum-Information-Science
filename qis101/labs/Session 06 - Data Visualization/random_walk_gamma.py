#!/usr/bin/env python3
"""random_walk_gamma.py"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma


def expected_dist(d: np.ndarray, N: int) -> np.ndarray:
    """
    Vectorized computation of E(dist) over array d with fixed N.
    """
    numerator = gamma((d + 1) / 2)
    denominator = gamma(d / 2)
    return np.sqrt((2 * N) / d) * (numerator / denominator) ** 2


def main():
    N = 20_000
    d_vals = np.linspace(1, 25, 500)
    E_vals = expected_dist(d_vals, N)

    plt.figure("random_walk_gamma", figsize=(10, 5))
    plt.plot(d_vals, E_vals, color="tab:blue", lw=2)
    plt.title(rf"Expected Distance After $N={N:,}$ Steps on Unit Lattice of Dimension $d$")
    plt.xlabel(r"Dimension $d$")
    plt.ylabel(r"$\mathbb{E}(\mathrm{dist})$")
    plt.grid(True, linestyle=":")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
