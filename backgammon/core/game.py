"""Lógica central del juego Backgammon con persistencia en Redis."""

import random
import redis
import json
from backgammon.core.board import Board
from backgammon.core.checker import Checker


class BackgammonGame:
    """Coordina el flujo general del juego, dados, turnos y guardado en Redis."""

    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.turno_actual = 1  # 1 = jugador1 (blancas), 2 = jugador2 (negras)
        self.board = Board()
        self.dados = []
        self.dados_usados = []

        # Conexión a Redis
        try:
            self.redis_client = redis.Redis(host="localhost", port=6379, db=0)
        except redis.ConnectionError:
            print("No se pudo conectar a Redis.")
            self.redis_client = None

        # Distribución inicial estándar
        # Jugador 1 (blancas)
        self.board.puntos[23] = [Checker(1, 23) for _ in range(2)]
        self.board.puntos[12] = [Checker(1, 12) for _ in range(5)]
        self.board.puntos[7] = [Checker(1, 7) for _ in range(3)]
        self.board.puntos[5] = [Checker(1, 5) for _ in range(5)]

        # Jugador 2 (negras)
        self.board.puntos[0] = [Checker(2, 0) for _ in range(2)]
        self.board.puntos[11] = [Checker(2, 11) for _ in range(5)]
        self.board.puntos[16] = [Checker(2, 16) for _ in range(3)]
        self.board.puntos[18] = [Checker(2, 18) for _ in range(5)]

    # ------------------------------
    # Dados
    # ------------------------------
    def tirar_dados(self):
        """Tira los dados y guarda los resultados."""
        self.dados = [random.randint(1, 6), random.randint(1, 6)]
        self.dados_usados = []
        print(f"Dados tirados: {self.dados}")
        return tuple(self.dados)

    def mostrar_info_turno(self):
        """Devuelve texto informativo del turno y los dados."""
        jugador = self.jugador1 if self.turno_actual == 1 else self.jugador2
        if not self.dados:
            return f"Turno de {jugador} - todavía no tiró los dados."
        return f"Turno de {jugador} - Dados: {self.dados[0]} y {self.dados[1]}"

    # ------------------------------
    # Movimiento y validación
    # ------------------------------
    def movimiento_valido(self, origen, destino):
        """Valida si un movimiento es posible según los dados y el turno."""
        if not self.dados:
            print("Primero debés tirar los dados.")
            return False

        if not self.board.puntos[origen]:
            print("No hay fichas en ese punto.")
            return False

        ficha = self.board.puntos[origen][-1]

        # Validar que la ficha pertenece al jugador actual
        if ficha.jugador != self.turno_actual:
            print("Esa ficha no te pertenece.")
            return False

        # Calcular distancia de movimiento (sin dirección negativa)
        distancia = abs(destino - origen)

        if distancia == 0:
            print("Movimiento inválido: origen y destino son iguales.")
            return False

        if distancia not in self.dados:
            print(f"Movimiento inválido: la distancia {distancia} no coincide con los dados {self.dados}.")
            return False

        # Mover ficha
        self.board.puntos[origen].pop()
        self.board.puntos[destino].append(ficha)
        self.dados.remove(distancia)
        self.dados_usados.append(distancia)
        print(f"Ficha {'blanca' if ficha.jugador == 1 else 'negra'} movida de {origen} a {destino}")

        # Turno automático cuando no quedan dados
        if not self.dados:
            self.cambiar_turno()
        return True

    # ------------------------------
    # Turnos
    # ------------------------------
    def cambiar_turno(self):
        """Alterna el turno entre los jugadores."""
        self.turno_actual = 2 if self.turno_actual == 1 else 1
        jugador = self.jugador1 if self.turno_actual == 1 else self.jugador2
        print(f"Turno cambiado: ahora juega {jugador}")

    # ------------------------------
    # Persistencia en Redis
    # ------------------------------
    def guardar_en_redis(self):
        """Guarda el estado actual del juego en Redis."""
        if not self.redis_client:
            print("Redis no está disponible.")
            return

        estado = {
            "turno": self.turno_actual,
            "dados": self.dados,
            "puntos": [[f.jugador for f in punto] for punto in self.board.puntos],
        }

        self.redis_client.set("backgammon_partida", json.dumps(estado))
        print("Partida guardada en Redis.")

    def cargar_desde_redis(self):
        """Carga el estado del juego desde Redis."""
        if not self.redis_client:
            print("Redis no está disponible.")
            return

        data = self.redis_client.get("backgammon_partida")
        if not data:
            print("No hay partida guardada en Redis.")
            return

        estado = json.loads(data)
        self.turno_actual = estado["turno"]
        self.dados = estado["dados"]

        # Reconstruir fichas
        self.board.puntos = []
        for i, punto in enumerate(estado["puntos"]):
            self.board.puntos.append([Checker(j, i) for j in punto])

        print("Partida restaurada desde Redis.")
