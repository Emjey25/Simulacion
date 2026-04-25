from score_calculator import Category


class SimulationLogger:
    """Maneja toda la salida en consola. Separar logging de lógica permite silenciarlo fácilmente."""

    def __init__(self, verbose: bool = True):
        self.verbose = verbose

    def log_game_start(self, number: int):
        print("\n" + "═" * 60)
        print(f"  🎲  SIMULACIÓN YAHTZEE — Partida #{number}")
        print("═" * 60)

    def log_turn_start(self, name: str):
        if self.verbose:
            print(f"\n── Turno de {name} ──")

    def log_roll(self, roll_num: int, dice):
        if self.verbose:
            print(f"  Lanzamiento {roll_num}: {dice}")

    def log_keep(self, dice):
        if self.verbose:
            print(f"  Guarda (*):    {dice}")

    def log_score(self, name: str, category: Category, score: int):
        print(f"  {name:<12} → {category.display_name():<20}: {score:>2} pts")

    def log_final_scores(self, p1, p2):
        print("\n" + "─" * 60)
        print("  MARCADOR FINAL")
        print("─" * 60)
        self._print_score_card(p1)
        print()
        self._print_score_card(p2)

    def _print_score_card(self, player):
        print(f"\n  {player.name.upper()}")
        print(f"  {'Categoría':<24} {'Pts':>4}")
        print("  " + "-" * 30)
        for cat in Category:
            score = player.score_card.get(cat)
            val   = str(score) if score is not None else "-"
            print(f"  {cat.display_name():<24} {val:>4}")
        upper = player.upper_section_sum()
        bonus = 35 if upper >= 63 else 0
        bonus_str = "(+35! ✓)" if bonus else ""
        print(f"  {'Bonus superior':<24} {upper}/63 {bonus_str}")
        print(f"  {'TOTAL':<24} {player.total_score():>4}")

    def log_winner(self, p1, p2):
        print("\n" + "═" * 60)
        s1, s2 = p1.total_score(), p2.total_score()
        if s1 > s2:
            print(f"  🏆  GANADOR: {p1.name}  ({s1} vs {s2} pts)")
        elif s2 > s1:
            print(f"  🏆  GANADOR: {p2.name}  ({s2} vs {s1} pts)")
        else:
            print(f"  🤝  EMPATE: {s1} puntos cada uno")
        print("═" * 60)

    def log_montecarlo_stats(self, sims, p1_wins, p2_wins, ties, avg1, avg2):
        print("\n" + "═" * 60)
        print(f"  📊  RESULTADOS MONTECARLO ({sims:,} simulaciones)")
        print("═" * 60)
        print(f"  IA-1 victorias  : {p1_wins:>6,}  ({100*p1_wins/sims:.1f}%)")
        print(f"  IA-2 victorias  : {p2_wins:>6,}  ({100*p2_wins/sims:.1f}%)")
        print(f"  Empates         : {ties:>6,}  ({100*ties/sims:.1f}%)")
        print(f"  Puntaje prom. IA-1: {avg1:.2f} pts")
        print(f"  Puntaje prom. IA-2: {avg2:.2f} pts")
        print("═" * 60)
