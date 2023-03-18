#!/usr/bin/env python3
"""plot_parabola.py"""

from __future__ import annotations

import os
import sys
import typing

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from matplotlib.figure import Figure
    from matplotlib.gridspec import GridSpec
    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    """Plot y = x^2 + 1 over the domain [-6, 6]"""
    x: NDArray[np.float_] = np.linspace(-4, 5, 100, dtype=np.float_)
    y: NDArray[np.float_] = np.power(x, 2) + 1.0

    # Plot the graph on the main axes
    ax.plot(x, y)

    # Give the graph a title and axis labels
    ax.set_title("$y = x^2+1$")  # LaTeX format
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # Center the graph over an appropriate domain
    ax.set_xlim(-6, 6)
    ax.set_ylim(-3, 30)

    # Turn on the grid, and add decorations
    ax.grid()
    ax.plot(0, 1, color="red", marker="o")
    ax.axhline(1, color="gray", linestyle="--")


def main() -> None:
    fig: Figure = plt.figure(os.path.basename(sys.argv[0]))
    gs: GridSpec = fig.add_gridspec(1, 1)
    ax: Axes = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
