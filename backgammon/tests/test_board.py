import unittest
from backgammon.core.board import Board

class TestBoard(unittest.TestCase):
    def test_reset_board(self):
        board = Board()
        estado = board.reset_board()
        self.assertEqual(len(estado), 24)
        self.assertTrue(all(p == 0 for p in estado))

if __name__ == "__main__":
    unittest.main()
