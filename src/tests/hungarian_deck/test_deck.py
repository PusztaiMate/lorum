import pytest
from game.hungarian_deck import HungarianDeck, HungarianCard, card
from game.hungarian_deck.deck import OutOfCardsException


def test_deck_can_be_created():
    deck = HungarianDeck()
    assert True, "couldn't initialize deck"


def test_new_deck_contains_32_cards(deck: HungarianDeck):
    assert len(deck) == 32


def test_card_can_be_drawn_from_deck(deck: HungarianDeck):
    drawn_card = deck.draw()

    assert isinstance(drawn_card, HungarianCard)


def test_many_cards_can_be_drawn(deck: HungarianDeck):
    cards_drawn = deck.draw_many(8)
    unique_cards = set(cards_drawn)

    assert len(cards_drawn) == 8
    assert len(unique_cards) == 8
    assert len(deck) == 24


def test_deck_contains_32_different_cards(deck: HungarianDeck):
    cards = {deck.draw() for _ in range(32)}

    assert len(cards) == 32


def test_drawing_more_than_32_times_causes_exception(deck: HungarianDeck):
    # ok so far
    deck.draw_many(32)

    with pytest.raises(OutOfCardsException) as e:
        deck.draw()
        assert "no cards left" in str(e)


def test_reset_recreates_the_deck(deck: HungarianDeck):
    deck.draw_many(10)

    assert len(deck) == 22

    deck.reset()

    assert len(deck) == 32
