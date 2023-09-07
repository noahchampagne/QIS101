#!/usr/bin/env python3
"""circle_area.py"""

from __future__ import annotations

import typing

import numpy as np
import scipy.integrate  # type: ignore

if typing.TYPE_CHECKING:
    from typing import Callable


def f(x: float) -> float:
    """This is the function we are numerically integrating"""
    return float(4 * np.sqrt(1 - x**2))


def F(x: float) -> float:
    """This is the exact analytic integral of our function"""
    return float(2 * (x * np.sqrt(1 - x**2) + np.arcsin(x)))


# fmt: off
def left_hand_rule(func: Callable[[float], float],
                   a: float, b: float, intervals: int) -> float:  # fmt: on
    """Numerically estimate the integral of func() in [a,b] using the left-hand rule"""
    dx: float = (b - a) / intervals
    area: float = 0.0
    for i in range(0, intervals):
        area += func(a + i * dx)
    return dx * area

# fmt:off
def simpsons_rule(func: Callable[[float], float],
                  a: float, b: float, intervals: int) -> float:  # fmt: on
    """Numerically estimate the integral of func() in [a,b] using Simpson's rule"""
    dx: float = (b - a) / intervals
    area: float = func(a) + func(b)
    for i in range(1, intervals):
        area += func(a + i * dx) * (2 * (i % 2 + 1))
    return dx / 3 * area


def main() -> None:
    a: float = 0.0
    b: float = 1.0
    intervals: int = int(1e6)

    print("Integrating 4 * sqrt(1 - x^2)", end=" ")
    print(f"over [{a}, {b}] using {intervals:,} intervals")

    area_act: float = F(b) - F(a)
    print(f"Analytic (Exact) : {area_act:.14f}\n")

    area_lh: float = left_hand_rule(f, a, b, intervals)
    print(f"Left-hand Rule   : {area_lh:.14f}")
    print(f"% Relative Error : {abs((area_lh - area_act) / area_act):.14%}\n")

    area_simpsons: float = simpsons_rule(f, a, b, intervals)
    print(f"Simpson's Rule   : {area_simpsons:.14f}")
    print(f"% Relative Error : {abs((area_simpsons - area_act) / area_act):.14%}\n")

    area_scipy: float = scipy.integrate.quad(f, a, b)[0]
    print(f"SciPy's quad()   : {area_scipy:.14f}")
    print(f"% Relative Error : {abs((area_scipy - area_act) / area_act):.14%}\n")


if __name__ == "__main__":
    main()
