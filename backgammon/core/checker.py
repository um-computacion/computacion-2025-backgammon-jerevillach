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
     # Métodos agregados para compatibilidad con los tests
    def obtener_color(self):
        """Devuelve el color textual usado en los tests."""
        if isinstance(self.jugador, str):
            return self.jugador
        return "blanco" if self.jugador == 1 else "negro"

    def obtener_posicion(self):
        """Devuelve la posición actual de la ficha."""
        return self.posicion
   

