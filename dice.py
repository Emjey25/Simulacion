import random

class Dice:
    """
    Representa un dado de 6 caras.
    El lanzamiento usa distribución uniforme discreta U(1,6) — núcleo del método Montecarlo.
    """

    def __init__(self):
        self.value = 0
        self.kept = False

    def roll(self):
        """Lanza el dado solo si no está guardado por la IA."""
        if not self.kept:
            self.value = random.randint(1, 6)  # U(1,6) uniforme

    def reset(self):
        self.value = 0
        self.kept = False

    def __repr__(self):
        marker = "*" if self.kept else ""
        return f"[{self.value}{marker}]"
