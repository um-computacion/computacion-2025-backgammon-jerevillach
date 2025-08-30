import unittest
from backgammon.core.dice import Dice

class TestDice(unittest.TestCase):
    def test_roll(self):
        dice = Dice()
        d1, d2 = dice.roll()
        self.assertTrue(1 <= d1 <= 6)
        self.assertTrue(1 <= d2 <= 6)

if __name__ == "__main__":
    unittest.main()
