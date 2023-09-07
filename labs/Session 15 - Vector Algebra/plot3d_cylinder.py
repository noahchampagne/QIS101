#!/usr/bin/env/python 3
"""plot3d_cylinder.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes

    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    """Plots a cylinder using MatPlotLibs 3D graphing"""
    theta: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 30)

    # Creates the coordinates for the cylinder
    x: NDArray[np.float_] = np.outer(np.ones_like(theta), np.sin(theta))
    y: NDArray[np.float_] = np.outer(np.ones_like(theta), np.cos(theta))
    z: NDArray[np.float_] = np.outer(np.linspace(-1, 1, 30), np.ones_like(theta))

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")  # type: ignore
    ax.set_title("Wireframe Plot of a Cylinder")

    # Plots the coordinates in a wire frame
    ax.plot_wireframe(x, y, z)  # type: ignore


def main() -> None:
    plt.figure(__file__, constrained_layout=True)
    plot(plt.axes(projection="3d"))
    plt.show()


if __name__ == "__main__":
    main()
