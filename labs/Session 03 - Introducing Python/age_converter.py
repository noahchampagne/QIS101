#!/usr/bin/env python3
"""age_converter.py"""


def main():
    first_name = "Dave"

    age_years = 55

    age_secs = age_years * 60 * 60 * 24 * 365

    print(f"Hello, my name is {first_name}.")

    print(f"I am {age_years} years old", end=", ")

    print(f"which is {age_secs:,} seconds.")


if __name__ == "__main__":
    main()
