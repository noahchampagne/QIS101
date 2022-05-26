#!/usr/bin/env python3
# welcome.py

import matplotlib.pyplot as plt
import numpy as np
import sys
import os


def plot(ax): 
    x = np.linspace(-2, 2, 500)
    f_top = np.sqrt(1 - (np.abs(x) - 1) ** 2)
    f_bot = np.arccos(1 - np.abs(x)) - np.pi
    ax.plot(x, f_top, color="red")
    ax.plot(x, f_bot, color="red")
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-3.5, 1.5)
    ax.set_title("Welcome to the Foundations of Quantum Information Science!")
    ax.set_aspect("equal")


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
            