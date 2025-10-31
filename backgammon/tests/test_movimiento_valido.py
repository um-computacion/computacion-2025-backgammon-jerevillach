import unittest
from backgammon.core.game import BackgammonGame

class TestMovimientoValido(unittest.TestCase):
    def setUp(self):
        self.juego = BackgammonGame("Jugador1", "Jugador2")

    def test_movimiento_valido_con_dado(self):
        self.juego.dados = [3, 5]
        self.juego.board.puntos[0].append(self.juego.board.puntos[0][0])  # asegurar ficha
        valido = self.juego.movimiento_valido(0, 3)
        self.assertTrue(valido)

    def test_movimiento_invalido_distancia(self):
        self.juego.dados = [2, 6]
        invalido = self.juego.movimiento_valido(0, 5)
        self.assertFalse(invalido)
