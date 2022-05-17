#!/usr/bin/env python3
# euclid_gcd.py


def gcd(a, b):
    if a < b:
        a, b = b, a
    c = a - b
    while c > 0:
        if c > b:
            a = c
        else:
            a = b
            b = c
        c = a - b
    return b


def main():
    a = 182
    b = 231
    print(f"The GCD of {a} and {b} = {gcd(a,b)}")


if __name__ == "__main__":
    main()
