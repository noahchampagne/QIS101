#!/usr/bin/env python3
"""gen_continued_fractions.py"""

import math

MAX_TERMS = 20


def decode_gencf(a_0, b_0, form: tuple) -> float:
    """Evaluates a generalized continued fraction of the given form"""
    a, b, c, d, e = form
    a_n, b_n = a_0, b_0
    h_n, k_n = 0, 0
    b_1, h_1, k_1 = 1, 1, 0
    h_2, k_2 = 0, 1
    for n in range(1, MAX_TERMS):
        h_n = a_n * h_1 + b_1 * h_2
        k_n = a_n * k_1 + b_1 * k_2
        b_1 = b_n
        h_1, h_2 = h_n, h_1
        k_1, k_2 = k_n, k_1
        a_n = d * n + e
        b_n = a * n * n + b * n + c
    return h_n / k_n


def print_rel_error(estimated: float, actual: float):
    print(f"Est.        : {estimated}")
    print(f"Act.        : {actual}")
    print(f"Rel. % Err  : {(actual - estimated)/actual:.14%}\n")


def main():
    print("Euler's Generalized Continued Fraction for Pi")
    x = decode_gencf(3, 1, (4, 4, 1, 0, 6))
    print_rel_error(x, math.pi)


if __name__ == "__main__":
    main()
