#!/usr/bin/env python3
"""lattice_circle.py"""

# See https://en.wikipedia.org/wiki/Gauss_circle_problem

import math
from numba import njit  # type: ignore

@njit  # type: ignore
def lattice_points(radius:int) -> int:
    num_points:int = 0
    radius_squared:int = radius**2
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            if x**2 + y**2 <= radius_squared:
                num_points += 1
    return num_points


def main() -> None:
    for radius in range(1000, 10001, 1000):
        act_points:int = lattice_points(radius)
        est_points:int = int(math.pi * radius**2 + 2 * math.sqrt(2 * math.pi * radius))
        print((
            f"Radius = {radius:>6,}"
            f"  Act Points = {act_points:>12,}"
            f"  Est Points = {est_points:>12,}"
            f"  % Rel. Err = {(act_points - est_points)/est_points:0.4%}"
        ))


if __name__ == "__main__":
    main()
