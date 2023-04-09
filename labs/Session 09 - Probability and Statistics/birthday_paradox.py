#!/usr/bin/env python3
"""birthday_paradox.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from numba import njit  # type: ignore

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


@njit  # type: ignore
def shared_birthdays(class_size: int) -> bool:
    birthdays: NDArray[np.int_] = np.random.randint(0, 365, class_size)
    for i in range(birthdays.size - 2):
        for j in range(i + 1, birthdays.size):
            if birthdays[i] == birthdays[j]:
                return True
    return False


@njit  # type: ignore
def calc_probabilities(num_classes: int, max_class_size: int) -> NDArray[np.float_]:
    prob: NDArray[np.float_] = np.zeros(max_class_size, dtype=np.float_)
    for class_size in range(max_class_size):
        count: int = 0
        for _ in range(num_classes):
            if shared_birthdays(class_size):
                count += 1
        prob[class_size] = count / num_classes
    return prob


def plot(ax: Axes) -> None:
    np.random.seed(2021)

    num_classes: int = 10_000
    max_class_size: int = 80
    prob: NDArray[np.float_] = calc_probabilities(num_classes, max_class_size)

    # fmt: off
    ax.step(range(max_class_size), prob, color="black", linewidth=3,
            label="Estimated Probability")
    # fmt: on

    min_class_size: int = np.where(prob > 0.50)[0][0]
    p: float = prob[min_class_size]
    ax.vlines(min_class_size, 0, prob[min_class_size], color="red")

    # See https://en.wikipedia.org/wiki/Birthday_problem
    x: NDArray[np.float_] = np.linspace(0, 80, 200, dtype=np.float_)
    y: NDArray[np.float_] = 1.0 - np.exp(-(x**2) / 730)

    # fmt: off
    ax.plot(x, y, color="blue",
            label=r"Approximation: $1-{\rm e}^-\frac{x^2}{365*2}$")
    # fmt: on

    ax.set_xlim(0, 80)
    ax.set_ylim(0, 1.0)
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(0.1))
    ax.grid()
    ax.set_title(f"Birthday Paradox ({num_classes:,} classes)")
    ax.set_xlabel("Class Size")
    ax.set_ylabel("Probability")
    ax.legend()

    ax.annotate(
        f"Min Class Size = {min_class_size}",
        xy=(min_class_size, p),
        xytext=(28, 0.45),
        arrowprops={"facecolor": "black", "shrink": 0.05},
    )


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
