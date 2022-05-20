#!/usr/bin/env python3
# dirichlet_function.py

import mpmath

mpmath.mp.dps = 2000  # dps = decimal places
k = 100
n = 1e10


def dirichlet_function(x):
    d = mpmath.power(mpmath.cos(mpmath.factorial(k) * mpmath.pi * x), n)
    return mpmath.chop(d)


def main():
    print(dirichlet_function(2))
    print(dirichlet_function(2.5))
    print(dirichlet_function(mpmath.sqrt(2)))
    print(dirichlet_function(mpmath.e))


if __name__ == "__main__":
    main()
