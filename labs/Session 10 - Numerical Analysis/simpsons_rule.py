#!/usr/bin/env python3
"""simpsons_rule.py"""

from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from typing import Callable


def f(x: float) -> float:
    """This is the function we are numerically integrating"""
    return (x + 9) * (x + 4) * (x + 1) * (x - 5) * (x - 11)


def F(x: float) -> float:
    """This is the exact analytic integral of our function"""
    # fmt: off
    return (1 / 6 * pow(x, 6) - 2 / 5 * pow(x, 5) - 30 * pow(x, 4)
                + 22 / 3 * pow(x, 3) + 2119 / 2 * pow(x, 2) + 1980 * x)
    # fmt: on


# fmt: off
def left_hand_rule(func: Callable[[float], float],
                   a: float, b: float, intervals: int) -> float:  # fmt: on
    """Numerically estimate the integral of func() using the left-hand rule"""
    dx: float = (b - a) / intervals
    area: float = 0.0
    for i in range(0, intervals):
        area += func(a + i * dx)
    return dx * area

# fmt: off
def simpsons_rule(func: Callable[[float], float],
                  a: float, b: float, intervals: int) -> float:  # fmt:on
    """Numerically estimate the integral of func() using Simpson's rule"""
    dx: float = (b - a) / intervals
    area: float = func(a) + func(b)
    for i in range(1, intervals):
        area += func(a + i * dx) * (2 * (i % 2 + 1))
    return dx / 3 * area


def main() -> None:
    a: float
    b: float
    a, b = -10.0, 12.0
    intervals: int = int(1e6)

    print("Integrating x^5 - 2x^4 - 120x^3 + 22x^2 + 2199x + 1980")
    print(f" over [{a}, {b}] using {intervals:,} intervals\n")

    area_act = F(b) - F(a)
    print(f"Analytic (Exact) : {area_act:.14f}\n")

    area_lh = left_hand_rule(f, a, b, intervals)
    print(f"Left-hand Rule   : {area_lh:.14f}")
    print(f"% Relative Error : {abs((area_lh - area_act) / area_act):.14%}\n")

    area_simpsons = simpsons_rule(f, a, b, intervals)
    print(f"Simpson's Rule   : {area_simpsons:.14f}")
    print(f"% Relative Error : {abs((area_simpsons - area_act) / area_act):.14%}")


if __name__ == "__main__":
    main()
