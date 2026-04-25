from player import Player
from logger import SimulationLogger


class YahtzeeGame:
    """Motor de una partida completa (13 rondas)."""

    def __init__(self, name1: str = "IA-1", name2: str = "IA-2", logger: SimulationLogger = None):
        self.player1 = Player(name1)
        self.player2 = Player(name2)
        self.logger  = logger or SimulationLogger(verbose=False)

    def play(self) -> Player | None:
        """Ejecuta las 13 rondas. Retorna el ganador o None si empatan."""
        round_num = 1
        while not self.player1.has_finished() and not self.player2.has_finished():
            if self.logger.verbose:
                print(f"\n  [Ronda {round_num}/13]")
            self.player1.play_turn(self.logger)
            self.player2.play_turn(self.logger)
            round_num += 1

        self.logger.log_final_scores(self.player1, self.player2)
        self.logger.log_winner(self.player1, self.player2)

        s1, s2 = self.player1.total_score(), self.player2.total_score()
        if s1 > s2: return self.player1
        if s2 > s1: return self.player2
        return None  # empate
