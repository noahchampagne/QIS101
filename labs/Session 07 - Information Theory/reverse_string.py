#!/usr/bin/env python3
"""reverse_string.py"""


def reverse_str(a: str) -> str:
    """Reverse string 'a' using range() with a negative step value"""
    b: str = ""
    for i in range(len(a) - 1, -1, -1):
        b += a[i]
    return b


def reverse_str2(a: str) -> str:
    """Reverse string 'a' using a reversed() range()"""
    b: str = ""
    for i in reversed(range(len(a))):
        b += a[i]
    return b


def reverse_str3(a: str) -> str:
    """Reverse string 'a' using string (prefix) concatenation"""
    b: str = ""
    for c in a:
        b = c + b
    return b


def main() -> None:
    s: str = "Forever Young"
    print(s)
    print(f"Number of characters: {len(s)}")

    print(reverse_str(s))
    print(reverse_str2(s))
    print(reverse_str3(s))

    # Reverse 's' using string join()
    print("".join(reversed(s)))

    # Reverse 's' using array slicing
    print(s[10:-1:-1])


if __name__ == "__main__":
    main()
