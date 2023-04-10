#!/usr/bin/env python3
"""kinematics_regression.py"""


from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from pathlib import Path

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def fit_quadratic(
    vec_x: NDArray[np.float_], vec_y: NDArray[np.float_]
) -> tuple[float, float, float]:
    vec_x = vec_x[:, np.newaxis]  # Make vec_x a "column" vector (now a 2D matrix)
    transformer = PolynomialFeatures(degree=2, include_bias=False)
    transformer.fit(vec_x)
    # The matrix vec_x2 has two columns: the original x values and now x**2 values
    vec_x2: NDArray[np.float_] = np.array(transformer.transform(vec_x))  # type: ignore
    lr = LinearRegression()
    model: LinearRegression = lr.fit(vec_x2, vec_y)  # Notice we use vec_x2
    a: float = model.coef_[1]
    b: float = model.coef_[0]
    c = float(model.intercept_)  # type: ignore
    return a, b, c


def plot(ax: Axes) -> None:
    data_file: Path = Path(__file__).parent.joinpath("kinematics_regression.csv")
    data: NDArray[np.float_] = np.genfromtxt(data_file, delimiter=",")

    vec_x: NDArray[np.float_] = data[:, 0]
    vec_y: NDArray[np.float_] = data[:, 1]

    a: float
    b: float
    c: float
    a, b, c = fit_quadratic(vec_x, vec_y)

    acceleration: float = a * 2
    initial_velocity: float = b

    print(f"Constant acceleration = {acceleration:.4f} m/s^2")
    print(f"     Initial velocity = {initial_velocity:.4f} m/s")

    min_x:float = float(np.min(vec_x))
    max_x:float = float(np.max(vec_x))
    x: NDArray[np.float_] = np.linspace(min_x, max_x, 1000)

    ax.plot(x, a * x**2 + b * x + c)
    ax.scatter(vec_x, vec_y, color="red")

    ax.set_title("Newtonian Kinematics")
    ax.set_xlabel("Time (sec)")
    ax.set_ylabel("Distance (m)")


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
