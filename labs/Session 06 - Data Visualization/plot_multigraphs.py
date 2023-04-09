#!/usr/bin/env python3
"""plot_multigraphs.py"""

import matplotlib.pyplot as plt
import plot_parabola
import plot_polynomial
import plot_rings
import plot_rose_curves


def main() -> None:
    plt.figure(__file__)
    plot_parabola.plot(plt.subplot(221))
    plot_polynomial.plot(plt.subplot(222))
    plot_rings.plot(plt.subplot(223))
    plot_rose_curves.plot(plt.subplot(224, projection="polar"))
    plt.show()


if __name__ == "__main__":
    main()
