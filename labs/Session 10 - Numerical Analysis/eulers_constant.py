#!/usr/bin/env python3
"""eulers_constant.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def equation(x: float) -> float:
    """Helper equation"""
    return np.log(np.log(1 / x))  # type: ignore


def find_constant(start: float, end: float) -> float:
    """Returns euler's constant through integration"""
    return scipy.integrate.quad(equation, start, end)[0]  # type: ignore


def plot(ax: Axes, constant: float) -> None:
    """Plot teh given equation"""
    # Solves for the points of the graph
    x_vals: NDArray[np.float_] = np.linspace(1e-10, 50, 1000, dtype=np.float_)
    y_vals: NDArray[np.float_] = constant + np.log(x_vals)

    ax.plot(x_vals, y_vals, color="blue")

    # Uses list comprehension to create a np array of the 1st 50 harmonic numbers
    s: float = 0
    harmonics: NDArray[np.float_] = np.array(
        [0] + [s := s + (1 / i) for i in range(1, 50)]
    )
    # Create a step function of those first 50 harmonic numbers
    plt.step(range(1, 51), harmonics, color="red")

    # Gives the plot a title, labels the axes, and limits the y-axis to only positive #'s
    ax.set_title(r"$y = \gamma + \ln(x)$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.set_ylim(0, 5)


def main() -> None:
    # Finds euler's constant!
    constant: float = -find_constant(0, 1)
    print(f"Euler's Constant = {constant:.4f}")

    # Plots the equation and step graph of the harmonics
    plt.figure(__file__)
    plot(plt.axes(), constant)
    plt.show()


if __name__ == "__main__":
    main()
