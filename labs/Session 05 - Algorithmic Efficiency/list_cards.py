#!/usr/bin/env python3
"""list_cards.py"""


suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = [
    "Deuce",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
]


def init_deck() -> list[int]:
    """Returns a 52 element list of integers initialized from 0 to 51"""
    deck: list[int] = [0] * 52
    for card_pos, _ in enumerate(deck):
        deck[card_pos] = card_pos
    return deck


def card_name(card_num: int) -> str:
    """Returns the rank and suit for the given card number"""
    name = f"{ranks[card_num % 13]} of {suits[card_num // 13]}"
    return name


def display_deck(deck: list[int]):
    """Displays each card in the given deck in order of increasing card position"""
    for card_pos, card_num in enumerate(deck):
        print(f"The card in position {card_pos} is the {card_name(card_num)}")


def main():
    deck = init_deck()
    display_deck(deck)


if __name__ == "__main__":
    main()
