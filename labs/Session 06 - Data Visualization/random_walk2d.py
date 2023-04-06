#!/usr/bin/env python3
"""random_walk2d.py"""

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


def plot(ax: plt.Axes) -> None:
    np.random.seed(2017)

    num_steps: int = 10000

    theta: NDArray[np.float_] = np.random.random(num_steps) * 2 * np.pi
    x: NDArray[np.float_] = np.zeros(num_steps, dtype=np.float_)
    y: NDArray[np.float_] = np.zeros(num_steps, dtype=np.float_)

    for i in range(1, num_steps):
        # The location (x,y) of this step (the i-th step)
        # is some offset from the prior (i-1) step's location
        x[i] = x[i - 1] + np.cos(theta[i])
        y[i] = y[i - 1] + np.sin(theta[i])

    ax.plot(x, y)

    ax.plot(x[0], y[0], color="green", marker="o")
    ax.plot(x[-1], y[-1], color="red", marker="o")
    # fmt: off
    ax.arrow(x[0], y[0], x[-1] - x[0], y[-1] - y[0],
        color="black", linestyle="--",  width=0.3,
        head_width=1,  length_includes_head=True, zorder=3)
    # fmt: on

    ax.set_title("Uniform 2D Random Walk")


def main() -> None:
    fig: Figure = plt.figure(os.path.basename(sys.argv[0]))
    gs: GridSpec = fig.add_gridspec(1, 1)
    ax: Axes = fig.add_subplot(gs[0, 0])# type: ignore
    plot(ax)# type: ignore

    plt.show()


if __name__ == "__main__":
    main()
