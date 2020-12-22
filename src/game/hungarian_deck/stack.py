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
        self._num_cards_on_stack = 0

        self.suit = suit
        self.top_card = HungarianCard(Rank.UNKNOWN_RANK, self.suit)
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
        self.top_card.rank = rank

    def put(self, card: HungarianCard):
        if self._num_cards_on_stack == self.max_stack_size:
            raise StackFullException(f"stack full ({self._num_cards_on_stack})")

        nc = self.next_card()
        if card != nc:
            raise WrongCardException(f"next card should be {nc}")

        self.top_card = nc
        self._num_cards_on_stack += 1

    def __len__(self) -> int:
        return self._num_cards_on_stack

    def next_card(self) -> Optional[HungarianCard]:
        if self._num_cards_on_stack == 0:
            return self.top_card

        if self._num_cards_on_stack >= self.max_stack_size:
            return None

        return next_card(self.top_card)
