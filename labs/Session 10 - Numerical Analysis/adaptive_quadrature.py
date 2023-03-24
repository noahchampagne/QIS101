#!/usr/bin/env python3
"""adaptive_quadrature.py"""

import time


def f(x: float) -> float:
    """This is the function we are numerically integrating"""
    return 5 * pow(x, 3) - 9 * pow(x, 2) + 11


def F(x: float) -> float:
    """This is the exact analytic integral of our function"""
    return 5 * pow(x, 4) / 4 - 3 * pow(x, 3) + 11 * x


def midpoint_fixed(a: float, b: float) -> float:
    x: float = a
    dx: float = (b - a) / 1e6
    area: float = 0.0
    while x < b:
        area += f(x + dx / 2) * dx
        x += dx
    return area


def midpoint_adaptive(a: float, b: float) -> float:
    x: float = a
    dx: float = 1.0
    area: float = 0.0
    while x < b:
        f1: float = f(x)
        f2: float = f(x + dx)
        # Keep halving dx if current delta is too great
        while abs(((f2 - f1) / f1)) > 1e-3:
            dx /= 2
            f2 = f(x + dx)
        # Use the midpoint rule
        area += f(x + dx / 2) * dx
        x += dx
        # Expand current interval width
        dx *= 2
    return area


def main() -> None:
    a: float = 0.0
    b: float = 10.0

    area_actual: float = F(b) - F(a)
    print(f"\nExact integral using analytic calculus = {area_actual}")
    print()

    start_time: float = time.process_time()
    area_fixed: float = midpoint_fixed(a, b)
    elapsed_time: float = time.process_time() - start_time
    rel_err: float = abs((area_fixed - area_actual) / area_actual)
    print(f"Estimated integral using fixed width midpoint rule = {area_fixed}")
    print(f"Fixed width midpoint rule % relative error = {rel_err:.8%}")
    print(f"Time (sec) Fixed = {elapsed_time:.3f}")
    print()

    start_time = time.process_time()
    area_adaptive: float = midpoint_adaptive(a, b)
    elapsed_time = time.process_time() - start_time
    rel_err = abs((area_adaptive - area_actual) / area_actual)
    print(f"Estimated integral using adaptive width midpoint rule = {area_adaptive}")
    print(f"Adaptive width midpoint rule % relative error = {rel_err:.8%}")
    print(f"Time (sec) Adaptive = {elapsed_time:.3f}")
    print()


if __name__ == "__main__":
    main()
