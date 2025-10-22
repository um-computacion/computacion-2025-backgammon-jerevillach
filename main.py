"""Punto de entrada del juego Backgammon."""

from backgammon.cli.cli import ejecutar_cli
from backgammon.pygame_ui.pygame_ui import PygameUI
from backgammon.core.board import Board
from backgammon.core.checker import Checker

def main():
    print("=== BACKGAMMON ===")
    print("1. Jugar en modo CLI")
    print("2. Jugar en modo gráfico (Pygame)")
    opcion = input("Elegí una opción: ")

    if opcion == "1":
        ejecutar_cli()

    elif opcion == "2":
        # Crear el tablero y agregar algunas fichas de ejemplo
        tablero = Board()
        tablero.puntos[0] = [Checker(1) for _ in range(2)]   # Jugador 1
        tablero.puntos[23] = [Checker(2) for _ in range(2)]  # Jugador 2

        interfaz = PygameUI()
        interfaz.dibujar_tablero()
        interfaz.dibujar_fichas(tablero)
        interfaz.ejecutar()

    else:
        print("Opción inválida.")

if __name__ == "__main__":
    main()





