#!/usr/bin/env python3
"""spectrum_rydberg.py"""


def main():
    rydberg_constant = 1.0967757e7

    print("Rydberg Formula for Hydrogen Spectral Lines")

    for k in range(1, 5):
        for j in range(k + 1, k + 6):
            # Formula for waveLength in nanometers
            wave_length = 1 / (rydberg_constant * (1 / pow(k, 2) - 1 / pow(j, 2))) * 1e9
            print(f"\t{j:>2} -> {k:>2}{wave_length:8.0f} nm")
        print()


if __name__ == "__main__":
    main()
