#!/usr/bin/env python3
"""plot3d_sphere.py"""

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
    u: NDArray[np.float_] = np.linspace(0, np.pi, 30)  # poloidal angle
    v: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 30)  # toroidal angle

    x: NDArray[np.float_] = np.outer(np.sin(u), np.sin(v))
    y: NDArray[np.float_] = np.outer(np.sin(u), np.cos(v))
    z: NDArray[np.float_] = np.outer(np.cos(u), np.ones_like(v))

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")  # type: ignore

    # TODO: Uncomment the following lines one-by-one
    ax.scatter(x, y, z)
    # ax.plot_wireframe(x, y, z)  # type: ignore
    # ax.plot_surface(x, y, z)  # type: ignore


def main() -> None:
    fig: Figure = plt.figure(os.path.basename(sys.argv[0]), constrained_layout=True)
    gs: GridSpec = fig.add_gridspec(1, 1)
    ax: Axes = fig.add_subplot(gs[0, 0], projection="3d")  # type: ignore
    plot(ax)  # type: ignore
    plt.show()


if __name__ == "__main__":
    main()
