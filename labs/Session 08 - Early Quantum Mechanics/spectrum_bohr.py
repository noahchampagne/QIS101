#!/usr/bin/env python3
# spectrum_bohr.py


def main():
    eCharge = 1.6e-19
    eMass = 9.1e-31
    permittivity = 8.84e-12
    hPlank = 6.63e-34
    speedLight = 3e8

    # Bohr's formula for ground state energy
    E0 = (pow(eCharge, 4) * eMass) / (8 * pow(permittivity, 2) * pow(hPlank, 2))

    print("Bohr Model Hydrogen Spectral Lines")

    for i in range(1, 5):
        for f in range(i + 1, i + 6):
            # Initial energy level
            Ei = -E0 / pow(i, 2)
            # Final energy level
            Ef = -E0 / pow(f, 2)
            # Formula for waveLength in nanometers
            waveLength = hPlank * speedLight / (Ef - Ei) * 1e9
            print(f"{f:>3,}{waveLength:10.0f} nm")
        print()


if __name__ == "__main__":
    main()
