#!/usr/bin/env python3
# dealer_bogus.py

import random

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


def init_deck():
    return list(range(52))


def card_name(card_num):
    name = f"{ranks[card_num % 13]} of {suits[card_num // 13]}"
    return name


def display_deck(deck):
    for card_pos, card_num in enumerate(deck):
        print(f"The card in position {card_pos} is the {card_name(card_num)}")


def deal_cards(deck):
    for card_pos, _ in enumerate(deck):
        new_card_num = random.randint(0, 51)
        deck[card_pos] = new_card_num


def main():
    random.seed(2016)
    deck = init_deck()
    deal_cards(deck)
    display_deck(deck)


if __name__ == "__main__":
    main()
