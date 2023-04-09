#!/usr/bin/env python3
"""welcome.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    x: NDArray[np.float_] = np.linspace(-2, 2, 500, dtype=np.float_)
    f_top: NDArray[np.float_] = np.sqrt(1 - (np.abs(x) - 1) ** 2)
    f_bot: NDArray[np.float_] = np.arccos(1 - np.abs(x)) - np.pi
    ax.plot(x, f_top, color="red")
    ax.plot(x, f_bot, color="red")
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-3.5, 1.5)
    ax.set_title("Welcome to the Foundations of Quantum Information Science!")
    ax.set_aspect("equal")


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
