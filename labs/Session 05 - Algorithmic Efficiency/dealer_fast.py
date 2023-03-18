#!/usr/bin/env python3
# dealer_fast.py

from random import randint, seed
from time import process_time

# fmt: off
suits: list[str] = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks: list[str] = ["Deuce", "Three", "Four", "Five", "Six", "Seven",
                    "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
# fmt: on


def init_deck() -> list[int]:
    """Returns a 52 element list of integers initialized from 0 to 51"""
    return list(range(52))


def card_name(card_num: int) -> str:
    """Returns the rank and suit for the given card number"""
    return f"{ranks[card_num % 13]} of {suits[card_num // 13]}"


def display_deck(deck: list[int]) -> None:
    """Displays each card in the given deck in order of increasing card position"""
    for card_pos, card_num in enumerate(deck):
        print(f"The card in position {card_pos} is the {card_name(card_num)}")


def deal_cards(deck: list[int]) -> None:
    """
    Swaps the card number between two randomly chosen card positions
    """
    for card_pos, card_num in enumerate(deck):
        new_card_pos: int = randint(0, 51)
        deck[card_pos] = deck[new_card_pos]
        deck[new_card_pos] = card_num


def main() -> None:
    seed(2016)
    deck: list[int] = init_deck()
    total_deals: int = 10_000
    start_time: float = process_time()
    for _ in range(0, total_deals):
        deal_cards(deck)
    elapsed_time: float = process_time() - start_time
    display_deck(deck)
    print(f"Total deals: {total_deals:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}\n")


if __name__ == "__main__":
    main()
