#!/usr/bin/env python3
"""plot3d_surface.py"""

from __future__ import annotations

import os
import sys
import typing

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator

if typing.TYPE_CHECKING:
    from typing import Any
    from matplotlib.axes import Axes
    from matplotlib.figure import Figure
    from matplotlib.gridspec import GridSpec
    from numpy.typing import NDArray


def f(x: NDArray[np.float_], y: NDArray[np.float_]) -> NDArray[np.float_]:
    return np.array(np.sin(np.sqrt(x**2 + y**2)))


def plot(ax: Axes) -> None:
    x: NDArray[np.float_] = np.linspace(-5, 5, 100)
    y: NDArray[np.float_] = np.linspace(-5, 5, 100)

    x, y = np.meshgrid(x, y)

    z: NDArray[np.float_] = f(x, y)

    surf: Any = ax.plot_surface(  # type: ignore
        x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=False  # type: ignore
    )

    ax.zaxis.set_major_locator(LinearLocator(10))  # type: ignore
    ax.zaxis.set_major_formatter("{x:.02f}")  # type: ignore

    plt.colorbar(surf, ax=ax, shrink=0.5, aspect=5)


def main() -> None:
    fig: Figure = plt.figure(os.path.basename(sys.argv[0]), constrained_layout=True)
    gs: GridSpec = fig.add_gridspec(1, 1)
    ax: Axes = fig.add_subplot(gs[0, 0], projection="3d")  # type: ignore
    plot(ax)  # type: ignore
    plt.show()


if __name__ == "__main__":
    main()
