#!/usr/bin/env python3
"""plot_polynomial.py"""

from __future__ import annotations

import os
import sys
import typing

import matplotlib.pyplot as plt
import numpy as np
from sympy import Derivative, Poly, Symbol, Expr, FunctionClass
from sympy import lambdify, latex, real_roots, symbols  # type: ignore

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from matplotlib.figure import Figure
    from matplotlib.gridspec import GridSpec
    from numpy.typing import NDArray


def plot(ax: plt.Axes) -> None:
    """Plot a polynomial with its zeros and extrema points"""
    # Declare x to be a sympy symbol, not a python variable
    x: Symbol = symbols("x")

    # Declare the polynomial "fn" by providing the coefficients
    # of each term in in decreasing (exponent) order
    fn_sym: Poly = Poly([1, -2, -120, 22, 2119, 1980], x)  # type: ignore

    # Find the real-only roots of the polynomial
    # and store in a numpy array of floats
    fn_zeros: NDArray[np.float_] = np.asarray(
        [float(r) for r in real_roots(fn_sym)]  # type: ignore
    )

    # Find the symbolic first derivative of "fn" and locate the real-only
    # zeros of this derivative to find the extrema (tangent) points
    fn_d1: Derivative = Derivative(fn_sym, x, evaluate=True)
    fn_d1_zeros: NDArray[np.float_] = np.asarray(
        [float(r) for r in real_roots(fn_d1)]  # type: ignore
    )

    # Combine the zeros of "fn" and the zeros of the derivative of "fn" into a
    # a single numpy array, then sort that array in increasing order. This array
    # now contains the x-coordinate of interesting points in the "fn" polynomial
    x_pts: NDArray[np.float_] = np.sort(np.concatenate((fn_zeros, fn_d1_zeros)))

    # Get the minimum and maximum of the interesting points array
    x_min: float
    x_max: float
    x_min, x_max = x_pts[0] - 1, x_pts[-1] + 1
    print(f"x_min = {x_min:.4f}, x_max = {x_max:.4f}")

    x_vec: NDArray[np.float_] = np.linspace(x_min, x_max, 1000, dtype=np.float_)

    # Label the graph and draw (0,0) axis lines
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.axhline(0, color="gray")
    ax.axvline(0, color="gray")

    # Create a numpy callable (numeric) function from the symbolic "fn" polynomial
    fn_expr: Expr = fn_sym.as_expr()  # type: ignore
    fn_lambda: FunctionClass = lambdify(x, fn_expr, modules="numpy")  # type: ignore

    ax.plot(x_vec, fn_lambda(x_vec), linewidth=2)

    # Plot the zeros and derivative roots on the line graph
    ax.scatter(fn_zeros, fn_lambda(fn_zeros), color="red")
    ax.scatter(fn_d1_zeros, fn_lambda(fn_d1_zeros), color="green")

    # Set the graph title to the polynomial expressed in LaTeX format
    ax.set_title(f"$y = {latex(fn_expr)}$")


def main() -> None:
    fig: Figure = plt.figure(os.path.basename(sys.argv[0]))
    gs: GridSpec = fig.add_gridspec(1, 1)
    ax: Axes = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
