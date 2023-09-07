#!/usr/bin/env python3
"""plot_ellipse.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    """Plot an ellipse of height 100 and length 50 centered at the origin"""
    x_rad: float = 50.0
    y_rad: float = 25.0
    theta: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 1000)

    # Polar to Cartesian coordinate conversion using vectorized operations
    x: NDArray[np.float_] = x_rad * np.cos(theta)
    y: NDArray[np.float_] = y_rad * np.sin(theta)

    # Plot the graph on the main axes
    ax.plot(x, y)

    # Sets the equation title for the graph is TeX formatting
    ax.set_title(
        rf"$\frac {{x^2}} {{{int(x_rad)}^2}} + \frac {{y^2}} {{{int(y_rad)}^2}} = 1$"
    )

    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.grid()
    ax.axhline(0, color="black")
    ax.axvline(0, color="black")

    # Ensures that the aspect ratio of your screen makes x & y equal distances
    ax.set_aspect("equal")


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
