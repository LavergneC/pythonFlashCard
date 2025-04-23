# typing-alias.py
# [Python typing]
import random
from itertools import product

from mypy import api as typing_check  # fcPython:keep line

SUITS = "♠ ♡ ♢ ♣".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()


def create_deck(shuffle=False):
    """
    Create a deck of 52 cards. A deck is a list of cards, a card is a tuple of (suit, rank)
        suits : "♠ ♡ ♢ ♣"
        ranks : "2 3 4 5 6 7 8 9 10 J Q K A"
    """
    deck = list(product(SUITS, RANKS))
    if shuffle:
        random.shuffle(deck)
    return deck


def test_create_deck() -> None:
    ordered_deck = create_deck()
    assert len(ordered_deck) == 52
    assert ordered_deck[0] == ("♠", "2")
    assert ordered_deck[-1] == ("♣", "A")
    assert ordered_deck.count(("♢", "5")) == 1

    shuffled_deck = create_deck(shuffle=True)
    assert len(shuffled_deck) == 52
    assert shuffled_deck.count(("♡", "J")) == 1

    assert ordered_deck != shuffled_deck

    result = typing_check.run(["exercise.py"])
    assert result[2] == 0, result[0] if result[0] else result[1]
