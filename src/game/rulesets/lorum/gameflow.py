from itertools import cycle


class GameFlowException(RuntimeError):
    pass


class SequentialGameFlow:
    def __init__(self, players):
        self._players = players
        self._players_cycle = cycle(players)

        self.current_player = next(self._players_cycle)

    def shift_players(self) -> None:
        self.current_player = next(self._players_cycle)

    def shift_players_to(self, player):
        if player not in self._players:
            raise GameFlowException(f"player '{player}' not found")
        else:
            while self.current_player != player:
                self.shift_players()
