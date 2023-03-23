#!/usr/bin/env python3
"""fermat_derivative.py"""

from __future__ import annotations

import os
import sys
import typing

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from matplotlib.figure import Figure
    from matplotlib.gridspec import GridSpec
    from numpy.typing import NDArray


def f(x: NDArray[np.float_]) -> NDArray[np.float_]:
    return np.cos(x)


def f_prime(x: NDArray[np.float_], h: float) -> NDArray[np.float_]:
    return (f(x + h) - f(x)) / h


def plot(ax: Axes) -> None:
    a: float = -4 * np.pi
    b: float = 4 * np.pi
    n: int = 500

    x: NDArray[np.float_] = np.linspace(a, b, n, dtype=float)

    y: NDArray[np.float_] = f(x)
    y_prime: NDArray[np.float_] = f_prime(x, (b - a) / n)

    ax.plot(x, y, label=r"$y=\cos{x}$")
    ax.plot(x, y_prime, label=r"$\frac{dy}{dx}=-\sin{x}$")

    ax.set_title("Fermat's Difference Quotient")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.xaxis.set_major_locator(MultipleLocator(2))
    ax.yaxis.set_major_locator(MultipleLocator(0.2))
    ax.legend(loc="upper right")

    ax.axhline(0, color="black", linestyle="-")
    ax.axvline(0, color="black", linestyle="-")


def main() -> None:
    fig: Figure = plt.figure(os.path.basename(sys.argv[0]))
    gs: GridSpec = fig.add_gridspec(1, 1)
    ax: Axes = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
