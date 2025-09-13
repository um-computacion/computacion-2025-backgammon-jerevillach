from backgammon.core.game import BackgammonGame

def main():
    print("Bienvenido a Backgammon (CLI)")
    juego = BackgammonGame("Jugador1", "Jugador2")
    d1, d2 = juego.tirar_dados()
    print(f"Tirada de dados: {d1} y {d2}")

if __name__ == "__main__":
    main()
