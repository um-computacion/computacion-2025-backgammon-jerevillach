import unittest
from backgammon.core.player import Player

class TestPlayer(unittest.TestCase):
    def test_player_initial_fichas(self):
        jugador = Player("Jeremías")
        self.assertEqual(jugador.__fichas__, 15)

if __name__ == "__main__":
    unittest.main()
