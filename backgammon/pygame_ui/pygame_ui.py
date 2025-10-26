"""Interfaz gráfica del juego Backgammon usando Pygame."""

import pygame
import random

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

        # Atributos nuevos para movimiento
        self.ficha_seleccionada = None
        self.tablero = None

    def dibujar_tablero(self):
        """Dibuja el fondo del tablero con triángulos alternados."""
        color_tablero = (205, 133, 63)
        color_tri1 = (255, 255, 255)
        color_tri2 = (0, 0, 0)
        ancho_punto = self.ancho // 12
        self.pantalla.fill(color_tablero)

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

    def dibujar_fichas(self, board):
        """Dibuja las fichas en pantalla según el estado del Board."""
        color_jugador1 = (255, 255, 255)
        color_jugador2 = (0, 0, 0)
        sombra = (60, 60, 60)
        radio = 15
        ancho_punto = self.ancho // 12
        self.tablero = board

        for i, punto in enumerate(board.puntos):
            for j, ficha in enumerate(punto):
                color = color_jugador1 if ficha.jugador == 1 else color_jugador2
                x = i * ancho_punto + ancho_punto // 2
                y = 100 + j * (radio * 2 + 5) if i < 12 else self.alto - 100 - j * (radio * 2 + 5)

                # Dibujar sombra
                pygame.draw.circle(self.pantalla, sombra, (x + 2, y + 2), radio)

                # Dibujar ficha principal
                pygame.draw.circle(self.pantalla, color, (x, y), radio)

                # Borde
                pygame.draw.circle(self.pantalla, (200, 200, 200), (x, y), radio, 2)

    def dibujar_dados(self, valores):
        """Dibuja dos dados con los valores actuales en el centro de la pantalla."""
        font = pygame.font.Font(None, 60)
        color_fondo = (255, 255, 255)
        color_borde = (0, 0, 0)
        color_numero = (0, 0, 0)

        posiciones = [
            (self.ancho // 2 - 90, self.alto // 2 - 30),
            (self.ancho // 2 + 30, self.alto // 2 - 30)
        ]

        for i, valor in enumerate(valores):
            x, y = posiciones[i]
            pygame.draw.rect(self.pantalla, color_fondo, (x, y, 60, 60))
            pygame.draw.rect(self.pantalla, color_borde, (x, y, 60, 60), 2)

            texto = font.render(str(valor), True, color_numero)
            texto_rect = texto.get_rect(center=(x + 30, y + 30))
            self.pantalla.blit(texto, texto_rect)

        pygame.display.flip()

    def manejar_click(self, posicion_mouse):
        """Detecta selección y movimiento básico de fichas."""
        if not self.tablero:
            return

        ancho_punto = self.ancho // 12
        punto_index = posicion_mouse[0] // ancho_punto

        if self.ficha_seleccionada is None:
            if self.tablero.puntos[punto_index]:
                self.ficha_seleccionada = punto_index
        else:
            ficha = self.tablero.puntos[self.ficha_seleccionada].pop()
            self.tablero.puntos[punto_index].append(ficha)
            self.ficha_seleccionada = None

    def ejecutar(self, board):
        """Loop principal con detección de clics."""
        self.tablero = board
        while self.ejecutando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.ejecutando = False
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    self.manejar_click(pygame.mouse.get_pos())

            self.dibujar_tablero()
            self.dibujar_fichas(board)
            pygame.display.flip()
            self.reloj.tick(30)

        pygame.quit()


   
