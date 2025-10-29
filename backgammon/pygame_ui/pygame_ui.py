"""Interfaz gráfica del juego Backgammon usando Pygame."""

import pygame
import random

class PygameUI:
    """Clase que maneja la interfaz visual del juego."""

    def __init__(self, juego):
        pygame.init()
        self.juego = juego
        self.tablero = juego.board
        self.ancho = 800
        self.alto = 600
        self.pantalla = pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption("Backgammon")
        self.reloj = pygame.time.Clock()
        self.ejecutando = True
        self.ficha_seleccionada = None
        self.valores_dados = (0, 0)
        self.boton_rect = pygame.Rect(self.ancho // 2 - 80, self.alto - 80, 160, 50)

    # --------------------------
    # DIBUJADO DEL TABLERO
    # --------------------------
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

    # --------------------------
    # DIBUJADO DE FICHAS
    # --------------------------
    def dibujar_fichas(self, board):
        """Dibuja las fichas correctamente: negras arriba, blancas abajo."""
        color_jugador1 = (255, 255, 255)  # Blancas
        color_jugador2 = (0, 0, 0)        # Negras
        sombra = (60, 60, 60)
        radio = 15
        ancho_punto = self.ancho // 12
        self.tablero = board

        for i, punto in enumerate(board.puntos):
            for j, ficha in enumerate(punto):
                color = color_jugador1 if ficha.jugador == 1 else color_jugador2

                # puntos 0–11 → parte inferior (izquierda a derecha)
                # puntos 12–23 → parte superior (derecha a izquierda)
                if i < 12:
                    # Parte inferior (jugador 1)
                    x = i * ancho_punto + ancho_punto // 2
                    y = self.alto - 100 - j * (radio * 2 + 5)
                else:
                    # Parte superior (jugador 2)
                    x = self.ancho - ((i - 12 + 1) * ancho_punto) + ancho_punto // 2
                    y = 100 + j * (radio * 2 + 5)

                pygame.draw.circle(self.pantalla, sombra, (x + 2, y + 2), radio)
                pygame.draw.circle(self.pantalla, color, (x, y), radio)
                pygame.draw.circle(self.pantalla, (200, 200, 200), (x, y), radio, 2)

    # --------------------------
    # DADOS Y BOTÓN
    # --------------------------
    def dibujar_dados(self):
        """Dibuja los valores actuales de los dados en el centro de la pantalla."""
        if not self.juego.dados:
            return

        font = pygame.font.Font(None, 60)
        color_fondo = (255, 255, 255)
        color_borde = (0, 0, 0)
        color_numero = (0, 0, 0)
        posiciones = [
            (self.ancho // 2 - 90, self.alto // 2 - 30),
            (self.ancho // 2 + 30, self.alto // 2 - 30)
        ]

        for i, valor in enumerate(self.juego.dados):
            x, y = posiciones[i]
            pygame.draw.rect(self.pantalla, color_fondo, (x, y, 60, 60))
            pygame.draw.rect(self.pantalla, color_borde, (x, y, 60, 60), 2)
            texto = font.render(str(valor), True, color_numero)
            texto_rect = texto.get_rect(center=(x + 30, y + 30))
            self.pantalla.blit(texto, texto_rect)

    def dibujar_boton_dados(self):
        """Dibuja el botón para tirar los dados."""
        color_boton = (180, 0, 0)
        color_texto = (255, 255, 255)
        pygame.draw.rect(self.pantalla, color_boton, self.boton_rect, border_radius=10)
        font = pygame.font.Font(None, 36)
        texto = font.render(" Tirar Dados", True, color_texto)
        texto_rect = texto.get_rect(center=self.boton_rect.center)
        self.pantalla.blit(texto, texto_rect)

    # --------------------------
    # EVENTOS DE CLICK
    # --------------------------
    def manejar_click(self, posicion_mouse):
        """Detecta clics en fichas o en el botón de dados."""
        # Clic en el botón de tirar dados
        if self.boton_rect.collidepoint(posicion_mouse):
            self.juego.tirar_dados()
            print(f" Dados tirados: {self.juego.dados}")
            return

        ancho_punto = self.ancho // 12
        punto_index = posicion_mouse[0] // ancho_punto

        # Determinar si el clic fue en la parte superior o inferior
        if posicion_mouse[1] > self.alto // 2:
            # Parte inferior (blancas)
            punto_index = punto_index
        else:
            # Parte superior (negras)
            punto_index = 23 - punto_index

        if self.ficha_seleccionada is None:
            # Selección de ficha
            if 0 <= punto_index < 24 and self.tablero.puntos[punto_index]:
                ficha = self.tablero.puntos[punto_index][-1]
                if ficha.jugador != self.juego.turno_actual:
                    print(" No es tu turno.")
                    return
                self.ficha_seleccionada = punto_index
                print(f"Seleccionaste ficha del jugador {ficha.jugador} en punto {punto_index}")
        else:
            # Intento de movimiento
            origen = self.ficha_seleccionada
            ficha = self.tablero.puntos[origen][-1]

            if self.juego.movimiento_valido(origen, punto_index):
                print(f" Movimiento válido de {origen} a {punto_index}")
                self.ficha_seleccionada = None
                self.juego.cambiar_turno()
                print(f" Turno cambiado: jugador {self.juego.turno_actual}")
            else:
                print(" Movimiento no permitido.")
                self.ficha_seleccionada = None

    # --------------------------
    # LOOP PRINCIPAL
    # --------------------------
    def ejecutar(self):
        """Loop principal del juego."""
        while self.ejecutando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.ejecutando = False
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    self.manejar_click(pygame.mouse.get_pos())

            self.dibujar_tablero()
            self.dibujar_fichas(self.tablero)
            self.dibujar_boton_dados()
            self.dibujar_dados()
            pygame.display.flip()
            self.reloj.tick(30)

        pygame.quit()

