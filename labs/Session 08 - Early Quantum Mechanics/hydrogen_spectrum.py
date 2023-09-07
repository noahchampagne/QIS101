#!/usr/bin/env python3
"""hydrogen_spectrum.py"""


def print_states() -> None:
    """Prints the Pfund & Humphreys Spectral Series"""
    print("Bohr's Model & Rydberg Formula for Hydrogen Spectral Lines")
    # Necessary constants
    e_charge: float = 1.602e-19
    e_mass: float = 9.109e-31
    perm: float = 8.854e-12
    h_plank: float = 6.626e-34
    speed_light: float = 2.998e8
    r_constant: float = 1.0967757e7

    # Bohr's formula for ground state energy
    e_0: float = (pow(e_charge, 4) * e_mass) / (8 * pow(perm, 2) * pow(h_plank, 2))

    print("\t\t\tBohr's Solution\t\tRydberg's Solution")
    # Loops through the Pfund & Humphreys final states
    for final in range(5, 7):
        for init in range(final + 1, final + 6):
            # Initial energy level
            e_i: float = -e_0 / pow(init, 2)
            # Final energy level
            e_f: float = -e_0 / pow(final, 2)
            # Formula for Bohr waveLength in nanometers
            b_wave_length: float = h_plank * speed_light / (e_i - e_f) * 1e9
            # Formula for Rydberg waveLength in nanometers
            r_wave_length: float = (
                1 / (r_constant * (1 / pow(final, 2) - 1 / pow(init, 2))) * 1e9
            )
            print(
                f"\t{init:>2} -> {final:>2}{b_wave_length:16.0f} nm\t{r_wave_length:16.0f} nm"
            )
        print()


def main() -> None:
    print_states()


if __name__ == "__main__":
    main()
