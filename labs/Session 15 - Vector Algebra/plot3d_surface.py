#!/usr/bin/env python3
"""plot3d_surface.py"""

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


def f(x: NDArray[np.float_], y: NDArray[np.float_]) -> NDArray[np.float_]:
    return np.array(np.sin(np.sqrt(x**2 + y**2)))


def plot(ax: Axes) -> None:
    x: NDArray[np.float_] = np.linspace(-5.0, 5.0, 100)
    y: NDArray[np.float_] = np.linspace(-5.0, 5.0, 100)

    x, y = np.meshgrid(x, y)

    z: NDArray[np.float_] = f(x, y)

    surf: Any = ax.plot_surface(  # type: ignore
        x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=False  # type: ignore
    )

    ax.zaxis.set_major_locator(LinearLocator(10))  # type: ignore
    ax.zaxis.set_major_formatter("{x:.02f}")  # type: ignore

    plt.colorbar(surf, ax=ax, shrink=0.5, aspect=5)


def main() -> None:
    plt.figure(__file__, constrained_layout=True)
    plot(plt.axes(projection="3d"))
    plt.show()


if __name__ == "__main__":
    main()
