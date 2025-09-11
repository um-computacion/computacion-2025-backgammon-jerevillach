from .board import Board
from .player import Player
from .dice import Dice

class BackgammonGame:
    """Coordina el flujo general del juego."""

    def __init__(self, jugador1: str, jugador2: str):
        self.__board__ = Board()
        self.__player1__ = Player(jugador1)
        self.__player2__ = Player(jugador2)
        self.__dice__ = Dice()

    def tirar_dados(self):
        """
        Llama a los dados y devuelve el resultado de la tirada.
        """
        return self.__dice__.roll()
