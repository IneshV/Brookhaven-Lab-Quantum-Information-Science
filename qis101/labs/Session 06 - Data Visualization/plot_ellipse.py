#!/usr/bin/env python3
"""plot_ellipse.py"""

import numpy as np
import matplotlib.pyplot as plt


def ellipse_polar(a: float, b: float, num: int = 720) -> tuple[np.ndarray, np.ndarray]:
    """Return x, y coordinates of the ellipse using the polar-radius formula."""
    theta = np.linspace(0, 2 * np.pi, num, endpoint=False)
    r = (a * b) / np.sqrt((b * np.cos(theta)) ** 2 + (a * np.sin(theta)) ** 2)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y


def main() -> None:
    # Ellipse parameters
    a, b = 100.0, 50.0

    # Generate perimeter points
    x, y = ellipse_polar(a, b)

    # Plot 
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(x, y, lw=2, color="tab:blue")

    ax.axhline(0, color="k", lw=1)
    ax.axvline(0, color="k", lw=1)

    ax.grid("on")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
