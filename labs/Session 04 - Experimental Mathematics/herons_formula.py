#!/usr/bin/env python3
# herons_formula.py

import numpy as np


def is_triangle(triangle):
    a, b, c = triangle
    return a + b > c and a + c > b and b + c > a


def area(triangle):
    a, b, c = triangle
    s = (a + b + c) / 2
    return np.sqrt(s * (s - a) * (s - b) * (s - c))


def main():
    np.random.seed(2016)
    for n in range(10):
        while not is_triangle(t := np.random.randint(1, 100, 3)):
            continue
        print(f"{t} {area(t):>9.4f}")


if __name__ == "__main__":
    main()
