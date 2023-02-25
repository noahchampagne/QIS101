#!/usr/bin/env python3
"""dealer_slow.py"""

import random
import time


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
    return list(range(52))


def card_name(card_num: int) -> str:
    """Returns the rank and suit for the given card number"""
    name = f"{ranks[card_num % 13]} of {suits[card_num // 13]}"
    return name


def display_deck(deck: list[int]):
    """Displays each card in the given deck in order of increasing card position"""
    for card_pos, card_num in enumerate(deck):
        print(f"The card in position {card_pos} is the {card_name(card_num)}")


def deal_cards(deck: list[int]):
    """
    Sets each card position to a random card number between 0 and 51
    while ensuring no card number is selected more than once
    """
    already_dealt = [False] * 52
    for card_pos, _ in enumerate(deck):
        new_card_num = random.randint(0, 51)
        while already_dealt[new_card_num]:
            new_card_num = random.randint(0, 51)
        deck[card_pos] = new_card_num
        already_dealt[new_card_num] = True


def main():
    random.seed(2016)

    deck = init_deck()

    total_deals = 10_000

    start_time = time.process_time()

    for _ in range(0, total_deals):
        deal_cards(deck)

    elapsed_time = time.process_time() - start_time

    display_deck(deck)

    print(f"Total deals: {total_deals:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}\n")


if __name__ == "__main__":
    main()
