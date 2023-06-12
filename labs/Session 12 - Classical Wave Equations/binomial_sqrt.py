#!/usr/bin/env python3
"""binomial_sqrt.py"""

from __future__ import annotations

import typing
from math import pow

from sympy import Float, Number, lambdify, symbols  # type: ignore

if typing.TYPE_CHECKING:
    from typing import Any


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
    return poly, lambdify(x, poly.as_expr(), modules="numpy")  # type: ignore


def heron(s: float) -> tuple[int, float]:
    """
    Returns a tuple containing the number of iterations of Heron's Method
    to calculate sqrt(s) to 1e-14 along with the actual root value
    """
    x: float = s / 2
    t = 1
    while x**2 - s > 1e-14:
        x = (s / x + x) / 2
        t += 1
    return t, x


def main() -> None:
    print(f"{'Terms':>5}{'Estimate':>18}{'Binomial Expansion':>21}")
    for t in range(1, 21):
        eqn: tuple[Any, Any] = binomial_expand(1, -1, 1, 1 / 2, t)
        # Evaluate the symbolic expression at x = 2/9
        print(f"{t:>5}  {3 * eqn[1](2/9):.14f}", end="")
        if t < 8:
            print(f" = 3*({expr_to_str(eqn[0], 5)})", end=" ")
        print()

    # Compare the Binomial Expression convergence rate to Heron's Method
    t, x = heron(7)
    print("Heron's Method")
    print(f"{t:>5}  {x:.14f}", end="")


if __name__ == "__main__":
    main()
