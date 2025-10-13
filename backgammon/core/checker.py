"""Representa una ficha (checker) del juego Backgammon."""

class Checker:
    """Cada ficha pertenece a un jugador y tiene una posición."""
    def __init__(self, color, posicion):
        self.__color__ = color          # Color del jugador (ej: 'blanco' o 'negro')
        self.__posicion__ = posicion    # Posición actual en el tablero (0 a 23)

    def mover(self, nueva_posicion):
        """Mueve la ficha a una nueva posición."""
        self.__posicion__ = nueva_posicion

    def obtener_color(self):
        """Devuelve el color de la ficha."""
        return self.__color__

    def obtener_posicion(self):
        """Devuelve la posición actual de la ficha."""
        return self.__posicion__
