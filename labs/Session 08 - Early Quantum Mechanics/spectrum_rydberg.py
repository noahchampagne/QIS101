#!/usr/bin/env python3
# spectrum_rydberg.py


def main():
    R = 1.0967757e7

    print("Rydberg Formula Hydrogen Spectral Lines")

    for k in range(1, 5):
        for j in range(k + 1, k + 6):
            # Formula for waveLength in nanometers
            waveLength = 1 / (R * (1 / pow(k, 2) - 1 / pow(j, 2))) * 1e9
            print(f"{j:>3,}{waveLength:10.0f} nm")
        print()


if __name__ == "__main__":
    main()
