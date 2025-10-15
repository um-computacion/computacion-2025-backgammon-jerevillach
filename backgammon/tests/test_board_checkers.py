"""Prueba la integración entre Board y Checker."""

import unittest
from backgammon.core.board import Board

class TestBoardCheckers(unittest.TestCase):
    """Verifica que el tablero pueda agregar fichas correctamente."""

    def test_agregar_ficha(self):
        tablero = Board()
        tablero.agregar_ficha("blanco", 3)
        self.assertEqual(tablero.obtener_fichas_en_punto(3), 1)

    def test_reset_board(self):
        tablero = Board()
        tablero.agregar_ficha("negro", 10)
        tablero.reset_board()
        total_fichas = sum(tablero.obtener_fichas_en_punto(i) for i in range(24))
        self.assertEqual(total_fichas, 0)


if __name__ == "__main__":
    unittest.main()
