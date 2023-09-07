#!usr/bin/env python3
"""hamming_weight.py"""


def popcount(x: int) -> int:
    """Uses bit manipulation to find the hamming weight of x"""
    # Works by the divide & conquer method which counts the number of
    # 1's bits in each section
    x = (x & 0x55555555) + (x >> 1 & 0x55555555)
    x = (x & 0x33333333) + (x >> 2 & 0x33333333)
    x = (x & 0x0F0F0F0F) + (x >> 4 & 0x0F0F0F0F)
    x = (x & 0x00FF00FF) + (x >> 8 & 0x00FF00FF)
    x = (x & 0x0000FFFF) + (x >> 16 & 0x0000FFFF)
    return x


def hamming(x: int) -> int:
    """A much simpler way to find the hamming weight of x"""
    binary: str = format(x, "b")
    return binary.count("1")


def main() -> None:
    n: int = 95601
    print(f"Hamming Weight of {n}: {popcount(95601)}")


if __name__ == "__main__":
    main()
