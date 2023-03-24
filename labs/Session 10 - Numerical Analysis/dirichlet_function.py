#!/usr/bin/env python3
"""dirichlet_function.py"""

from __future__ import annotations

import typing
import mpmath  # type: ignore

if typing.TYPE_CHECKING:
    from typing import Any

mpmath.mp.dps = 2000  # dps = decimal places


def dirichlet_function(x: Any) -> Any:
    k: float = 100.0
    n: float = 1e10
    val: Any = mpmath.power(
        mpmath.cos(mpmath.factorial(k) * mpmath.pi * x), n  # type: ignore
    )
    val = mpmath.chop(val)
    return val


def main() -> None:
    print(f"f(2) = {dirichlet_function(2)}")
    print(f"f(2.5) = {dirichlet_function(2.5)}")
    print(f"f(sqrt(2)) = {dirichlet_function(mpmath.sqrt(2))}")  # type: ignore
    print(f"f(e) = {dirichlet_function(mpmath.e)}")


if __name__ == "__main__":
    main()
