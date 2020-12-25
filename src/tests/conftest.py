import pytest
from game.hungarian_deck import HungarianDeck


@pytest.fixture(scope="function")
def deck():
    return HungarianDeck()


@pytest.fixture(scope="function")
def players():
    return ["p1", "p2", "p3", "p4"]
