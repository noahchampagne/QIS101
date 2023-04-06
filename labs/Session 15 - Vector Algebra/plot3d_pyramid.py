#!/usr/bin/env python3
"""plot3d_pyramid_instructor.py"""

from __future__ import annotations

import os
import sys
import typing
from math import sqrt

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # type: ignore

if typing.TYPE_CHECKING:
    from typing import Any

    from matplotlib.axes import Axes
    from matplotlib.figure import Figure
    from matplotlib.gridspec import GridSpec


def plot(ax: Axes) -> None:
    golden_ratio: float = (1 + sqrt(5)) / 2

    length = 150  # X direction
    width = 150  # Y direction
    height: float = length * golden_ratio  # Z direction

    vertices: list[Any] = [None] * 5
    vertices[0] = (0, 0, 0)  # Base Front Left
    vertices[1] = (length, 0, 0)  # Base Front Right
    vertices[2] = (length, width, 0)  # Base Back Right
    vertices[3] = (0, width, 0)  # Base Back Left
    vertices[4] = (length / 2, width / 2, height)  # Apex

    facets: list[Any] = [None] * 5
    facets[0] = (vertices[0], vertices[1], vertices[2], vertices[3])  # Base
    facets[1] = (vertices[0], vertices[3], vertices[4])  # Left
    facets[2] = (vertices[0], vertices[1], vertices[4])  # Front
    facets[3] = (vertices[1], vertices[2], vertices[4])  # Right
    facets[4] = (vertices[2], vertices[3], vertices[4])  # Back

    p = Poly3DCollection(
        facets, linewidth=3, edgecolors=["darkgoldenrod"], facecolors=["gold"]
    )

    ax.add_collection3d(p)  # type: ignore

    ax.view_init(azim=-79, elev=28)  # type: ignore
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")  # type: ignore
    ax.set_xlim3d(xmin=-10, xmax=200)  # type: ignore
    ax.set_ylim3d(ymin=-10, ymax=200)  # type: ignore
    ax.set_zlim3d(zmin=0, zmax=350)  # type: ignore


def main() -> None:
    fig: Figure = plt.figure(os.path.basename(sys.argv[0]), constrained_layout=True)
    gs: GridSpec = fig.add_gridspec(1, 1)
    ax: Axes = fig.add_subplot(gs[0, 0], projection="3d")  # type: ignore
    plot(ax)  # type: ignore
    plt.show()


if __name__ == "__main__":
    main()
