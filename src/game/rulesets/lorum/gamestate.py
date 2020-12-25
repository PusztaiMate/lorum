from typing import List
from game.hungarian_deck.ranks import Rank

from game.hungarian_deck.stack import Stack
from ...hungarian_deck import HungarianDeck, Suit, HungarianCard


class GameStateException(RuntimeError):
    pass


class GameState:
    MAX_STACK_SIZE = 8

    def __init__(self, players: list, deck: HungarianDeck) -> None:
        self._player_cards = {p: [] for p in players}
        self._stacks = {
            suit: Stack(suit=suit) for suit in Suit if suit != Suit.UNKNOWN_SUIT
        }

        self._deck = deck

    def init_new_round(self):
        self._deck.reset()
        for player in self._player_cards.keys():
            self._player_cards[player] = self._deck.draw_many(8)

    def cards_of(self, player) -> List[HungarianCard]:
        try:
            return self._player_cards[player]
        except KeyError:
            raise GameStateException(f"players '{player}' not found")

    def stack(self, suit: Suit) -> Stack:
        try:
            return self._stacks[suit]
        except KeyError:
            raise GameStateException(f"suit '{suit}' not found")

    def valid_next_moves(self) -> List[HungarianCard]:
        return [
            stack.next_card()
            for stack in self._stacks.values()
            if stack.next_card() is not None
        ]

    def place_card_on_stack(self, card: HungarianCard) -> None:
        try:
            target_stack = self._stacks[card.suit]
        except KeyError:
            raise GameStateException(f"stack {card.suit} not found")

        if target_stack.starting_rank == Rank.UNKNOWN_RANK:
            for stack in self._stacks.values():
                stack.starting_rank = card.rank

        target_stack.put(card)
