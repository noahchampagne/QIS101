#!/usr/bin/env python3
"""quadratic_regression.py"""


from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def fit_quadratic(
    vec_x: NDArray[np.float_], vec_y: NDArray[np.float_]
) -> tuple[float, float, float]:
    sum_x: float = sum(vec_x)
    sum_x2: float = sum(vec_x**2)
    sum_x3: float = sum(vec_x**3)
    sum_x4: float = sum(vec_x**4)

    sum_y: float = sum(vec_y)
    sum_xy: float = sum(vec_x * vec_y)
    sum_x2y: float = sum(vec_x**2 * vec_y)

    coeffs: NDArray[np.float_] = np.array(
        [[sum_x4, sum_x3, sum_x2], [sum_x3, sum_x2, sum_x], [sum_x2, sum_x, len(vec_x)]]
    )

    vals: NDArray[np.float_] = np.array([sum_x2y, sum_xy, sum_y])

    det_coeffs: float = np.linalg.det(coeffs)

    mat_a: NDArray[np.float_] = np.copy(coeffs)
    mat_a[:, 0] = vals
    det_a: float = np.linalg.det(mat_a)

    mat_b: NDArray[np.float_] = np.copy(coeffs)
    mat_b[:, 1] = vals
    det_b: float = np.linalg.det(mat_b)

    mat_c: NDArray[np.float_] = np.copy(coeffs)
    mat_c[:, 2] = vals
    det_c: float = np.linalg.det(mat_c)

    a: float = det_a / det_coeffs
    b: float = det_b / det_coeffs
    c: float = det_c / det_coeffs

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

    x: NDArray[np.float_] = np.linspace(np.min(vec_x), np.max(vec_x), 1000)

    a: float
    b: float
    c: float
    a, b, c = fit_quadratic(vec_x, vec_y)
    ax.plot(x, a * x**2 + b * x + c, label="Quadratic")

    print(f"y = ({a:.4f})x^2 + ({b:.4f})x + ({c:.4})")
    print(f"Tape counter at 65 mins = {f(a, b, c, 6.5):,.4f}")

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
