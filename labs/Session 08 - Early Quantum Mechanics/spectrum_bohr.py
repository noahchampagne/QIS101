#!/usr/bin/env python3
# spectrum_bohr.py


def main():
    eCharge = 1.602e-19
    eMass = 9.109e-31
    permittivity = 8.854e-12
    hPlank = 6.626e-34
    speedLight = 2.998e8

    # Bohr's formula for ground state energy
    E0 = (pow(eCharge, 4) * eMass) / (8 * pow(permittivity, 2) * pow(hPlank, 2))

    print("Bohr Model Hydrogen Spectral Lines")

    for f in range(1, 5):
        for i in range(f + 1, f + 6):
            # Initial energy level
            Ei = -E0 / pow(i, 2)
            # Final energy level
            Ef = -E0 / pow(f, 2)
            # Formula for waveLength in nanometers
            waveLength = hPlank * speedLight / (Ei - Ef) * 1e9
            print(f"{f:>3,}{waveLength:10.0f} nm")
        print()


if __name__ == "__main__":
    main()
