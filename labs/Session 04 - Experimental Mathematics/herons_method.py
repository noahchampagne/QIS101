#!/usr/bin/env python3
"""herons_method.py"""

import random

EPSILON: float = 10e-8


def heron(num: float) -> float:
    """Used heron's method to hone in on a value within EPSILON of the numbers square"""
    guess: float = num / 2
    while not ((guess + EPSILON) ** 2 > num) or not ((guess - EPSILON) ** 2 < num):
        guess = (num / guess + guess) / 2
    return guess


def main() -> None:
    s: float = random.randint(1_000_000, 2_000_000)
    print(f"s = {s:,} | r = {heron(s):,.8f}")


if __name__ == "__main__":
    main()
