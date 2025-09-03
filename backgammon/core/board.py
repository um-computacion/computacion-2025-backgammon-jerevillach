class Board:
    """Representa el tablero de Backgammon con 24 puntos."""

    def __init__(self):
        self.__puntos__ = [0] * 24

    def reset_board(self):
        """
        Inicializa el tablero en estado vacío (todas las posiciones con 0).
        """
        self.__puntos__ = [0] * 24
        return self.__puntos__
