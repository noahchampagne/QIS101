#!/usr/bin/env python3
"""plot3d_helix.py"""

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
    theta: NDArray[np.float_] = np.linspace(0, 20 * np.pi, 2000)  # poloidal angle

    x: NDArray[np.float_] = theta * np.cos(theta)
    y: NDArray[np.float_] = theta * np.sin(theta)
    z: NDArray[np.float_] = theta

    ax.plot(x, y, z)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")  # type: ignore


def main() -> None:
    fig: Figure = plt.figure(os.path.basename(sys.argv[0]), constrained_layout=True)
    gs: GridSpec = fig.add_gridspec(1, 1)
    ax: Axes = fig.add_subplot(gs[0, 0], projection="3d")  # type: ignore
    plot(ax)  # type: ignore

    plt.show()


if __name__ == "__main__":
    main()
