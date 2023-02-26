#!/usr/bin/env python3
"""std_continued_fractions.py"""

import math

MAX_TERMS = 20


def normalize_cf(std_cf: list[int]) -> list[int]:
    """Drops any final 1 term by increasing the new final term by 1"""
    while True:
        if len(std_cf) > 2:
            if std_cf[-1] == 1 and std_cf[-2] != 1:
                std_cf[-2] += 1
                std_cf.pop(-1)
            else:
                break

    return std_cf


def encode_cf(x: float) -> list[int]:
    """Returns the standard continued fraction encoding of decimal x"""
    std_cf: list = []
    while len(std_cf) < MAX_TERMS:
        std_cf.append(math.floor(x))
        x = x - math.floor(x)
        if x < 1e-11:
            break
        x = 1 / x
    return normalize_cf(std_cf)


def decode_cf(std_cf) -> float:
    """Returns the decimal encoded by the given standard continued fraction"""
    h_n, k_n = 0, 0
    b_1, h_1, k_1 = 1, 1, 0
    h_2, k_2 = 0, 1
    for term in std_cf:
        a_n, b_n = term, 1
        h_n = a_n * h_1 + b_1 * h_2
        k_n = a_n * k_1 + b_1 * k_2
        b_1 = b_n
        h_1, h_2 = h_n, h_1
        k_1, k_2 = k_n, k_1
    return h_n / k_n


def eval_cf(x: float):
    """Encodes and decodes decimal x as a standard continued fraction"""
    std_cf = encode_cf(x)
    x2 = decode_cf(std_cf)
    print(f"{x} -> {std_cf} -> {x2}")


def main():
    eval_cf(3.245)
    eval_cf(math.sqrt(2))
    eval_cf(math.sqrt(113))

    golden_ratio = (1 + math.sqrt(5)) / 2
    eval_cf(golden_ratio)


if __name__ == "__main__":
    main()
