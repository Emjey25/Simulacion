"""
╔══════════════════════════════════════════════════════╗
║      SIMULACIÓN YAHTZEE — MÉTODO DE MONTECARLO       ║
║      Actividad Didáctica 2-M1 | Simulación           ║
╚══════════════════════════════════════════════════════╝

Método de Montecarlo:
  Cada dado lanza random.randint(1, 6) → distribución uniforme U(1,6).
  Repetir la partida N veces estima empíricamente probabilidades
  que serían muy difíciles de calcular analíticamente.

Flujo:
  1. Partida de demostración con logs detallados.
  2. 10.000 simulaciones silenciosas → estadísticas finales.
"""

from game import YahtzeeGame
from logger import SimulationLogger
from montecarlo import MontecarloSimulator


def main():
    # ── Fase 1: Partida de demostración ───────────────────────────────────
    verbose_logger = SimulationLogger(verbose=True)
    verbose_logger.log_game_start(1)

    demo = YahtzeeGame("IA-1", "IA-2", verbose_logger)
    demo.play()

    # ── Fase 2: Simulación Montecarlo ─────────────────────────────────────
    simulator = MontecarloSimulator(simulations=1_000)
    result    = simulator.run()

    verbose_logger.log_montecarlo_stats(
        result.simulations,
        result.p1_wins,
        result.p2_wins,
        result.ties,
        result.avg_p1,
        result.avg_p2,
    )


if __name__ == "__main__":
    main()
