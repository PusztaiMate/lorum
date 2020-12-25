from game.hungarian_deck.card import HungarianCard
from game.hungarian_deck.deck import HungarianDeck
from game.hungarian_deck.ranks import Rank
from game.hungarian_deck.suits import Suit
from game.rulesets.lorum.gamestate import GameState, GameStateException


def test_first(players, deck):
    state = GameState(players=players, deck=deck)

    assert True


def test_init_new_round_gives_8_cards_per_player_in_case_of_4_players(players, deck):
    state = GameState(players=players, deck=deck)

    state.init_new_round()

    assert len(state.cards_of("p1")) == 8


def test_after_init_new_round_resets_stacks(players, deck):
    state = GameState(players, deck)

    state.init_new_round()

    for suit in (Suit.ACORNS, Suit.BELLS, Suit.LEAVES, Suit.HEARTS):
        assert len(state.stack(suit)) == 0


def test_next_valid_moves_can_be_queried(players, deck):
    state = GameState(players, deck)
    state.init_new_round()

    valid_moves = state.valid_next_moves()

    assert len(valid_moves) == 4
    for card in valid_moves:
        assert card.rank == Rank.UNKNOWN_RANK


def test_valid_moves_update_after_a_valid_card_is_played(players, deck):
    state = GameState(players, deck)
    state.init_new_round()

    # every card is still not ranked
    for card in state.valid_next_moves():
        assert card.rank == Rank.UNKNOWN_RANK

    hearts_vii = HungarianCard(Rank.VII, Suit.HEARTS)
    state.place_card_on_stack(hearts_vii)

    valid_moves = state.valid_next_moves()
    assert len(valid_moves) == 4
    assert HungarianCard(Rank.VIII, Suit.HEARTS) in valid_moves
    assert HungarianCard(Rank.VII, Suit.LEAVES) in valid_moves
    assert HungarianCard(Rank.VII, Suit.ACORNS) in valid_moves
    assert HungarianCard(Rank.VII, Suit.BELLS) in valid_moves