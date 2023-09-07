#!/usr/bin/env/python 3
"""euler_curve.py"""

from __future__ import annotations
from turtle import width

import typing

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad  # type: ignore

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def f_sin(u: float) -> float:
    """Helper function for sin(x^2)"""
    return float(np.sin(u**2))


def f_cos(u: float) -> float:
    """Helper function for cos(x^2)"""
    return float(np.cos(u**2))


def plot(ax: Axes) -> None:
    """Plots the temperature vs volume and its line of best fit"""
    # Plots the data desires
    times: NDArray[np.float_] = np.linspace(0, 12.34, 1000)
    x_vals: NDArray[np.float_] = np.zeros_like(times)
    y_vals: NDArray[np.float_] = np.zeros_like(times)
    # Estimates the integral using a quadrature
    for i, time in enumerate(times):
        x_vals[i] = quad(f_cos, 0, time)[0]
        y_vals[i] = quad(f_sin, 0, time)[0]
    ax.plot(x_vals, y_vals)

    # Plots a point at a very large value of t
    # Value obtained on Wolfram Alpha bc scipy.quad has too large of an error
    ax.scatter(0.5 * np.sqrt(np.pi / 2), 0.5 * np.sqrt(np.pi / 2), color="red")

    # Sets graph details
    ax.set_title("Euler Curve")
    ax.set_xlabel("x")
    ax.set_ylabel("y")


def f(t: float) -> float:
    """Helper function for arc length"""
    return float(np.sqrt(f_cos(t) ** 2 + f_sin(t) ** 2))


def arc_length(start: float, end: float) -> float:
    """Returns the arc length of an Euler Curve"""
    return quad(f, start, end)[0]  # type: ignore


def main() -> None:
    # Finds the distance of the archimedes spiral
    length: float = arc_length(0, 12.34)
    print(f"The arc length of an Euler Curve from time 0 -> 12.34 = {length:.4f}")

    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
