#!/usr/bin/env python3
# dealer_fast.py

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


def init_deck():
    return list(range(52))


def card_name(card_num):
    name = f"{ranks[card_num % 13]} of {suits[card_num // 13]}"
    return name


def display_deck(deck):
    for card_pos, card_num in enumerate(deck):
        print(f"The card in position {card_pos}" f" is the {card_name(card_num)}")


def deal_cards(deck):
    for card_pos, card_num in enumerate(deck):
        new_card_pos = random.randint(0, 51)
        deck[card_pos] = deck[new_card_pos]
        deck[new_card_pos] = card_num


def main():
    random.seed(2016)
    deck = init_deck()
    total_deals = 10000
    start_time = time.process_time()
    for _ in range(0, total_deals):
        deal_cards(deck)
    elapsed_time = time.process_time() - start_time
    display_deck(deck)
    print(f"Total deals: {total_deals:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}\n")


if __name__ == "__main__":
    main()
