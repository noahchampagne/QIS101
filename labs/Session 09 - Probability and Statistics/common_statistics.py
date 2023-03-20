#!/usr/bin/env python3
"""common_statistics.py"""

import statistics
from collections import Counter
from math import sqrt
from random import randint, seed


def mean(samples: list[int]) -> float:
    return sum(samples) / len(samples)


def median(samples: list[int]) -> float:
    samples.sort()
    i: int = len(samples) // 2
    return samples[i] if len(samples) % 2 == 1 else (samples[i - 1] + samples[i]) / 2


def mode(samples: list[int]) -> list[int]:
    # Create a dictionary to tally the occurrence of each value
    count: Counter[int] = Counter(sorted(samples))
    # Find the maximum count of all keys (samples)
    max_count: int = max(count.values())
    # Select the keys which have that max count
    return [k for k, v in count.items() if v == max_count]


def sample_variance(samples: list[int]) -> float:
    m: float = mean(samples)
    v: float = 0.0
    for i in range(0, len(samples)):
        v += (samples[i] - m) ** 2
    v /= len(samples) - 1
    return v


def main() -> None:
    seed(2016)

    # Create list of 30 random integers in range [0,100]
    samples: list[int] = []
    for _ in range(30):
        samples.append(randint(0, 100))

    # Print list in rows of 10 elements each
    print("Samples = list[")
    for i in range(3):
        print("\t", end="")
        print(*samples[i * 10 : i * 10 + 10], sep=", ", end=",\n")
    print("]\n")

    # Compare common statistics calculated via custom code
    # versus using the standard library "statistics" package
    print(f"Mean    = {mean(samples):.4f}")
    print(f"Mean    = {statistics.mean(samples):.4f}")
    print()

    print(f"Median  = {median(samples):.4f}")
    print(f"Median  = {statistics.median(samples):.4f}")
    print()

    print(f"Mode    = {mode(samples)}")
    print(f"Mode    = {sorted(statistics.multimode(samples))}")
    print()

    v: float = sample_variance(samples)
    print(f"Sample Variance = {v:.4f}")
    print(f"Sample Variance = {statistics.variance(samples):.4f}")
    print()

    print(f"Sample Std. Dev = {sqrt(v):.4f}")
    print(f"Sample Std. Dev = {statistics.stdev(samples):.4f}")


if __name__ == "__main__":
    main()
