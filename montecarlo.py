import time
from dataclasses import dataclass
from game import YahtzeeGame
from logger import SimulationLogger


@dataclass
class SimulationResult:
    simulations: int
    p1_wins:     int
    p2_wins:     int
    ties:        int
    avg_p1:      float
    avg_p2:      float


class MontecarloSimulator:
    """
    Simulador de Montecarlo para Yahtzee.

    Principio: repetir un experimento aleatorio N veces para
    estimar probabilidades empíricamente. Aquí cada dado usa
    distribución uniforme U(1,6), base del método de Montecarlo.
    """

    def __init__(self, simulations: int = 10_000):
        self.simulations = simulations

    def run(self) -> SimulationResult:
        p1_wins = p2_wins = ties = 0
        total_p1 = total_p2 = 0
        silent = SimulationLogger(verbose=False)

        print(f"\nEjecutando {self.simulations:,} simulaciones de Montecarlo...")
        start = time.time()

        for i in range(self.simulations):
            game   = YahtzeeGame("IA-1", "IA-2", silent)
            winner = game.play()

            total_p1 += game.player1.total_score()
            total_p2 += game.player2.total_score()

            if winner is None:              ties   += 1
            elif winner.name == "IA-1":     p1_wins += 1
            else:                           p2_wins += 1

            # Mostrar progreso cada 10%
            step = self.simulations // 10
            if step > 0 and (i + 1) % step == 0:
                pct = (i + 1) * 100 // self.simulations
                print(f"  {pct}% completado...")

        elapsed = time.time() - start
        print(f"Completado en {elapsed:.2f} s.")

        return SimulationResult(
            simulations = self.simulations,
            p1_wins     = p1_wins,
            p2_wins     = p2_wins,
            ties        = ties,
            avg_p1      = total_p1 / self.simulations,
            avg_p2      = total_p2 / self.simulations,
        )
