from itertools import cycle
from typing import List
from copy import deepcopy
from collections.abc import Callable

from game.hungarian_deck import HungarianDeck
from game.hungarian_deck.card import HungarianCard
from game.hungarian_deck.ranks import Rank
from game.hungarian_deck.stack import Stack
from game.hungarian_deck.suits import Suit
from game.player_base import PlayerBase


class InvalidMove(Exception):
    pass


class Round:
    def __init__(
        self, players: list[PlayerBase], player_won_callback: Callable[[], []]
    ) -> None:
        if len(players) != 4:
            raise RuntimeError("wrong number of players (should be 4)")

        self.players = players
        self.player_won_callback = player_won_callback

        self._stacks = {
            suit: Stack(suit=suit) for suit in Suit if suit != Suit.UNKNOWN_SUIT
        }

        self._player_cycle = cycle(players)
        self.current_player = next(self._player_cycle)

        self._first_card_played = False

    def get_cards_of(self, player_id) -> List[HungarianCard]:
        for player in self.players:
            if player.id == player_id:
                return player.cards

    def play_card(self, card: HungarianCard) -> None:
        # pass
        if card is None:
            if not self._first_card_played:
                raise InvalidMove(f"first play can't pass")
            self._shift_to_next_player()
            return

        # first card is not played yet
        if not self._first_card_played:
            for stack in self._stacks.values():
                stack.starting_rank = card.rank
            self._first_card_played = True

        # pass
        if card is None:
            self._shift_to_next_player()
            return

        self._check_play_validity(card)
        self._play_card(card)
        # player won
        if len(self.current_player.cards) == 0:
            self.player_won_callback()
            return
        self._shift_to_next_player()

    def valid_next_moves(self) -> List[HungarianCard]:
        return [
            stack.next_card()
            for stack in self._stacks.values()
            if stack.next_card() is not None
        ]

    def _play_card(self, card):
        self._stacks[card.suit].put(card)
        self.current_player.remove_card(card)

    def _shift_to_next_player(self):
        self.current_player = next(self._player_cycle)

    def _check_play_validity(self, card):
        if not self._current_player_owns_card(card):
            raise InvalidMove(f"player {self.current_player} does not own card {card}")

        if not self._valid_as_next_move(card):
            raise InvalidMove(f"card {card} is not a valid move")

    def _current_player_owns_card(self, card):
        return card in self.current_player.cards

    def _valid_as_next_move(self, card):
        return card in self.valid_next_moves()
