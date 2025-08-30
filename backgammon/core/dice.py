import random

class Dice:
    """Representa dos dados de seis caras."""
    def roll(self):
        return random.randint(1, 6), random.randint(1, 6)
