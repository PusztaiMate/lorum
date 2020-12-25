from random import choice
from typing import List
from . import Rank, Suit, HungarianCard


class OutOfCardsException(Exception):
    pass


class HungarianDeck:
    def __init__(self):
        self._cards = None

        self.reset()

    def __len__(self) -> int:
        return len(self._cards)

    def draw(self) -> HungarianCard:
        if not self._cards:
            raise OutOfCardsException("no cards left")
        card = choice(self._cards)
        self._cards.remove(card)
        return card

    def draw_many(self, num: int) -> List[HungarianCard]:
        return [self.draw() for _ in range(num)]

    def reset(self):
        self._cards = [
            HungarianCard(rank, suit)
            for rank in Rank
            for suit in Suit
            if rank != Rank.UNKNOWN_RANK and suit != Suit.UNKNOWN_SUIT
        ]
