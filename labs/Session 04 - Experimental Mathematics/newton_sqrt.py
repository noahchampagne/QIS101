#!/usr/bin/env python3
"""newton_sqrt.py"""


def square_root(x: float) -> float:
    """Returns square root of x using Newton's Method"""
    low_end = 0.0
    high_end = x

    estimate = (high_end + low_end) / 2
    estimate_squared = estimate * estimate

    epsilon = 1e-14

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
    x = 168923

    x_sqrt = square_root(x)

    print(f"Estimated square root of \n {x}")
    print(f"is \n {x_sqrt:.14f}")


if __name__ == "__main__":
    main()
