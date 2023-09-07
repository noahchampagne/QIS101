#!/usr/bin/env python3
"""plot3d_complex_sine.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator

if typing.TYPE_CHECKING:
    from typing import Any
    from matplotlib.axes import Axes

    from numpy.typing import NDArray


def f(x: NDArray[np.float_]) -> NDArray[np.float_]:
    """Helper function used to get the values for our equation"""
    return np.abs(np.sin(x))


def plot(ax: Axes) -> None:
    """Function used to plot the given surface"""
    x: NDArray[np.float_] = np.linspace(-2.5, 2.5, 100)
    y: NDArray[np.complex_] = np.linspace(-1j, 1j, 100)
    # Creates a mesh grid of the x, y coordinate pairs we are going to input into our f(x) function
    x_mesh, y_mesh = np.meshgrid(x, y)  # type: ignore
    z = f(x_mesh + y_mesh)  # type: ignore

    # Labels the graph
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")  # type: ignore
    ax.set_title(r"$|\sin(z)|$")

    # Plots the surface of the function
    ax.plot_surface(
        x_mesh.real,
        y_mesh.imag,
        z,
        cmap=cm.coolwarm,
    )

    ax.zaxis.set_major_locator(LinearLocator(10))  # type: ignore
    ax.zaxis.set_major_formatter("{x:.02f}")  # type: ignore


def main() -> None:
    plt.figure(__file__, constrained_layout=True)
    plot(plt.axes(projection="3d"))
    plt.show()


if __name__ == "__main__":
    main()
