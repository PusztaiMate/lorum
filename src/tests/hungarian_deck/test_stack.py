from pluggy.hooks import _HookCaller
import pytest
from game.hungarian_deck import Stack, Suit, Rank, HungarianCard
from game.hungarian_deck.stack import StackFullException, WrongCardException
from game.hungarian_deck.suits import BadSuitException
from game.hungarian_deck.utils import next_card


def test_stack_can_be_initialized_with_suit():
    heart_stack = Stack(Suit.HEARTS)

    assert True, "couldn't initialize deck"
    assert heart_stack.suit == Suit.HEARTS


def test_stack_throws_exception_if_not_suit_type_is_given_as_suit():
    with pytest.raises(TypeError) as e:
        Stack(suit="Heart")
    assert "new value is not type Suit" in str(e)


def test_stack_starting_rank_can_be_set():
    stack = Stack(Suit.LEAVES)

    stack.starting_rank = Rank.VII

    assert stack.starting_rank == Rank.VII


def test_setting_starting_rank_sets_starting_card():
    stack = Stack(Suit.LEAVES)

    stack.starting_rank = Rank.VII

    assert stack.next_card() == HungarianCard(Rank.VII, Suit.LEAVES)


def test_after_setting_starting_card_the_next_card_in_line_can_be_put_onto_the_stack():
    stack = Stack(Suit.LEAVES)
    stack.starting_rank = Rank.VII
    assert len(stack) == 0

    stack.put(HungarianCard(Rank.VII, Suit.LEAVES))

    assert len(stack) == 1


def test_putting_card_with_different_suit_causes_exception():
    stack = Stack(Suit.ACORNS)
    stack.starting_rank = Rank.VII

    with pytest.raises(WrongCardException) as e:
        stack.put(HungarianCard(Rank.VIII, Suit.HEARTS))

    assert "next card should be" in str(e)


def test_putting_the_wrong_rank_to_the_stack_causes_WrongCardException():
    stack = Stack(Suit.ACORNS)
    stack.starting_rank = Rank.VII

    with pytest.raises(WrongCardException) as e:
        # VIII should be the next one
        stack.put(HungarianCard(Rank.IX, Suit.ACORNS))

    assert "next card should be" in str(e)


def test_putting_more_cards_than_the_maximum_causes_StackFullException():
    stack = Stack(Suit.ACORNS, max_stack_size=8)
    stack.starting_rank = Rank.VII

    # this should be ok the stack can hold 8
    for _ in range(8):
        stack.put(stack.next_card())

    with pytest.raises(StackFullException) as e:
        stack.put(next_card(stack.top_card))


def test_next_card_returns_starting_card_if_stack_is_empty():
    stack = Stack(Suit.ACORNS, max_stack_size=8)
    stack.starting_rank = Rank.VII

    assert HungarianCard(Rank.VII, Suit.ACORNS) == stack.next_card()


def test_next_card_gives_the_next_valid_card():
    stack = Stack(Suit.ACORNS, max_stack_size=8)
    stack.starting_rank = Rank.VII

    stack.put(HungarianCard(Rank.VII, Suit.ACORNS))
    stack.put(HungarianCard(Rank.VIII, Suit.ACORNS))

    assert HungarianCard(Rank.IX, Suit.ACORNS) == stack.next_card()