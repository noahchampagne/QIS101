#!/usr/bin/env python3
"""big_sqrt.py"""

# From http://mpmath.org
from mpmath import mp, mpf, nstr


def square_root(x: float):
    """Return square root of x using Newton's Method"""
    low_end = mpf(0.0)
    high_end = mpf(x)

    estimate = mpf((high_end + low_end) / 2)
    estimate_squared = estimate * estimate

    epsilon = mpf(1e-14)

    while abs(estimate_squared - x) > epsilon:
        if estimate_squared > x:
            high_end = estimate
        else:
            low_end = estimate

        estimate = (high_end + low_end) / 2
        estimate_squared = estimate * estimate

        if high_end == low_end:
            break

    return estimate


def main():
    mp.dps = 200  # dps = decimal places

    x = mpf(
        "335903513812618226222181638735285568136989476656876"
        "15688767589021060440979380129292322236643684251591"
    )

    x_sqrt = square_root(x)

    print(f"Estimated square root of \n {x}")
    print(f"is \n {nstr(x_sqrt, 100)}")


if __name__ == "__main__":
    main()
