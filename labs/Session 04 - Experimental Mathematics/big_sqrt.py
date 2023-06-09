#!/usr/bin/env python3
"""big_sqrt.py"""

from __future__ import annotations

import typing

# From http://mpmath.org
from mpmath import mp, mpf, nstr  # type: ignore


if typing.TYPE_CHECKING:
    from typing import Any


def square_root(x: Any) -> Any:
    """Return square root of x using Newton's Method"""
    low_end: Any = mpf(0.0)
    high_end: Any = mpf(x)

    estimate: Any = mpf((high_end + low_end) / 2)
    estimate_squared: Any = estimate * estimate

    epsilon: Any = mpf(1e-14)

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


def main() -> None:
    mp.dps = 200  # dps = decimal places

    x: Any = mpf(
        (
            "33590351381261822622218163873528556813698947665687"
            "61568876758902106044097938012929232223664368425159"
        )
    )

    x_sqrt: Any = square_root(x)

    print(f"Estimated square root of \n {x}")
    print(f"is \n {nstr(x_sqrt, 100)}")


if __name__ == "__main__":
    main()
