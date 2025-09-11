import unittest
from backgammon.core.game import BackgammonGame

class TestBackgammonGame(unittest.TestCase):
    def test_tirar_dados(self):
        juego = BackgammonGame("Jugador1", "Jugador2")
        d1, d2 = juego.tirar_dados()
        self.assertTrue(1 <= d1 <= 6)
        self.assertTrue(1 <= d2 <= 6)

if __name__ == "__main__":
    unittest.main()
