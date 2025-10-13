"""Pruebas unitarias para la clase Checker."""

import unittest
from backgammon.core.checker import Checker


class TestChecker(unittest.TestCase):
    """Verifica el comportamiento básico de la ficha Checker."""

    def test_creacion_checker(self):
        ficha = Checker("blanco", 5)
        self.assertEqual(ficha.obtener_color(), "blanco")
        self.assertEqual(ficha.obtener_posicion(), 5)

    def test_mover_checker(self):
        ficha = Checker("negro", 10)
        ficha.mover(15)
        self.assertEqual(ficha.obtener_posicion(), 15)


if __name__ == "__main__":
    unittest.main()
