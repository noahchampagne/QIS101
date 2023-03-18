#!/usr/bin/env python3
"""euler_totient.py"""


def gcd(a:int, b:int) -> int:
    """Find greatest common divisor of a & b"""
    while b > 0:
        a, b = b, a % b
    return a


def totient(n: int) -> int:
    """Calculate Euler's totient of n"""
    s: int = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            s += 1
    return s


def main() -> None:
    print("Natural numbers between 2 and 100", end=" ")
    print("that exceed their totient by one:")

    for n in range(2, 101):
        if n == totient(n) + 1:
            print(n, end=" ")


if __name__ == "__main__":
    main()
