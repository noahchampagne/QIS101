#!/usr/bin/env python3
# hero_abilities.py

import numpy as np
import random


def calc_stats_1d20(num_rolls):
    prng_state = random.getstate()
    mean = 0
    for n in range(0, num_rolls):
        roll = random.randint(3, 18)
        mean += roll
    mean /= num_rolls
    random.setstate(prng_state)
    variance = 0
    for n in range(0, num_rolls):
        roll = random.randint(3, 18)
        variance += pow(roll - mean, 2)
    variance /= num_rolls
    std_dev = np.sqrt(variance)
    return mean, std_dev


def calc_stats_3d6(num_rolls):
    prng_state = random.getstate()
    mean = 0
    for n in range(0, num_rolls):
        roll = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        mean += roll
    mean /= num_rolls
    random.setstate(prng_state)
    variance = 0
    for n in range(0, num_rolls):
        roll = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        variance += pow(roll - mean, 2)
    variance /= num_rolls
    std_dev = np.sqrt(variance)
    return mean, std_dev


def main():
    random.seed(2016)

    num_rolls = int(1e6)

    print(f"Rolling abilities for {num_rolls:,} heroes...")

    m1, s1 = calc_stats_1d20(num_rolls)
    m3, s3 = calc_stats_3d6(num_rolls)

    print(f"Mean ability (1d20): {m1:.2f}")
    print(f"Mean ability (3d6):  {m3:.2f}")

    print(f"Standard Deviation ability (1d20): {s1:.2f}")
    print(f"Standard Deviation ability (3d6) : {s3:.2f}")


if __name__ == "__main__":
    main()
