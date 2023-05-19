# python_dictionaries.py

from pprint import pprint


def main():
    capitals = {
        "USA": "Washington D.C.",
        "Germany": "Berlin",
        "France": "Paris",
        "Russia": "Moscow",
        "India": "New Delhi",
        "China": "Beijing",
    }

    print(capitals)
    print()

    # Add new key-value pairs to dictionary
    capitals.update({"United Kingdom": "London"})
    capitals["Spain"] = "Madrid"

    # Change an existing key's value
    capitals["USA"] = "New York"

    # Remove a key-value pair
    del capitals["Russia"]

    # Pretty print the dictionary (will sort by keys)
    pprint(capitals)
    print()

    # Get the value of a specific key
    country = "France"
    capital = capitals[country]
    print(f"The Capital of {country} is {capital}")


main()
