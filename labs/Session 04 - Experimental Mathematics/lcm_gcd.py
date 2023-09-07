#!/usr/bin/env python3
"""lcm_gcd.py"""

import math


def find_lcm(x: int, y: int) -> int:
    """Uses a short algorithm to find the least common multiple between x & y"""
    divisor: int = math.gcd(x, y)
    return x * y // divisor


def main() -> None:
    print(f"{find_lcm(447618, 2011835):,}")


if __name__ == "__main__":
    main()
