#!/usr/bin/env python3
"""taylor_series.py"""

from __future__ import annotations

import os
import sys
import typing
import sympy

import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols  # type: ignore

if typing.TYPE_CHECKING:
    from typing import Any
    from matplotlib.axes import Axes
    from matplotlib.figure import Figure
    from matplotlib.gridspec import GridSpec
    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    """Plot exact y = cos(x)"""
    x: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 1000, dtype=np.float_)
    ax.plot(x, np.cos(x), label="Exact")

    # fmt: off
    # Plot Newton's Expansion for cos(x)
    ax.plot(x, 1 - (1 / 2) * np.power(x, 2) / 2  + (1 / 24) * np.power(x, 4)
        - (1 / 720) * np.power(x, 6) + (1 / 362880) * np.power(x, 9),
        label="Newton (5 terms)",
    )
    # fmt: on

    # Plot Taylor Series for cos(x)
    num_terms = 5
    xs: Any = symbols("x")
    poly: Any = sympy.cos(xs).series(xs, 0, num_terms).removeO()  # type: ignore
    eqn: Any = sympy.lambdify(xs, poly.as_expr(), modules="numpy")
    print(f"Taylor Series for cos(x) = {poly}")
    ax.plot(x, eqn(x), label=f"Taylor ({num_terms} terms)")

    # Plot Euler's Method for d[cos(x)] = -sin(x)
    xm: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 20, dtype=np.float_)
    ym: NDArray[np.float_] = np.zeros(len(xm), dtype=np.float_)
    dx: np.float_ = xm[1] - xm[0]
    ym[0] = np.cos(0)
    for i in range(1, len(xm)):
        ym[i] = ym[i - 1] - np.sin(xm[i - 1]) * dx
    ax.plot(xm, ym, label="Euler (20 terms)")

    ax.set_title(r"Taylor Series for $y = \cos(x)$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim(-1.1, 1.1)
    ax.axhline(y=0.0, color="lightgray", zorder=-2)
    ax.legend(loc="lower left")


def main() -> None:
    fig: Figure = plt.figure(os.path.basename(sys.argv[0]))
    gs: GridSpec = fig.add_gridspec(1, 1)
    ax: Axes = fig.add_subplot(gs[0, 0])# type: ignore
    plot(ax)# type: ignore
    plt.show()


if __name__ == "__main__":
    main()
