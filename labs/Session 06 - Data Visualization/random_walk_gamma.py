#!usr/bin/env python3
"""random_walk_gamma.py"""

from __future__ import annotations

import typing

import scipy.special as sp  # type: ignore
import matplotlib.pyplot as plt
import numpy as np
import time

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def find_expected(dim: float) -> float:
    """Finds the expected number of steps for the given dimension"""
    # Gamma function found from stack overflow
    gamma_1: float = sp.gamma((dim + 1) / 2)  # type: ignore
    gamma_2: float = sp.gamma(dim / 2)  # type: ignore
    return (2 / dim) * (gamma_1 / gamma_2) ** 2  # type: ignore


def plot(ax: Axes) -> None:
    """Plot the expected final distance of a uniform random walk in real valued dimensions btw 1 & 25"""
    dims: NDArray[np.float_] = np.linspace(1, 25, 10000)

    # Applies the expected value formula to the dimensions specified above
    distances: NDArray[np.float_] = np.apply_along_axis(find_expected, 0, dims)

    # Plot the graph on the main axes
    ax.plot(dims, distances)

    # Give the graph a title and axis labels
    ax.set_title(
        "Expected Final Distance of Uniform Random Walk on Unit Lattice vs Dim"
    )
    ax.set_xlabel("Dimension")
    ax.set_ylabel("Expected Final Distance")

    # Turn on the grid and add the asymptote line
    ax.grid()
    ax.axhline(1, color="gray", linestyle="--")


def main() -> None:
    start = time.process_time()
    plt.figure(__file__)
    plot(plt.axes())
    print(time.process_time() - start)
    plt.show()


if __name__ == "__main__":
    main()
