#!/usr/bin/env python3
"""ellipse_perimeter.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad  # type: ignore
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def d_s(theta: float, a: float, b: float) -> float:
    return float(
        np.sqrt(np.power(a * np.sin(theta), 2) + np.power(b * np.cos(theta), 2))
    )


def ramanujan_estimate(a: float, b: float) -> float:
    h: float = (a - b) / (a + b)
    return float((a + b) * (1 + 3 * h / (10 + np.sqrt(4 - 3 * h))) * np.pi)


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


def plot_p(ax: Axes, p: NDArray[np.float_], r: NDArray[np.float_]) -> None:
    ax.plot(range(len(p)), p, label="Integral")
    ax.plot(range(len(r)), r, label="Ramanujan")
    ax.set_title("Numerical Ellipse Perimeter Estimate")
    ax.set_xlabel("b")
    ax.set_ylabel("Perimeter")
    ax.legend(loc="best")
    ax.set_xlim(1, len(p) - 1)


def plot_err(ax: Axes, e: NDArray[np.float_]) -> None:
    ax.scatter(range(len(e)), e, color="red")
    ax.set_title("Ramanujan's Estimate Relative Error")
    ax.set_xlabel("b")
    ax.set_ylabel("Relative Error")
    ax.set_xlim(1, len(e) - 1)


def plot_fit(ax: Axes, e: NDArray[np.float_], fa: float, fb: float, fc: float) -> None:
    ax.scatter(range(len(e)), e, color="red")
    x: NDArray[np.float_] = np.linspace(0, len(e) - 1, 500)
    ax.plot(x, fa * x**2 + fb * x + fc)  # type: ignore
    ax.set_title("Ramanujan's Error (Quadratic Fit)")
    ax.set_xlabel("b")
    ax.set_ylabel("Relative Error")
    ax.set_xlim(1, len(e) - 1)


def plot_fix(ax: Axes, p: NDArray[np.float_], f: NDArray[np.float_]) -> None:
    ax.plot(range(len(p)), p, label="Integral")
    ax.plot(range(len(f)), f, label="Adjusted")
    ax.set_title("Ramanujan's Perimeter Estimate (Adjusted)")
    ax.set_xlabel("b")
    ax.set_ylabel("Perimeter")
    ax.legend(loc="best")
    ax.set_xlim(1, len(f) - 1)


def main() -> None:
    a = 100
    peri: NDArray[np.float_] = np.zeros(21)
    ram: NDArray[np.float_] = np.zeros(21)
    err: NDArray[np.float_] = np.zeros(21)
    adj: NDArray[np.float_] = np.zeros(21)

    for b, _ in enumerate(peri):
        peri[b] = quad(d_s, 0, 2 * np.pi, args=(a, b))[0]  # type: ignore
        ram[b] = ramanujan_estimate(a, b)
        err[b] = np.abs((ram[b] - peri[b]) / ram[b])

    fit_a: float
    fit_b: float
    fit_c: float
    fit_a, fit_b, fit_c = fit_quadratic(np.arange(len(err), dtype=np.float_), err)
    print("Quadratic Error Adjuster:")
    print(f"{fit_a:.5f}x^2 + {fit_b:.5f}x + {fit_c:.5f}")

    print(f"{'b':>3}{'Perimeter':>10}{'Ramanujan':>11}{'Error':>10}{'Adjusted':>10}")
    for b, _ in enumerate(peri):
        adj[b] = ram[b] - ram[b] * (fit_a * b**2 + fit_b * b + fit_c)
        print(f"{b:>3}{peri[b]:>10.3f}{ram[b]:>11.3f}{err[b]:>10.6f}{adj[b]:>10.3f}")

    plt.figure(__file__, constrained_layout=True)
    plot_p(plt.subplot(221), peri, ram)
    plot_err(plt.subplot(222), err)
    plot_fit(plt.subplot(223), err, fit_a, fit_b, fit_c)
    plot_fix(plt.subplot(224), peri, adj)
    plt.show()


if __name__ == "__main__":
    main()
