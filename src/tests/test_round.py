import pytest
from unittest.mock import MagicMock
from typing import List

from game.hungarian_deck.card import HungarianCard
from game.hungarian_deck.ranks import Rank
from game.hungarian_deck.suits import Suit
from game.hungarian_deck.utils import next_card
from game.player_base import PlayerBase
from game.round import Round
from tests.test_card import test_not_using_rank_class_results_in_exception


def get_prepped_player(name: str, cards: List[HungarianCard]) -> PlayerBase:

    player = MagicMock(PlayerBase)
    player.cards = cards
    player.__len__.return_value = len(cards)
    player.id = name

    return player


def get_cards_for(suit: Suit):
    return [HungarianCard(rank, suit) for rank in Rank if rank is not Rank.UNKNOWN_RANK]


def get_multiple_prepped_players(names_and_suits) -> List[PlayerBase]:
    return [
        get_prepped_player(n_a_s[0], get_cards_for(n_a_s[1]))
        for n_a_s in names_and_suits
    ]


def get_4_prepped_players() -> List[PlayerBase]:
    names = ["Kata", "Máté", "Pest", "Réka"]
    suits = [Suit.HEARTS, Suit.LEAVES, Suit.BELLS, Suit.ACORNS]
    return get_multiple_prepped_players(zip(names, suits))


def test_round_can_be_initiated_with_4_players():
    players = get_4_prepped_players()

    round = Round(players=players, player_won_callback=(lambda: None))

    assert True


def test_round_cannot_be_created_with_less_than_four_players():
    names = ["Kata", "Máté", "Peti"]
    suits_less = [Suit.HEARTS, Suit.ACORNS, Suit.BELLS]
    players_less = get_multiple_prepped_players(zip(names, suits_less))

    with pytest.raises(RuntimeError) as e:
        Round(players_less, lambda: None)
    assert "wrong number of players" in str(e)


def test_round_cannot_be_created_with_more_than_four_players():
    names = ["Kata", "Máté", "Peti"]
    suits = [Suit.HEARTS, Suit.ACORNS, Suit.BELLS]
    players = get_multiple_prepped_players(zip(names, suits))

    with pytest.raises(RuntimeError) as e:
        Round(players, lambda: None)
    assert "wrong number of players" in str(e)


def test_first_card_sets_the_valid_cards():
    players = get_4_prepped_players()
    p1 = players[0]
    round = Round(players=players, player_won_callback=(lambda: None))
    first_card = round.get_cards_of(p1.id)[0]

    round.play_card(first_card)

    p1.remove_card.assert_called_once_with(first_card)
    assert next_card(first_card) in round.valid_next_moves()
    assert (
        HungarianCard(Rank.UNKNOWN_RANK, Suit.UNKNOWN_SUIT)
        not in round.valid_next_moves()
    )


def test_player_won_callback_called_when_player_runs_out_of_cards():
    players = get_4_prepped_players()
    callback_function = MagicMock()
    round = Round(players, callback_function)
    p1 = round.current_player
    # all but 1 card left
    p1_only_card = p1.cards[0]
    p1.cards = [p1_only_card]

    round.play_card(p1_only_card)

    callback_function.assert_called_once_with()