from typing import Optional
from game.hungarian_deck.card import HungarianCard
from game.hungarian_deck.utils import next_card
from . import Suit, Rank


class StackFullException(Exception):
    pass


class WrongCardException(Exception):
    pass


class Stack:
    def __init__(self, suit: Suit, max_stack_size: int = 8):
        self._suit = Suit.UNKNOWN_SUIT
        self._starting_rank = Rank.UNKNOWN_RANK
        self._cards = []

        self.suit = suit
        self.max_stack_size = 8

    @property
    def suit(self) -> Suit:
        return self._suit

    @suit.setter
    def suit(self, new_suit: Suit):
        if not isinstance(new_suit, Suit):
            raise TypeError("new value is not type Suit")
        self._suit = new_suit

    @property
    def starting_rank(self) -> Rank:
        return self._starting_rank

    @starting_rank.setter
    def starting_rank(self, rank: Rank):
        if not isinstance(rank, Rank):
            raise TypeError("new rank is not type Rank")
        self._starting_rank = rank

    @property
    def top_card(self) -> HungarianCard:
        if len(self._cards) != 0:
            return self._cards[-1]
        return None

    def put(self, card: HungarianCard):
        if len(self._cards) == self.max_stack_size:
            raise StackFullException(f"stack full ({len(self._cards)})")

        nc = self.next_card()
        if card != nc:
            raise WrongCardException(f"next card should be {nc}")

        self._cards.append(nc)

    def __len__(self) -> int:
        return len(self._cards)

    def next_card(self) -> Optional[HungarianCard]:
        # no starting card set, every card with the same suit is a good option
        if self._starting_rank == Rank.UNKNOWN_RANK:
            return HungarianCard(Rank.UNKNOWN_RANK, self.suit)

        # no card, but starting rank already set
        if len(self._cards) == 0:
            return HungarianCard(self._starting_rank, self.suit)

        # stack is full, no more please
        if len(self._cards) >= self.max_stack_size:
            return None

        return next_card(self.top_card)
