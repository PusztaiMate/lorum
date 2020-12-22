from typing import List, Iterable
from abc import ABC, abstractmethod, abstractproperty

from game.hungarian_deck import HungarianCard


class PlayerBase(ABC):
    @abstractproperty
    def id(self) -> str:
        pass

    @abstractproperty
    def cards(self) -> List[HungarianCard]:
        pass

    @abstractmethod
    def __len__(self) -> int:
        """Return the number of cards left"""
        pass

    @abstractmethod
    def receive_cards(self, *cards: Iterable[HungarianCard]) -> None:
        pass

    @abstractmethod
    def receive_card(self, card: HungarianCard) -> None:
        pass

    @abstractmethod
    def remove_card(self, card: HungarianCard) -> None:
        pass


class Player(PlayerBase):
    def __init__(self, name: str):
        self.name = name

        self._cards = []

    @property
    def id(self):
        return self.name

    @property
    def cards(self) -> List[HungarianCard]:
        return self._cards

    def receive_card(self, card: HungarianCard):
        self._cards.append(card)

    def receive_cards(self, *cards):
        for card in cards:
            self.receive_card(card)

    def remove_card(self, card: HungarianCard) -> None:
        self.cards.remove(card)

    def __len__(self):
        return len(self._cards)
