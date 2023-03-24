#!/usr/bin/env python3
"""bubble_sort.py"""


from random import randint, seed
from time import process_time


def bubble_sort(values: list[int]) -> list[int]:
    """Sorts the provided list in increasing order using the Bubble Sort algorithm"""
    last_index: int = len(values) - 1
    is_sorted: bool = False
    while not is_sorted:
        swap_needed: bool = False
        for i in range(last_index):
            if values[i] > values[i + 1]:
                # Swap these adjacent values
                values[i], values[i + 1] = values[i + 1], values[i]
                swap_needed = True
        if not swap_needed:
            is_sorted = True
        else:
            last_index -= 1
    return values


def main() -> None:
    seed(2016)

    num_samples: int = 10_000

    print(f"Bubble Sorting {num_samples:,} random samples...")
    samples: list[int] = [randint(1, 10_000) for _ in range(num_samples)]

    print("UNSORTED")
    print(f"{samples[:10]} ... {samples[-10:]}")

    start_time: float = process_time()
    samples = bubble_sort(samples)
    elapsed_time: float = process_time() - start_time

    print("SORTED")
    print(f"{samples[:10]} ... {samples[-10:]}")

    print(f"Total run time (sec): {elapsed_time:.3f}\n")


if __name__ == "__main__":
    main()
