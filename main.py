"""Punto de entrada del juego Backgammon."""

from backgammon.core.game import BackgammonGame
from backgammon.pygame_ui.pygame_ui import PygameUI
from backgammon.core.checker import Checker


def main():
    """Menú principal del juego Backgammon."""
    print("=== BACKGAMMON ===")
    print("1. Jugar nueva partida")
    print("2. Reanudar partida guardada en Redis")

    opcion = input("Elegí una opción (1 o 2): ").strip()

    # Crear juego
    juego = BackgammonGame("Jugador 1", "Jugador 2")
    tablero = juego.board

    # Distribución inicial clásica (solo si se empieza nuevo juego)
    if opcion == "1":
        # Jugador 1 (blancas)
        tablero.puntos[23] = [Checker(1, 23) for _ in range(2)]  # arriba derecha
        tablero.puntos[12] = [Checker(1, 12) for _ in range(5)]  # arriba izquierda
        tablero.puntos[7] = [Checker(1, 7) for _ in range(3)]    # abajo derecha
        tablero.puntos[5] = [Checker(1, 5) for _ in range(5)]    # abajo izquierda

        # Jugador 2 (negras)
        tablero.puntos[0] = [Checker(2, 0) for _ in range(2)]    # abajo izquierda
        tablero.puntos[11] = [Checker(2, 11) for _ in range(5)]  # abajo derecha
        tablero.puntos[16] = [Checker(2, 16) for _ in range(3)]  # arriba izquierda
        tablero.puntos[18] = [Checker(2, 18) for _ in range(5)]  # arriba derecha

        print("Nueva partida iniciada.")

    elif opcion == "2":
        juego.cargar_desde_redis()
        print("Partida restaurada desde Redis.")
    else:
        print("Opción inválida, se iniciará una nueva partida.")
# Iniciar interfaz gráfica
    interfaz = PygameUI(juego)
    interfaz.ejecutar()  # ✅ sin argumentos

# Guardar el estado actual al salir del juego
    juego.guardar_en_redis()
print("Estado de la partida guardado en Redis. Fin del juego.")

   
if __name__ == "__main__":
    main()






 








