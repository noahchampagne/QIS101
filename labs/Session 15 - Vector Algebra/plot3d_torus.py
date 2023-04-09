#!/usr/bin/env python3
"""plot3d_torus.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    radius_poloidal: float = 5.0
    radius_toroidal: float = 25.0

    u: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 30)  # Poloidal rotation
    v: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 30)  # Toroidal rotation

    x: NDArray[np.float_] = np.outer(
        radius_toroidal + radius_poloidal * np.sin(u), np.cos(v)
    )
    y: NDArray[np.float_] = np.outer(
        radius_toroidal + radius_poloidal * np.sin(u), np.sin(v)
    )
    z: NDArray[np.float_] = np.outer(radius_poloidal * np.cos(u), np.ones_like(v))

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")  # type: ignore

    ax.view_init(azim=-60, elev=50)  # type: ignore
    ax.set_xlim(-radius_toroidal, radius_toroidal)
    ax.set_ylim(-radius_toroidal, radius_toroidal)
    ax.set_zlim(-radius_toroidal, radius_toroidal)  # type: ignore

    # TODO: Uncomment the following lines one-by-one
    ax.scatter(x, y, z)
    # ax.plot_wireframe(x, y, z)  # type: ignore
    # ax.plot_surface(x, y, z)  # type: ignore


def main() -> None:
    plt.figure(__file__, constrained_layout=True)
    plot(plt.axes(projection="3d"))
    plt.show()


if __name__ == "__main__":
    main()
