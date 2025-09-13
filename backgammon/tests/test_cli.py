import unittest
from io import StringIO
from unittest.mock import patch
from backgammon.cli import cli

class TestCLI(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_cli_output(self, mock_stdout):
        cli.main()
        salida = mock_stdout.getvalue()
        self.assertIn("Tirada de dados", salida)

if __name__ == "__main__":
    unittest.main()
