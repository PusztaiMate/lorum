import pytest

from game.hungarian_deck import (
    HungarianCard,
    Suit,
    Rank,
    BadRankException,
    BadSuitException,
)


def test_card_can_be_initiated_with_good_rank_and_value():
    rank = Rank.VII
    suit = Suit.HEARTS

    card = HungarianCard(rank=rank, suit=suit)

    assert card.suit == suit
    assert card.rank == rank


def test_not_using_rank_class_results_in_exception():
    suit = Suit.HEARTS
    rank = "VII"

    with pytest.raises(BadRankException):
        HungarianCard(rank=rank, suit=suit)


def test_not_using_suit_class_results_in_exception():
    rank = Rank.VII
    suit = "HEARTS"

    with pytest.raises(BadSuitException):
        HungarianCard(rank=rank, suit=suit)
