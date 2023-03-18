#!/usr/bin/env python3
"""plot_rose_curves.py"""

from __future__ import annotations

import os
import sys
import typing

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from matplotlib.figure import Figure
    from numpy.typing import NDArray

num_curves: int = 1


def plot(ax: Axes) -> None:
    """Draw parametric polar curves where radius is a function of theta"""
    theta: NDArray[np.float_] = np.linspace(0, 4 * np.pi, 1000, dtype=np.float_)

    radius_1: NDArray[np.float_] = 4.0 + 4 * np.cos(4 * theta)
    radius_2: NDArray[np.float_] = 3.0 + 3 * np.cos(4 * theta + np.pi)
    radius_3: NDArray[np.float_] = 5.0 + 5 * np.cos(3 / 2 * theta)
    radius_4: NDArray[np.float_] = 7.0 + 7 * np.cos(5 * theta) * np.sin(11 * theta)

    if num_curves < 4:
        ax.plot(theta, radius_1, color="blue")
        ax.set_ylim(0, 11)

    if 2 <= num_curves < 4:
        ax.plot(theta, radius_2, color="green")

    if 3 <= num_curves < 4:
        ax.plot(theta, radius_3, color="red")

    if num_curves == 4:
        ax.plot(theta, radius_4, color="black")

    ax.set_aspect("equal")
    ax.axis()


def main() -> None:
    fig: Figure
    ax: Axes
    fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
    fig.canvas.manager.set_window_title(os.path.basename(sys.argv[0]))  # type: ignore
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
