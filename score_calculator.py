from collections import Counter
from enum import Enum, auto


class Category(Enum):
    # Sección superior
    ONES   = auto()
    TWOS   = auto()
    THREES = auto()
    FOURS  = auto()
    FIVES  = auto()
    SIXES  = auto()
    # Sección inferior
    THREE_OF_A_KIND = auto()
    FOUR_OF_A_KIND  = auto()
    FULL_HOUSE      = auto()
    SMALL_STRAIGHT  = auto()
    LARGE_STRAIGHT  = auto()
    YAHTZEE         = auto()
    CHANCE          = auto()

    def display_name(self) -> str:
        names = {
            Category.ONES:           "Unos",
            Category.TWOS:           "Doses",
            Category.THREES:         "Treses",
            Category.FOURS:          "Cuatros",
            Category.FIVES:          "Cincos",
            Category.SIXES:          "Seises",
            Category.THREE_OF_A_KIND:"Trío",
            Category.FOUR_OF_A_KIND: "Póker",
            Category.FULL_HOUSE:     "Full House",
            Category.SMALL_STRAIGHT: "Escalera Pequeña",
            Category.LARGE_STRAIGHT: "Escalera Grande",
            Category.YAHTZEE:        "Yahtzee",
            Category.CHANCE:         "Chance",
        }
        return names[self]


class ScoreCalculator:
    """Calcula la puntuación de una mano para cada categoría."""

    @staticmethod
    def calculate(values: list[int], category: Category) -> int:
        freq = Counter(values)
        total = sum(values)
        counts = list(freq.values())
        unique = set(values)

        match category:
            case Category.ONES:   return sum(v for v in values if v == 1)
            case Category.TWOS:   return sum(v for v in values if v == 2)
            case Category.THREES: return sum(v for v in values if v == 3)
            case Category.FOURS:  return sum(v for v in values if v == 4)
            case Category.FIVES:  return sum(v for v in values if v == 5)
            case Category.SIXES:  return sum(v for v in values if v == 6)

            case Category.THREE_OF_A_KIND:
                return total if max(counts) >= 3 else 0

            case Category.FOUR_OF_A_KIND:
                return total if max(counts) >= 4 else 0

            case Category.FULL_HOUSE:
                return 25 if sorted(counts) == [2, 3] else 0

            case Category.SMALL_STRAIGHT:
                straights = [{1,2,3,4}, {2,3,4,5}, {3,4,5,6}]
                return 30 if any(s.issubset(unique) for s in straights) else 0

            case Category.LARGE_STRAIGHT:
                return 40 if unique in ({1,2,3,4,5}, {2,3,4,5,6}) else 0

            case Category.YAHTZEE:
                return 50 if max(counts) == 5 else 0

            case Category.CHANCE:
                return total

    @staticmethod
    def best_category(values: list[int], available: set[Category]) -> Category:
        """Retorna la categoría disponible que da más puntos con esta mano."""
        return max(available, key=lambda cat: ScoreCalculator.calculate(values, cat))

