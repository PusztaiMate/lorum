from .ranks import Rank, BadRankException
from .suits import Suit, BadSuitException


class HungarianCard:
    def __init__(self, rank: Rank, suit: Suit):
        self._rank = Rank.UNKNOWN_RANK
        self._suit = Suit.UNKNOWN_SUIT

        self.rank = rank
        self.suit = suit

    @property
    def rank(self) -> Rank:
        return self._rank

    @rank.setter
    def rank(self, new_rank: Suit):
        if not isinstance(new_rank, Rank):
            raise BadRankException(f"Unknown rank ({new_rank})")
        self._rank = new_rank

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, new_suit: Suit):
        if not isinstance(new_suit, Suit):
            raise BadSuitException(f"Unknown suit ({new_suit})")
        self._suit = new_suit
