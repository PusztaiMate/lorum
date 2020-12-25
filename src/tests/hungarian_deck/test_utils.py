from game.hungarian_deck import HungarianCard, Rank, Suit, next_card


def test_next_card_returns_next_in_line_with_same_suit():

    card = next_card(HungarianCard(Rank.VII, Suit.BELLS))

    assert card == HungarianCard(Rank.VIII, Suit.BELLS)


def test_next_card_work_when_going_from_ACE_to_VII():
    card = next_card(HungarianCard(Rank.ACE, Suit.BELLS))

    assert card == HungarianCard(Rank.VII, Suit.BELLS)
