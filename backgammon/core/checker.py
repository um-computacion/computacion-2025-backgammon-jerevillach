"""Representa una ficha (checker) del juego Backgammon."""

class Checker:
    """Cada ficha pertenece a un jugador y ocupa una posición del tablero."""

    def __init__(self, jugador, posicion):
        # jugador: 1 o 2
        # posicion: índice (0–23) del punto en el tablero
        self.jugador = jugador
        self.posicion = posicion

    def mover(self, nueva_posicion):
        """Cambia la posición de la ficha."""
        self.posicion = nueva_posicion

