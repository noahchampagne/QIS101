#!/usr/bin/env python3
"""maxwell_boltzmann.py"""
from __future__ import annotations

import typing
import math

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def create_array(a: int) -> None:
    """Plots the probability density for values of x=1 -> x=20 associated with the inputted a value"""
    # Taking 1000 x values and calculating the pdf
    x_vals: NDArray[np.float_] = np.linspace(0, 20, 1000)
    constant: float = math.sqrt(2 / np.pi) / a**3
    # Maxwell-Boltzmann PDF equation
    prob: NDArray[np.float_] = constant * (
        x_vals**2 * (np.exp(-(x_vals**2) / (2 * (a**2))))
    )
    # Plotting
    plt.plot(x_vals, prob, label=f"a={a}")


def plot(ax: Axes) -> None:
    """Plots the probability density for values of x=1 -> x=20 and a=1, a=2, & a=5"""
    create_array(1)
    create_array(2)
    create_array(5)
    plt.xlabel("x")
    plt.ylabel("Probability Density")
    plt.title("Maxwell-Boltzmann Distribution")
    ax.legend()


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
