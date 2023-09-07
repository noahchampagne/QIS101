#!/usr/bin/env python3
"""archimedes_spiral.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate  # type: ignore

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def find_distance(start: float, end: float) -> float:
    """Returns the arc length of an archimedes spiral"""
    return scipy.integrate.quad(lambda x: x, start, end)[0]  # type: ignore


def plot(ax: Axes) -> None:
    """Draw an archimedes spiral where radius is a function of theta"""
    # Solves for the points of the archimedes spiral
    theta: NDArray[np.float_] = np.linspace(0, 8 * np.pi, 1000, dtype=np.float_)
    radius: NDArray[np.float_] = theta

    ax.plot(theta, radius, color="blue")

    ax.set_title("Archimedes Spiral from angle 0 -> 8*pi")
    ax.set_aspect("equal")


def main() -> None:
    # Finds the distance of the archimedes spiral
    length: float = find_distance(0, 8 * np.pi)
    print(f"The arc length of an Archimedes Spiral from angel 0 -> 8*pi = {length:.4f}")

    # Plots the archimedes spiral
    plt.figure(__file__)
    plot(plt.axes(projection="polar"))
    plt.show()


if __name__ == "__main__":
    main()
