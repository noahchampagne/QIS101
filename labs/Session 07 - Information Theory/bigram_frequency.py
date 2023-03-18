#!/usr/bin/env python3
"""bigram_frequency.py"""

from collections import Counter
import os
import sys

# import typing

# if typing.TYPE_CHECKING:
# from typing import Any


def main() -> None:
    file_name: str = os.path.dirname(sys.argv[0]) + "/bigram_ciphertext.txt"
    with open(file_name, "rb") as f_in:
        print(f'Bigram analysis of file \n"{file_name}" :')

        # Read in text file into an array of file bytes
        f_bytes: bytearray = bytearray(f_in.read())

        # Create Counter dictionary storing successive letter counts
        bigrams: Counter[tuple[int, int]] = Counter()
        for i in range(0, len(f_bytes) - 2):
            bigrams[(f_bytes[i], f_bytes[i + 1])] += 1

        # Reverse sort bigrams tallied by Counter's dictionary item value,
        # so the bigrams with the highest frequency appear first
        sorted_bigrams: list[tuple[tuple[int, int], int]] = sorted(
            bigrams.items(), key=lambda v: v[1], reverse=True
        )

        # Print the top 10 most frequently occurring bigrams in text file
        num_bigrams: int = sum(bigrams.values())
        for k, v in sorted_bigrams[:10]:
            # Convert key tuple to ASCII string
            s: str = "".join(map(chr, k))
            print(f'Bigram {k}, "{s}": freq = {v/num_bigrams:>5.2%}')


if __name__ == "__main__":
    main()
