#!/usr/bin/env python3
# pachinko_normal.py

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import scipy.stats as stats
from numba import jit
import os
import sys


def stegun_normal(mean, std_dev):
    q = 1 - np.random.random()
    p = q if q < 0.5 else 1 - q
    t = np.sqrt(np.log(1 / p**2))
    x = t - (2.515517 + 0.802853 * t + 0.010328 * (t * t)) / (
        1 + 1.432788 * t + 0.189269 * (t * t) + 0.001308 * (t * t * t)
    )
    x = x if q < 0.5 else -x
    return x * std_dev + mean


@jit(nopython=True)
def pachinko_normal(num_balls, num_levels):
    np.random.seed(2016)
    balls = np.zeros(num_balls, dtype=np.int32)
    for ball_num in range(num_balls):
        slot = 0
        for _ in range(num_levels):
            slot += -1 if np.random.rand() < 0.5 else 1
        balls[ball_num] = slot // 2
    return balls


def plot(ax):
    num_levels = 10
    num_balls = 1000

    balls = pachinko_normal(num_balls, num_levels)

    slots = np.zeros(num_levels + 1)
    first_slot = num_levels // 2
    for ball_num in range(num_balls):
        slot_num = int(first_slot + balls[ball_num])
        slots[slot_num] += 1
    slots = slots / num_balls

    x = np.linspace(-num_levels // 2, num_levels // 2, num_levels + 1)
    ax.plot(x, slots, color="blue", linewidth=2, label="Pachinko")

    mu = np.mean(balls)
    sigma = np.std(balls)
    norm_x = np.linspace(-num_levels // 2, num_levels // 2, 100)
    norm_y = stats.norm(mu, sigma).pdf(norm_x)
    ax.plot(norm_x, norm_y, color="red", linewidth=2, label="Normal")

    ax.set_title(
        f"Pachinko vs. Normal PDF ({num_levels:,} levels : " f"{num_balls:,} balls)"
    )
    ax.set_xlabel("Slot Number")
    ax.set_ylabel("Probability")
    ax.legend()


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
