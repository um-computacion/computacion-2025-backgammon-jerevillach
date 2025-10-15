"""Representa el tablero del juego Backgammon."""

from backgammon.core.checker import Checker

class Board:
    """Tablero con 24 puntos que pueden contener fichas."""
    def __init__(self):
        # Cada punto del tablero será una lista de fichas (checkers)
        self.__puntos__ = [[] for _ in range(24)]

    def agregar_ficha(self, color, posicion):
        """Agrega una ficha de cierto color en una posición del tablero."""
        if 0 <= posicion < 24:
            ficha = Checker(color, posicion)
            self.__puntos__[posicion].append(ficha)

    def obtener_fichas_en_punto(self, posicion):
        """Devuelve la cantidad de fichas en una posición."""
        if 0 <= posicion < 24:
            return len(self.__puntos__[posicion])
        return 0

    def reset_board(self):
        """Vacía todas las posiciones del tablero."""
        self.__puntos__ = [[] for _ in range(24)]
        return self.__puntos__
