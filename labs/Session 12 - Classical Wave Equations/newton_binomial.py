#!/usr/bin/env python3
"""newton_binomial.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from sympy import Float, Number, lambdify, symbols  # type: ignore

if typing.TYPE_CHECKING:
    from typing import Any

    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def expr_to_str(expr: Any, num_digits: int) -> Any:
    """
    Returns a string representation of the given polynomial expression
    rounding each coefficient to fractional part with num_digits precision
    """
    return expr.xreplace(
        {
            n.evalf(): n if type(n) == int else Float(n, num_digits)  # type: ignore
            for n in expr.atoms(Number)
        }
    )


def calc_coeff(a: int, b: int, r: float, n: int) -> float:
    """
    Returns the coefficient for the nth term in the Binomial expansion of (a+b)^r
    """
    coeff: float = 1.0
    for m in range(n):
        coeff = coeff * (r - m) / (m + 1)
    coeff = coeff * pow(a, r - n)
    coeff = coeff * pow(b, n)
    return coeff


def binomial_expand(a: int, b: int, c: int, r: float, max_t: int) -> tuple[Any, Any]:
    """
    Returns a tuple containing the Binomial Expansion of (a+b*x^c)^r
    to max_t terms as a Sympy Polynomial in x along with
    a callable Numpy expression for that expansion
    """
    x: Any = symbols("x")
    poly: float = 0.0
    for t in range(max_t):
        # Append this term (as a symbolic expression in x)
        # to the growing polynomial of max_t terms
        poly += calc_coeff(a, b, r, t) * x ** (c * t)
        print(poly)
        input()
    return poly, lambdify(x, poly.as_expr(), modules="numpy")  # type: ignore


def plot(ax: Axes) -> None:
    x: NDArray[np.float_] = np.linspace(0, 10, 1000, dtype=np.float_)

    ax.plot(x, 1 / np.power(2 * np.power(x, 2) + 7, 2 / 3), label="Exact")

    print(f"{'Terms':>5}   Binomial Expansion")
    for t in range(2, 8):
        # Use Newton's Binomial Theorem to expand (2x^2+7)^(-2/3) to 't' terms
        eqn: tuple[Any, Any] = binomial_expand(7, 2, 2, -2 / 3, t)
        print(f"{t:>5} = {expr_to_str(eqn[0], 5)}")
        # Evaluate the symbolic expression across the domain x=[0, 10]
        ax.plot(x, np.array(list(map(eqn[1], x))), label=f"{t} terms")

    ax.set_title(r"Binomial Expansion of $y=(2x^2+7)^{-2/3}$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim(0, 0.3)
    ax.legend(loc="upper right")


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
