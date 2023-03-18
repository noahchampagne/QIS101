#!/usr/bin/env python3
"""plot_multigraphs.py"""

from __future__ import annotations

import os
import sys
import typing

import matplotlib.pyplot as plt
import plot_parabola
import plot_polynomial
import plot_rings
import plot_rose_curves

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from matplotlib.figure import Figure
    from matplotlib.gridspec import GridSpec

def main() -> None:
    fig: Figure = plt.figure(os.path.basename(sys.argv[0]))
    gs: GridSpec = fig.add_gridspec(2, 2)

    ax: Axes = fig.add_subplot(gs[0, 0])
    plot_parabola.plot(ax)

    ax = fig.add_subplot(gs[0, 1])
    plot_polynomial.plot(ax)

    ax = fig.add_subplot(gs[1, 0])
    plot_rings.plot(ax)

    ax = fig.add_subplot(gs[1, 1], projection="polar")
    plot_rose_curves.plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
