#!/usr/bin/env python3
"""pells_equation.py"""

from math import floor, sqrt
from numba import njit


@njit()
def pell_solution(n: int) -> tuple[bool, int, int]:
    """
    Returns minimal positive (x,y) integer solution to
    x^2 + n*y^2 == 1 or False if no solution is found
    """
    x = 1
    while x < 70_000:
        x2 = x * x
        y = 1
        y_max = floor(sqrt((x2 - 1) / n))
        while y <= y_max:
            y2 = y * y
            if x2 - n * y2 == 1:
                return True, x, y
            y += 1
        x += 1
    return False, 0, 0


def main():
    print(f"{'n':>4}{'x':>8}{'y':>8}")
    print(f"{'='*3:>4}{'='*6:>8}{'='*6:>8}")

    for n in range(2, 71):
        solution_exists, x, y = pell_solution(n)
        if solution_exists:
            print(f"{n:>4}{x:>8}{y:>8}")
        else:
            print(f"{n:>4}{'-':>8}{'-':>8}")


if __name__ == "__main__":
    main()
