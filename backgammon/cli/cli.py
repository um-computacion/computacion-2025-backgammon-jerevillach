"""Interfaz de línea de comando (CLI) para jugar Backgammon."""

from backgammon.core.game import BackgammonGame

def mostrar_menu():
    print("\n=== BACKGAMMON ===")
    print("1. Tirar dados")
    print("2. Salir")

def main():
    """Ejecuta la versión de consola del juego."""
    print("Bienvenido a Backgammon (CLI)")
    juego = BackgammonGame("Jugador 1", "Jugador 2")

    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            d1, d2 = juego.tirar_dados()
            print(f"Tirada de dados: {d1} y {d2}")
        elif opcion == "2":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida, probá de nuevo.")

if __name__ == "__main__":
    main()
