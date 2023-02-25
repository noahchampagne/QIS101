#!/usr/bin/env python3
"""sort_race.py"""


import timeit

from numba import jit
import numpy as np


@jit(nopython=True)
def init_samples() -> np.ndarray:
    """Returns an numpy array of 50,000 integers decreasing from 50,000 to 0"""
    np.random.seed(2021)
    samples = np.arange(50_000, 0, -1)
    return samples


@jit(nopython=True)
def bubble_sort(ary: np.ndarray):
    """Sorts the provided list in increasing order using the Bubble Sort algorithm"""
    last_index = len(ary) - 1
    is_sorted = False
    while not is_sorted:
        swap_needed = False
        for i in range(last_index):
            if ary[i] > ary[i + 1]:
                temp = ary[i]
                ary[i] = ary[i + 1]
                ary[i + 1] = temp
                swap_needed = True
        if not swap_needed:
            is_sorted = True
        else:
            last_index -= 1
    return


@jit(nopython=True)
def median_of_three(ary: np.ndarray, low: int, high: int):
    """Finds the index of the median array value at the low, high, and middle elements"""
    mid = (low + high) // 2
    x, y, z = ary[low], ary[mid], ary[high]
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


@jit(nopython=True)
def quick_sort_partition(ary: np.ndarray, low: int, high: int):
    """Partitions a list using the median of three strategy"""
    pivot_index = median_of_three(ary, low, high)  # pivot index
    pivot_value = ary[pivot_index]  # pivot value

    while True:
        while ary[low] <= pivot_value and low < pivot_index:
            low += 1
        while ary[high] > pivot_value and high > pivot_index:
            high -= 1
        if low == pivot_index and high == pivot_index:
            return pivot_index

        # Swap array values at lo and hi indexes
        ary[low], ary[high] = ary[high], ary[low]

        if low == pivot_index:
            pivot_index = high
        elif high == pivot_index:
            pivot_index = low


@jit(nopython=True)
def quick_sort(a, lo, hi):
    """Sorts the provided list in increasing order using the Quicksort algorithm"""
    if lo < hi:
        partition_index = quick_sort_partition(a, lo, hi)
        if partition_index > 0:
            # Sort the left-hand sub-array
            quick_sort(a, lo, partition_index - 1)
        # Sort the right-hand sub-array
        quick_sort(a, partition_index + 1, hi)
    return


@jit(nopython=True)
def bubble_sort_once():
    """Sorts a random list just once using the Bubble Sort algorithm"""
    samples = init_samples()
    bubble_sort(samples)


@jit(nopython=True)
def quicksort_once():
    """Sorts a random list just once using the Quicksort algorithm"""
    samples = init_samples()
    quick_sort(samples, 0, len(samples) - 1)


def main():
    print("Running tests . . .")

    time = timeit.timeit(bubble_sort_once, number=10)
    print(f"Bubble Sort time: {time/10:.3f} secs")

    time = timeit.timeit(quicksort_once, number=100)
    print(f"Quicksort time  : {time/100:.3f} secs")


if __name__ == "__main__":
    main()
