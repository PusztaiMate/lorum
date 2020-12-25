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


def test_equal_works_currectly():
    card_one = HungarianCard(Rank.VII, Suit.HEARTS)
    card_two = HungarianCard(Rank.VII, Suit.HEARTS)

    assert card_one == card_two

    card_three = HungarianCard(Rank.ACE, Suit.HEARTS)

    assert card_three != card_one
    assert card_three != card_two


def test_hash_works_correctly():
    card_one = HungarianCard(Rank.VII, Suit.HEARTS)
    card_two = HungarianCard(Rank.VII, Suit.HEARTS)

    assert hash(card_one) == hash(card_two)
    assert len(set([card_one, card_two])) == 1


def test_card_has_a_nice_string_representation():
    card = HungarianCard(Rank.VII, Suit.HEARTS)

    assert "Card(VII, HEARTS)" == str(card)


def test_card_has_a_repr_set():
    card = HungarianCard(Rank.VII, Suit.HEARTS)

    assert "<Card(Rank.VII, Suit.HEARTS)>" == repr(card)
