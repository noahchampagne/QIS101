#!/usr/bin/env python3
# freq_histogram.py

import os
import sys
from typing import Counter

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator


def plot(ax : plt.Axes, file_name:str):
    with open(file_name, "rb") as f_in:
        f_bytes = bytearray(f_in.read())
        file_size = f_in.tell()
        f_in.close()

    ticks = []
    char_count = np.zeros(256)
    for char, count in Counter(f_bytes).items():
        char_count[char] = count
        if count / file_size > 0.06:
            ticks.append(char)

    base = os.path.basename(file_name)
    text_name = os.path.splitext(base)[0]
    ax.set_title(f"Frequency Analysis ({text_name})")
    ax.set_xlabel("ASCII Value")
    ax.set_ylabel("Count")

    ax.bar([*range(256)], char_count)

    ax.xaxis.set_ticks(ticks)
    ax.xaxis.set_tick_params(rotation=90)
    ax.yaxis.set_minor_locator(AutoMinorLocator())


def main(file_name: str):
    fig = plt.figure(os.path.basename(sys.argv[0]))
    fig.set_size_inches(12, 8)
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax, file_name)
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("You must provide a filename")
    else:
        main(sys.argv[1])
