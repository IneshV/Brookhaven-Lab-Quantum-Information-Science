#!/usr/bin/env python3
"""dealer_fast.py"""

import time

import numpy as np

#Card options ORDERED for encoding
# fmt: off
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

ranks = ["Deuce", "Three", "Four", "Five", "Six", "Seven",
         "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
# fmt: on


def init_deck():
    """Return a *shuffled* NumPy array of 52 integers 0–51.
    The shuffle is done via 52 random swaps (Fisher-Yates style).
    """

    deck = np.arange(52) # ordered deck [0, 1, …, 51]
    for card_pos in range(52):
        new_card_pos = np.random.randint(52) # pick random target slot
        swap_card = deck[card_pos] # remember card in position of iterated loop
        deck[card_pos] = deck[new_card_pos] # replace card in position of iterated loop with the card in random target slot
        deck[new_card_pos] = swap_card # replace card in random target slot with card that was in position of iterated loop
    return deck


def print_deck(deck):
    """Print the 52 cards in order of the array positions.
        Each integer encodes a specific card:
        value // 13  -> suit index  (0=Clubs … 3=Spades)
        value % 13   -> rank index  (0=Deuce … 12=Ace)
    """

    for card_pos in range(52):
        card_num = deck[card_pos]
        suit_num = card_num // 13               # 0–3
        rank_num = card_num % 13                # 0–12
        card_name = f"{ranks[rank_num]} of {suits[suit_num]}"
        print(f"The card in position {card_pos} is the {card_name}")


def main():
    np.random.seed(2016)        # reproducible shuffles
    total_deals = 10_000        # shuffle count

    #shuffle total_deals times and times the process
    start_time = time.perf_counter()
    for _ in range(total_deals):
        deck = init_deck()
    elapsed_time = time.perf_counter() - start_time

    print_deck(deck)

    print(f"Total deals: {total_deals:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}")


if __name__ == "__main__":
    main()
