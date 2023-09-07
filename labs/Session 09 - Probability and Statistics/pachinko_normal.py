#!/usr/bin/env python3
"""pachinko_normal.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats  # type: ignore
from numba import njit  # type: ignore

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def stegun_normal(mean: float, std_dev: float) -> float:
    q: float = 1 - np.random.random()
    p: float = q if q < 0.5 else 1 - q
    t: float = np.sqrt(np.log(1 / p**2))
    x: float = t - (2.515517 + 0.802853 * t + 0.010328 * (t * t)) / (
        1 + 1.432788 * t + 0.189269 * (t * t) + 0.001308 * (t * t * t)
    )
    x = x if q < 0.5 else -x
    return x * std_dev + mean


@njit  # type: ignore
def pachinko_normal(num_balls: int, num_levels: int) -> NDArray[np.int_]:
    np.random.seed(2016)
    balls: NDArray[np.int_] = np.zeros(num_balls, dtype=np.int_)
    for ball_num in range(num_balls):
        slot: int = 0
        for _ in range(num_levels):
            slot += -1 if np.random.rand() < 0.5 else 1
        balls[ball_num] = slot // 2
    return balls


def plot(ax: Axes) -> None:
    num_levels: int = 100
    num_balls: int = 1000000

    balls: NDArray[np.int_] = pachinko_normal(num_balls, num_levels)
    slots: NDArray[np.float_] = np.zeros(num_levels + 1, dtype=np.float_)

    first_slot: int = num_levels // 2
    for ball_num in range(num_balls):
        slot_num: int = int(first_slot + balls[ball_num])
        slots[slot_num] += 1
    slots = slots / float(num_balls)

    x: NDArray[np.float_] = np.linspace(
        -num_levels // 2, num_levels // 2, num_levels + 1, dtype=np.float_
    )
    ax.plot(x, slots, color="blue", linewidth=2, label="Pachinko")

    mu: np.float_ = np.mean(balls)
    sigma: np.float_ = np.std(balls)
    norm_x: NDArray[np.float_] = np.linspace(
        -num_levels // 2, num_levels // 2, 100, dtype=np.float_
    )
    norm_y: NDArray[np.float_] = stats.norm(mu, sigma).pdf(norm_x)  # type: ignore
    ax.plot(norm_x, norm_y, color="red", linewidth=2, label="Normal")

    ax.set_title(
        f"Pachinko vs. Normal PDF ({num_levels:,} levels : {num_balls:,} balls)"
    )
    ax.set_xlabel("Slot Number")
    ax.set_ylabel("Probability")
    ax.legend()


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
