# plot_liquid_range.py

import json
import numpy as np
import matplotlib.pyplot as plt


def main():
    # Create a Python dictionary from the JSON file
    with open("periodic_table.json", "r", encoding="utf-8") as infile:
        periodic_table = json.load(infile)

    # Sort elements by group, period, and then atomic number
    elements: list = []
    for group in range(1, 19):
        for period in range(1, 8):
            for _, v in enumerate(periodic_table["elements"]):
                if group == int(v["group"]) and period == int(v["period"]):
                    elements.append(
                        (
                            f"{v['symbol']}-{v['number']}",
                            float(v["melt"] or np.NINF),
                            float(v["boil"] or np.inf),
                        )
                    )

    # Create numpy arrays from sorted elements list
    data = np.array(elements)
    melt = np.array(data[:, 1], dtype=float) - 273.15
    boil = np.array(data[:, 2], dtype=float) - 273.15

    # Find element with smallest liquid range
    liquid_range = boil - melt
    min_idx = np.argmin(liquid_range)
    min_range = liquid_range[min_idx]
    print(f"Smallest liquid range: " f"{min_range:>8,.2f}°C is " f"{data[min_idx, 0]}")

    # Find element with largest liquid range
    measured_liquid_range = np.array(sorted(liquid_range, reverse=True))
    max_measured_idx = np.argwhere(measured_liquid_range < np.inf).min()
    max_range = measured_liquid_range[max_measured_idx]
    max_idx = np.argwhere(liquid_range == max_range)[0, 0]
    print(f" Largest liquid range: " f"{max_range:>8,.2f}°C is " f"{data[max_idx, 0]}")

    # Plot the melting and boiling point of every element
    plt.figure(__file__)
    ax = plt.axes()

    x = np.arange(len(elements))
    ax.plot(x, melt, color="turquoise", marker=".", label="Melting Point")
    ax.plot(x, boil, color="coral", marker=".", label="Boiling Point")

    ax.legend(loc="lower center")

    ax.set_title("Melting and Boiling Point")
    ax.set_xlabel("Elements (By Group, Period, Atomic Number)")
    ax.set_ylabel(r"$Temperature\;(\degree C)$")

    ax.set_xticks(x)
    ax.set_xticklabels(data[:, 0], fontsize=9, rotation=90)
    ax.grid()

    plt.show()


main()
