"""Interfaz gráfica del juego Backgammon usando Pygame."""

import pygame

class PygameUI:
    """Clase que maneja la interfaz visual del juego."""

    def __init__(self):
        pygame.init()
        self.ancho = 800
        self.alto = 600
        self.pantalla = pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption("Backgammon")
        self.reloj = pygame.time.Clock()
        self.ejecutando = True

    def mostrar_tablero(self):
        """Dibuja las fichas en sus posiciones iniciales básicas."""
        color_jugador1 = (255, 255, 255)  # blanco
        color_jugador2 = (0, 0, 0)        # negro
        radio = 15

        # Fichas jugador 1
        for i in range(5):
            x = 50 + i * 40
            y = 100
            pygame.draw.circle(self.pantalla, color_jugador1, (x, y), radio)

        # Fichas jugador 2
        for i in range(5):
            x = 50 + i * 40
            y = 500
            pygame.draw.circle(self.pantalla, color_jugador2, (x, y), radio)

        pygame.display.flip()

    def ejecutar(self):
        """Loop principal de la interfaz gráfica."""
        while self.ejecutando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.ejecutando = False

            self.mostrar_tablero()
            self.reloj.tick(30)

        pygame.quit()

