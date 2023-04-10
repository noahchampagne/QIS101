#!/usr/bin/env python3
"""quadratic_regression_sklearn.py"""


from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

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
    model: LinearRegression = lr.fit(vec_x2, vec_y)
    a: float = model.coef_[1]
    b: float = model.coef_[0]
    c = float(model.intercept_)  # type: ignore
    return a, b, c


def fit_linear(
    vec_x: NDArray[np.float_], vec_y: NDArray[np.float_]
) -> tuple[float, float]:
    vec_x = vec_x[:, np.newaxis]  # Make vec_x a "column" vector (now a 2D matrix)
    model: LinearRegression = LinearRegression().fit(vec_x, vec_y)
    m: float = float(model.coef_[0])
    b: float = float(model.intercept_)  # type: ignore
    return m, b


def f(a: float, b: float, c: float, x: float) -> float:
    return a * x**2 + b * x + c


def plot(ax: Axes) -> None:
    vec_x: NDArray[np.float_] = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    vec_y: NDArray[np.float_] = np.array([205, 430, 677, 945, 1233, 1542, 1872, 2224])

    min_x: float = float(np.min(vec_x))
    max_x: float = float(np.max(vec_x))
    x: NDArray[np.float_] = np.linspace(min_x, max_x, 1000)

    a: float
    b: float
    c: float
    a, b, c = fit_quadratic(vec_x, vec_y)
    ax.plot(x, a * x**2 + b * x + c, label="Quadratic")

    print(f"y = ({a:.4f})x^2 + ({b:.4f})x + ({c:.4})")
    print(f"Tape counter at 65 mins = {f(a,b,c,6.5):,.4f}")

    m: float
    m, b = fit_linear(vec_x, vec_y)
    ax.plot(x, m * x + b, label="Linear")

    ax.scatter(vec_x, vec_y, color="red")

    ax.set_title("Tape Counter Per Minute")
    ax.set_xlabel("Elapsed time x10 (min)")
    ax.set_ylabel("Tape Counter")
    ax.legend()


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
