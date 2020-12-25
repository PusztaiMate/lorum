import pytest

from game.rulesets.lorum.gameflow import GameFlowException, SequentialGameFlow


def test_if_not_explicitly_set_up_first_player_is_the_current_player():
    players = ["p1", "p2", "p3", "p4"]

    flow = SequentialGameFlow(players=players)

    assert flow.current_player == "p1"


def test_shift_players_shifts_to_the_current_player_to_following_player():
    players = ["p1", "p2", "p3", "p4"]
    flow = SequentialGameFlow(players=players)

    flow.shift_players()

    assert flow.current_player == "p2"


def test_current_player_can_be_set_to_anyone_with_shift_players_to_function():
    players = ["p1", "p2", "p3", "p4"]
    flow = SequentialGameFlow(players=players)

    flow.shift_players_to(player="p3")

    assert flow.current_player == "p3"


def test_shift_players_to_throws_exception_when_player_not_found():
    players = ["p1", "p2", "p3", "p4"]
    flow = SequentialGameFlow(players=players)

    with pytest.raises(GameFlowException) as e:
        flow.shift_players_to(player="p5")

    assert "player 'p5' not found" in str(e)