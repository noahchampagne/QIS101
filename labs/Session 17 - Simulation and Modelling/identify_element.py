#!/usr/bin/env/python 3
"""identify_element.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def solve_element(temp: float, volume: float) -> None:
    """Uses PV = nRT with known values to solve for number of mols which helps find what element"""
    pressure: float = 2.0 * 101_325
    r: float = 8.31
    mass: float = 50.0
    mols: float = (pressure * volume) / (r * temp)
    molar_mass: float = mass / mols
    print(f"The element has a molar mass of {molar_mass}g / mol making it Argon!")


def fit_linear(
    vec_x: NDArray[np.float_], vec_y: NDArray[np.float_]
) -> tuple[float, float]:
    """Dave's linear regression function using sklearn"""
    vec_x = vec_x[:, np.newaxis]  # Make vec_x a "column" vector (now a 2D matrix)
    model: LinearRegression = LinearRegression().fit(vec_x, vec_y)
    m: float = float(model.coef_[0])
    b: float = float(model.intercept_)  # type: ignore
    return m, b


def plot(ax: Axes) -> None:
    """Plots the temperature vs volume and its line of best fit"""
    # Plots the inputted data
    temps: NDArray[np.float_] = np.linspace(223.15, 423.15, 5)
    volumes: NDArray[np.float_] = np.array([11.6, 14, 16.2, 19.4, 21.8])
    ax.plot(temps, volumes / 1000, label="Real Data")

    # Plots the line of best fit
    m, b = fit_linear(temps, volumes)

    ax.plot(
        temps,
        (m * temps + b) / 1000,
        label=f"Linear Regression (y = {m:.02f}x - {-b:.02f})",
        linestyle="dashed",
    )

    # Sets graph details
    ax.set_title("Temp vs Volume for Unknown Element")
    ax.set_xlabel("$Temperature (K)$")
    ax.set_ylabel("$Volume (m^3)$")
    ax.legend()

    # Solves for the element
    solve_element(temps[0], m * temps[0] + b)


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
