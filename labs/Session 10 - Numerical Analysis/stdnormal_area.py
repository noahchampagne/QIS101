#!/usr/bin/env python3
"""stdnormal_area.py"""

import numpy as np
import scipy.integrate  # type: ignore


def f(x: float) -> float:
    return float(1 / np.sqrt(2 * np.pi) * np.exp(-(x**2) / 2))


def main() -> None:
    integral: float = scipy.integrate.quad(f, -1, 1)[0]

    # See https://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7_rule
    print(f"Normal CDF: Probability X is within ± 1st sigma = {integral:.5%}")


if __name__ == "__main__":
    main()
