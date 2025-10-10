"""Punto de entrada del juego Backgammon."""

from backgammon.cli.cli import ejecutar_cli
from backgammon.pygame_ui.pygame_ui import PygameUI

def main():
    print("=== BACKGAMMON ===")
    print("1. Jugar en modo CLI")
    print("2. Jugar en modo gráfico (Pygame)")
    opcion = input("Elegí una opción: ")

    if opcion == "1":
        ejecutar_cli()
    elif opcion == "2":
        interfaz = PygameUI()
        interfaz.ejecutar()
    else:
        print("Opción inválida.")

if __name__ == "__main__":
    main()




