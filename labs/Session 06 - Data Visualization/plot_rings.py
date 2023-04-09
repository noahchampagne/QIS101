#!/usr/bin/env python3
"""plot_rings.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    """Draw the Olympic Rings"""
    radius: float = 25.0
    theta: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 1000, dtype=np.float_)
    x: NDArray[np.float_] = radius * np.cos(theta)
    y: NDArray[np.float_] = radius * np.sin(theta)

    x_offset: float = 5 / 2 * radius
    y_offset: float = radius

    ax.plot(x, y, color="black", linewidth=12)
    ax.plot(x - x_offset, y, color="blue", linewidth=12)
    ax.plot(x + x_offset, y, color="red", linewidth=12)
    ax.plot(x - x_offset / 2, y - y_offset, color="yellow", linewidth=12)
    ax.plot(x + x_offset / 2, y - y_offset, color="green", linewidth=12)

    ax.set_title("The Olympic Rings")
    ax.set_aspect("equal")
    ax.axis("off")


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
