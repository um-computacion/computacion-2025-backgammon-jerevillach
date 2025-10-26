"""Lógica central del juego Backgammon."""

import random
from backgammon.core.board import Board
from backgammon.core.checker import Checker


class BackgammonGame:
    """Coordina el flujo general del juego y la lógica de turnos."""

    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.turno_actual = 1  # 1 = jugador1, 2 = jugador2
        self.board = Board()
        self.dados = []
        self.dados_usados = []

        # Configurar fichas iniciales (simplificado)
        self.board.puntos[0] = [Checker(1, 0) for _ in range(2)]
        self.board.puntos[23] = [Checker(2, 23) for _ in range(2)]

    def tirar_dados(self):
        """Tira dos dados y guarda los valores."""
        self.dados = [random.randint(1, 6), random.randint(1, 6)]
        self.dados_usados = []
        print(f"Dados: {self.dados}")
        return self.dados

    def movimiento_valido(self, origen, destino):
        """Valida si un movimiento es posible según los dados disponibles."""
        if not self.dados:
            print("Primero debes tirar los dados.")
            return False

        distancia = abs(destino - origen)
        if distancia not in self.dados:
            print(f"Movimiento inválido: la distancia {distancia} no coincide con ningún dado {self.dados}.")
            return False

        # Verificar si hay fichas en el punto de origen
        if not self.board.puntos[origen]:
            print("No hay fichas en ese punto.")
            return False

        ficha = self.board.puntos[origen][-1]

        # Verificar si pertenece al jugador actual
        if ficha.jugador != self.turno_actual:
            print("Esa ficha no te pertenece.")
            return False

        # Si todo es válido, mover la ficha
        self.board.puntos[origen].pop()
        self.board.puntos[destino].append(ficha)
        self.dados_usados.append(distancia)
        self.dados.remove(distancia)
        print(f"Ficha movida de {origen} a {destino}. Dados restantes: {self.dados}")
        return True

    def cambiar_turno(self):
        """Cambia el turno entre los jugadores."""
        self.turno_actual = 2 if self.turno_actual == 1 else 1
