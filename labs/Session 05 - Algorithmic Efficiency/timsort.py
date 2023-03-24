#!/usr/bin/env python3
"""timsort.py"""

from random import randint, seed
from time import process_time


def main() -> None:
    seed(2016)

    num_samples: int = 10_000

    print(f"Timsorting {num_samples:,} random samples...")
    samples: list[int] = [randint(1, 10_000) for _ in range(num_samples)]

    print("UNSORTED")
    print(f"{samples[:10]} ... {samples[-10:]}")

    start_time: float = process_time()
    samples.sort()
    elapsed_time: float = process_time() - start_time

    print("SORTED")
    print(f"{samples[:10]} ... {samples[-10:]}")

    print(f"Total run time (sec): {elapsed_time:.3f}\n")


if __name__ == "__main__":
    main()
