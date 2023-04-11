#!/usr/bin/env python3
"""bessel_correction.py"""

from __future__ import annotations

import pickle
import typing
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from numba import njit  # type: ignore
from numpy.random import choice, randint, seed  # type: ignore

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


@njit  # type: ignore
def get_bsv(arr: NDArray[np.int_]) -> float:
    mean: np.float_ = np.mean(arr)
    bsv: float = float(np.sum((arr - mean) ** 2) / len(arr))  # type: ignore
    return bsv


@njit  # type: ignore
def get_sample_bsv(population: NDArray[np.int_], sample_size: int) -> float:
    num_trials: int = 20_000
    total_bsv: float = 0.0
    for _ in range(num_trials):
        samples: NDArray[np.int_] = choice(population, sample_size, replace=False)
        total_bsv += get_bsv(samples)
    mean_bsv: float = total_bsv / num_trials
    return mean_bsv


def run_trials() -> list[tuple[float, float, float, float]]:
    seed(2021)
    population: NDArray[np.int_] = randint(0, 1000, 7000)
    pop_var: float = get_bsv(population)

    max_sample_size: int = 20

    print(f"{'Sample Size':^11}{'Sample Var':^21}{'Pop Var':^18}{'Ratio':^8}")

    results: list[tuple[float, float, float, float]] = []
    for sample_size in range(2, max_sample_size + 1):
        sample_bsv: float = get_sample_bsv(population, sample_size)
        ratio: float = sample_bsv / pop_var
        results.append((sample_size, sample_bsv, pop_var, ratio))
        print(
            f"{sample_size:^11}{sample_bsv:>16,.4f}{pop_var:>18,.4f}",
            f"{ratio:^15.4f}",
        )
    return results


def plot_ratio(ax: Axes, results: list[tuple[float, float, float, float]]) -> None:
    x1: list[float] = [r[0] for r in results]
    y1: list[float] = [r[3] for r in results]
    ax.plot(x1, y1, label="BSV/PV")

    x2: NDArray[np.float_] = np.linspace(2, 20, endpoint=True)
    y2: NDArray[np.float_] = (x2 - 1) / x2
    ax.plot(x2, y2, label=r"$\frac{n-1}{n}$")

    ax.set_title(r"$\frac{BSV}{PV}$ compared to Hyperbola $\frac{(n-1)}{n}$")
    ax.set_xlabel("Sample Size")
    ax.set_ylabel("Biased Sample Var / Population Var")
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(0.05))
    ax.legend()


def plot_ubsv(ax: Axes, results: list[tuple[float, float, float, float]]) -> None:
    x: list[float] = [r[0] for r in results]
    y: list[float] = [r[2] for r in results]
    ax.plot(x, y, label="Pop Var")

    y = [r[1] for r in results]
    ax.plot(x, y, label="BSV")

    for i, _ in enumerate(y):
        y[i] = y[i] * x[i] / (x[i] - 1)
    ax.plot(x, y, label="UBSV")

    ax.set_title("Variance: Population v. Biased Sample v. Unbiased Sample")
    ax.set_xlabel("Sample Size")
    ax.set_ylabel("Variance")
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.legend()


def main() -> None:
    data_file: Path = Path(__file__).parent.joinpath("bessel.pickle")
    if not data_file.exists():
        results: list[tuple[float, float, float, float]] = run_trials()
        with open(data_file, "wb") as file_out:
            pickle.dump(results, file_out, pickle.HIGHEST_PROTOCOL)
        plt.figure(__file__)
        plot_ratio(plt.axes(), results)  # type: ignore
        plt.show()
    else:
        with open(data_file, "rb") as file_in:
            results = pickle.load(file_in)
        print(f"{'Sample Size':^11}{'Sample Var':^21}{'Pop Var':^16}{'UBSV':^12}")
        for r in results:
            sample_size, sample_bsv, pop_var, _ = r
            ubsv: float = sample_bsv * sample_size / (sample_size - 1)
            print(
                f"{sample_size:^11}{sample_bsv:>16,.4f}{pop_var:>18,.4f}",
                f"{ubsv:^18,.4f}",
            )

        plt.figure(__file__)
        plot_ubsv(plt.axes(), results)
        plt.show()


if __name__ == "__main__":
    main()
