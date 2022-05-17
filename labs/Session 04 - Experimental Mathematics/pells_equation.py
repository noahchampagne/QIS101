#!/usr/bin/env python3
# pells_equation.py

import math
import numba as nb


@nb.njit(locals={"x": nb.uint64, "y": nb.uint64})
def pell_solution(n):
    x = 1
    while x < 70_000:
        x2 = x * x
        y = 1
        y_max = math.floor(math.sqrt((x2 - 1) / n))
        while y <= y_max:
            y2 = y * y
            if x2 - n * y2 == 1:
                return x, y
            y += 1
        x += 1
    return None, None


def main():
    print(f"{'n':>4}{'x':>8}{'y':>8}")
    print(f"{'='*3:>4}{'='*6:>8}{'='*6:>8}")

    for n in range(2, 71):
        x, y = pell_solution(n)
        if x == None:
            print(f"{n:>4}{'-':>8}{'-':>8}")
        else:
            print(f"{n:>4}{x:>8}{y:>8}")


if __name__ == "__main__":
    main()
