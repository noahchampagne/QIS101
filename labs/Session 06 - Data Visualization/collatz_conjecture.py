#!/usr/bin/env python3
"""collatz_conjecture.py"""

from __future__ import annotations

import os
import sys
import typing

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator
from numba import njit  # type: ignore

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from matplotlib.figure import Figure
    from matplotlib.gridspec import GridSpec
    from numpy.typing import NDArray


@njit()  # type: ignore
def stop_time(n: int) -> int:
    """Return the Collatz stopping time for the given integer"""
    counter: int = 0
    while n > 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        counter += 1
    return counter


@njit()  # type: ignore
def stop_times(max_n: int) -> NDArray[np.int_]:
    """Returns the Collatz stopping time for each integer to max_n"""
    y: NDArray[np.int_] = np.zeros(max_n, dtype=np.int_)
    for i in range(max_n):
        y[i] = stop_time(i)
    return y


def plot(ax: plt.Axes) -> None:
    """Plot a histogram of Collatz stopping times"""
    max_n: int = 100_000_000

    print(f"Calculating the Collatz stopping time for each integer to {max_n:,}")

    y: NDArray[np.int_] = stop_times(max_n)

    ax.set_title(f"Collatz Conjecture (n < {max_n:,})")
    ax.set_xlabel("Stopping Time")
    ax.set_ylabel("Count")

    ax.hist(y, bins=500, color="blue")

    ax.yaxis.set_minor_locator(AutoMinorLocator())


def main() -> None:
    fig: Figure = plt.figure(os.path.basename(sys.argv[0]))
    gs: GridSpec = fig.add_gridspec(1, 1)
    ax: Axes = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
