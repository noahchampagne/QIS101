#!/usr/bin/env python3
# dirichlet_function.py

import mpmath

mpmath.mp.dps = 2000  # dps = decimal places


def dirichlet_function(x):
    k = 100
    n = 1e10
    f = mpmath.power(mpmath.cos(mpmath.factorial(k) * mpmath.pi * x), n)
    return mpmath.chop(f)


def main():
    print(f"f(2) = {dirichlet_function(2)}")
    print(f"f(2.5) = {dirichlet_function(2.5)}")
    print(f"f(sqrt(2)) = {dirichlet_function(mpmath.sqrt(2))}")
    print(f"f(e) = {dirichlet_function(mpmath.e)}")


if __name__ == "__main__":
    main()
