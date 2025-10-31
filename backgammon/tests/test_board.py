import unittest
from backgammon.core.board import Board

class TestBoard(unittest.TestCase):
    def test_reset_board(self):
        board = Board()
        estado = board.reset_board()
        self.assertEqual(len(estado), 24)
        self.assertTrue(all(p == 0 for p in estado))

    def test_add_piece(self):
        board = Board()
        board.reset_board()
        board.add_piece(5)
        self.assertEqual(board._Board__puntos__[5], 1)
if __name__ == "__main__":
    unittest.main()
    