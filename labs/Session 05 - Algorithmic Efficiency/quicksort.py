#!/usr/bin/env python3
"""quicksort.py"""


from random import randint, seed
from timeit import timeit

from numba import njit


@njit
def bubble_sort(values: list[int]) -> list[int]:
    """Sorts the provided list in increasing order using the Bubble Sort algorithm"""
    last_index = len(values) - 1
    is_sorted = False
    while not is_sorted:
        swap_needed = False
        for i in range(last_index):
            if values[i] > values[i + 1]:
                temp = values[i]
                values[i] = values[i + 1]
                values[i + 1] = temp
                swap_needed = True
        if not swap_needed:
            is_sorted = True
        else:
            last_index -= 1
    return values


@njit
def median_of_three(values: list[int], low: int, high: int):
    """Finds the index of the median value at the low, high, and middle elements"""
    mid = (low + high) // 2
    x, y, z = values[low], values[mid], values[high]
    if x < y:
        if y < z:
            return mid
        elif x < z:
            return high
        else:
            return low
    else:
        if x < z:
            return low
        elif y < z:
            return high
        else:
            return mid


@njit
def quick_sort_partition(values: list[int], low_index: int, high_index: int) -> int:
    """Partitions a list using the median of three strategy"""
    pivot_index = median_of_three(values, low_index, high_index)  # pivot index
    pivot_value = values[pivot_index]  # pivot value

    while True:
        while values[low_index] <= pivot_value and low_index < pivot_index:
            low_index += 1
        while values[high_index] > pivot_value and high_index > pivot_index:
            high_index -= 1
        if low_index == pivot_index and high_index == pivot_index:
            return pivot_index

        # Swap array values at lo and hi indexes
        values[low_index], values[high_index] = values[high_index], values[low_index]

        if low_index == pivot_index:
            pivot_index = high_index
        elif high_index == pivot_index:
            pivot_index = low_index


@njit
def quick_sort(values: list[int], low_index: int, high_index: int) -> list[int]:
    """Sorts the provided list in increasing order using the Quicksort algorithm"""
    if low_index < high_index:
        partition_index = quick_sort_partition(values, low_index, high_index)
        if partition_index > 0:
            # Sort the left-hand sub-array
            quick_sort(values, low_index, partition_index - 1)
        # Sort the right-hand sub-array
        quick_sort(values, partition_index + 1, high_index)
    return values


@njit
def bubble_sort_once():
    """Sorts a random list just once using the Bubble Sort algorithm"""
    samples = [randint(1, 10_000) for _ in range(10_000)]
    samples = bubble_sort(samples)


@njit
def quicksort_once():
    """Sorts a random list just once using the Quicksort algorithm"""
    samples = [randint(1, 10_000) for _ in range(10_000)]
    samples = quick_sort(samples, 0, len(samples) - 1)


def main():
    seed(2016)
    print("Running tests . . .")

    time = timeit(bubble_sort_once, number=10)
    print(f"Bubble Sort time (avg) : {time/10:.3f} secs")

    time = timeit(quicksort_once, number=10)
    print(f"Quicksort time (avg)   : {time/100:.3f} secs")


if __name__ == "__main__":
    main()
