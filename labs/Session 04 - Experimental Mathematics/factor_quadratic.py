#!usr/bin/env python3
"""factor_quadratic.py"""
import math


def factor(a: int, b: int, c: int) -> tuple[int, int, int, int, int]:
    """Takes in values in the form of ax^2 + bx + c and factors the polynomial to
    display it as ({w}x + {x})({y}x + {z})"""
    # Take care of the gcd
    divisor: int = math.gcd(a, b, c)
    # Attempts to find a common divisor
    if divisor != 1:
        a //= divisor
        b //= divisor
        c //= divisor
    # Accounts for the fact that negatives are possible
    if a < 0 and b < 0 and c < 0:
        a = abs(a)
        b = abs(b)
        c = abs(c)
        divisor *= -1
    # Start finding factors

    # Loops through all the possible factorizations until one works
    # Returns 0's if no factors are found
    for w in range(1, math.floor(math.sqrt(abs(a))) + 1):
        if a % w == 0:
            y: int = a // w
            for x in range(1, math.floor(math.sqrt(abs(c))) + 1):
                if c % x == 0:
                    z: int = c // x
                    if (((w + x) * (y + z)) - a - c) == b:
                        return divisor, w, x, y, z
                    elif (((w - x) * (y - z)) - a - c) == b:
                        return divisor, w, -x, y, -z
    return 0, 0, 0, 0, 0


def main() -> None:
    a: int = 115425
    b: int = 3254121
    c: int = 379020
    divisor, w, x, y, z = factor(a, b, c)
    if divisor:
        print(f"The factorization is: {divisor}({w}x + {x})({y}x + {z})")
    else:
        print("No factorization")


if __name__ == "__main__":
    main()
