"""Punto de entrada del juego Backgammon."""

import random
import pygame
from backgammon.cli.cli import ejecutar_cli
from backgammon.pygame_ui.pygame_ui import PygameUI
from backgammon.core.board import Board
from backgammon.core.checker import Checker


def main():
    """Menú principal del juego."""
    print("=== BACKGAMMON ===")
    print("1. Jugar en modo CLI")
    print("2. Jugar en modo gráfico (Pygame)")
    opcion = input("Elegí una opción: ")

    if opcion == "1":
        ejecutar_cli()

    elif opcion == "2":
        # Crear tablero y colocar fichas de ejemplo
        tablero = Board()

        # Fichas del Jugador 1 (blancas) arriba
        tablero.puntos[0] = [Checker(1, 0) for _ in range(5)]
        tablero.puntos[5] = [Checker(1, 5) for _ in range(3)]

        # Fichas del Jugador 2 (negras) abajo
        tablero.puntos[23] = [Checker(2, 23) for _ in range(5)]
        tablero.puntos[18] = [Checker(2, 18) for _ in range(3)]

        # Iniciar interfaz gráfica
        interfaz = PygameUI()

        # Mostrar tirada de dados al comienzo
        valores_dados = [random.randint(1, 6), random.randint(1, 6)]
        interfaz.dibujar_tablero()
        interfaz.dibujar_dados(valores_dados)
        pygame.time.wait(2000)

        # Entrar al loop principal
        interfaz.ejecutar(tablero)

    else:
        print("Opción inválida.")


if __name__ == "__main__":
    main()







