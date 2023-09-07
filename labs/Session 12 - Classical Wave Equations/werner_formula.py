#!/usr/bin/env python3
"""werner_formula.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    """Plots various functions"""
    x_vals: NDArray[np.float_] = np.linspace(-3 * np.pi, 3 * np.pi, 80)
    y_vals_1: NDArray[np.float_] = np.sin(0.8 * x_vals)
    y_vals_2: NDArray[np.float_] = np.sin(0.5 * x_vals)
    # Plots the 4 given functions
    plt.plot(x_vals, y_vals_1, label=r"$\sin(.8x)$")
    plt.plot(x_vals, y_vals_2, label=r"$\sin(.5x)$")
    plt.plot(x_vals, y_vals_1 * y_vals_2, label=r"$\sin(.8x) * \sin(.5x)$")
    plt.plot(
        x_vals,
        (np.cos(0.3 * x_vals) - np.cos(1.3 * x_vals)) / 2,
        label=r"$Werner's Product$",
        linestyle="dotted",
        marker="o",
    )

    # Sets the graph's title and labels
    ax.set_title("Various Wave Function")
    ax.set_ylabel("y")
    ax.set_xlabel("x")
    ax.grid()
    ax.legend()


def main() -> None:
    plt.figure(" ")
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
