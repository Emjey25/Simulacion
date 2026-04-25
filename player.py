from dice import Dice
from score_calculator import Category, ScoreCalculator
from ai_strategy import AIStrategy


class Player:
    """Jugador IA que ejecuta turnos automáticamente."""

    UPPER_CATEGORIES = {
        Category.ONES, Category.TWOS, Category.THREES,
        Category.FOURS, Category.FIVES, Category.SIXES
    }

    def __init__(self, name: str):
        self.name = name
        self.score_card: dict[Category, int] = {}
        self.dice = [Dice() for _ in range(5)]

    def play_turn(self, logger=None) -> Category | None:
        available = self.available_categories()
        if not available:
            return None

        # Resetear dados
        for d in self.dice:
            d.reset()

        if logger:
            logger.log_turn_start(self.name)

        for roll_num in range(1, 4):
            # Lanzar dados no guardados
            for d in self.dice:
                d.roll()

            if logger:
                logger.log_roll(roll_num, self.dice)

            if roll_num < 3:
                keep = AIStrategy.decide_keep(self.dice, available)
                for i, d in enumerate(self.dice):
                    d.kept = keep[i]

                if logger:
                    logger.log_keep(self.dice)

                # Si todos guardados, no tiene sentido relanzar
                if all(d.kept for d in self.dice):
                    break

        # Elegir la mejor categoría con la mano final
        values = [d.value for d in self.dice]
        chosen = ScoreCalculator.best_category(values, available)
        score  = ScoreCalculator.calculate(values, chosen)

        self.score_card[chosen] = score

        if logger:
            logger.log_score(self.name, chosen, score)

        return chosen

    def total_score(self) -> int:
        base  = sum(self.score_card.values())
        upper = sum(self.score_card.get(c, 0) for c in self.UPPER_CATEGORIES)
        bonus = 35 if upper >= 63 else 0
        return base + bonus

    def upper_section_sum(self) -> int:
        return sum(self.score_card.get(c, 0) for c in self.UPPER_CATEGORIES)

    def has_finished(self) -> bool:
        return len(self.score_card) == len(Category)

    def available_categories(self) -> set[Category]:
        return set(Category) - set(self.score_card.keys())
