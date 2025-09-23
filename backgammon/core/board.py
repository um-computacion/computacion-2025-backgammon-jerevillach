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
    def add_piece(self, index: int):
        """
        Agrega una ficha en el punto indicado (0-23).
        """
        if 0 <= index < 24:
            self.__puntos__[index] += 1
        return self.__puntos__[index]