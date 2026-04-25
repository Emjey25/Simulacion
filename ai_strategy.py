from collections import Counter
from dice import Dice
from score_calculator import Category, ScoreCalculator


class AIStrategy:
    """
    Estrategia greedy de la IA.
    Evalúa la mejor categoría alcanzable y guarda los dados
    que más contribzuyen a conseguirla.
    """

    @staticmethod
    def decide_keep(dice: list[Dice], available: set[Category]) -> list[bool]:
        values = [d.value for d in dice]
        target = ScoreCalculator.best_category(values, available)
        score  = ScoreCalculator.calculate(values, target)

        # Si ya tenemos un puntaje alto, guardar todo
        if score >= 40:
            return [True] * 5

        keep = [False] * 5

        match target:
            case Category.ONES:   AIStrategy._keep_value(dice, keep, 1)
            case Category.TWOS:   AIStrategy._keep_value(dice, keep, 2)
            case Category.THREES: AIStrategy._keep_value(dice, keep, 3)
            case Category.FOURS:  AIStrategy._keep_value(dice, keep, 4)
            case Category.FIVES:  AIStrategy._keep_value(dice, keep, 5)
            case Category.SIXES:  AIStrategy._keep_value(dice, keep, 6)

            case Category.YAHTZEE | Category.THREE_OF_A_KIND | Category.FOUR_OF_A_KIND:
                AIStrategy._keep_most_frequent(dice, keep)

            case Category.FULL_HOUSE:
                AIStrategy._keep_for_full_house(dice, keep)

            case Category.SMALL_STRAIGHT | Category.LARGE_STRAIGHT:
                AIStrategy._keep_for_straight(dice, keep)

            case Category.CHANCE:
                keep = [True] * 5  # Guardar todo, suma todos los dados

        return keep

    # ── Helpers privados ────────────────────────────────────────────────────

    @staticmethod
    def _keep_value(dice, keep, value):
        for i, d in enumerate(dice):
            keep[i] = d.value == value

    @staticmethod
    def _keep_most_frequent(dice, keep):
        freq = Counter(d.value for d in dice)
        most_common = freq.most_common(1)[0][0]
        AIStrategy._keep_value(dice, keep, most_common)

    @staticmethod
    def _keep_for_full_house(dice, keep):
        freq = Counter(d.value for d in dice)
        for i, d in enumerate(dice):
            keep[i] = freq[d.value] >= 2

    @staticmethod
    def _keep_for_straight(dice, keep):
        seen = set()
        for i, d in enumerate(dice):
            if d.value not in seen:
                keep[i] = True
                seen.add(d.value)
