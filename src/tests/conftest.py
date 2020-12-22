import pytest
from game.hungarian_deck import HungarianDeck


@pytest.fixture(scope="function")
def deck():
    return HungarianDeck()
