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

    def dibujar_tablero(self):
        """Dibuja el fondo del tablero con triángulos alternados."""
        color_tablero = (205, 133, 63)  # marrón base
        color_tri1 = (255, 255, 255)    # blanco
        color_tri2 = (0, 0, 0)          # negro
        ancho_punto = self.ancho // 12

        # Fondo
        self.pantalla.fill(color_tablero)

        # Triángulos superiores e inferiores
        for i in range(12):
            color = color_tri1 if i % 2 == 0 else color_tri2

            # Triángulos superiores
            puntos_superior = [
                (i * ancho_punto, 0),
                ((i + 1) * ancho_punto, 0),
                (i * ancho_punto + ancho_punto // 2, 150)
            ]
            pygame.draw.polygon(self.pantalla, color, puntos_superior)

            # Triángulos inferiores
            puntos_inferior = [
                (i * ancho_punto, self.alto),
                ((i + 1) * ancho_punto, self.alto),
                (i * ancho_punto + ancho_punto // 2, self.alto - 150)
            ]
            pygame.draw.polygon(self.pantalla, color, puntos_inferior)

    def dibujar_fichas(self):
        """Dibuja las fichas iniciales de los jugadores."""
        color_blanco = (255, 255, 255)
        color_negro = (0, 0, 0)
        radio = 15
        ancho_punto = self.ancho // 12

        # Fichas jugador 1 (superior)
        for i in range(5):
            x = ancho_punto * 2 + i * (radio * 2 + 5)
            y = 200
            pygame.draw.circle(self.pantalla, color_blanco, (x, y), radio)

        # Fichas jugador 2 (inferior)
        for i in range(5):
            x = ancho_punto * 8 + i * (radio * 2 + 5)
            y = self.alto - 200
            pygame.draw.circle(self.pantalla, color_negro, (x, y), radio)

    def ejecutar(self):
        """Loop principal de la interfaz gráfica."""
        while self.ejecutando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.ejecutando = False

            self.dibujar_tablero()
            self.dibujar_fichas()
            pygame.display.flip()
            self.reloj.tick(30)

        pygame.quit()


