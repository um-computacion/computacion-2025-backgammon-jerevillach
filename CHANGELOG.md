
Todas las modificaciones importantes de este proyecto se documentarán en este archivo.

## [0.1.0] - 2025-08-31

- Estructura inicial del proyecto.
- Clases base: Board, Player, Dice y BackgammonGame.
- Test inicial para dados.
## [0.2.0] - 2025-09-11
- Método `reset_board()` en Board.
- Método `add_checker()` en Player.
- Método `tirar_dados()` en BackgammonGame.
- Tests para Board, Player y BackgammonGame.
- Archivos de registro: prompts-testing.md y prompts-documentacion.md.
## [0.2.1] - 2025-09-22
- Se agregó el método `add_piece()` en Board.
- Se agregó un test para verificar `add_piece()`.
## [0.2.2] - 2025-10-13
- Clase `Checker` creada con color y posición.
- Test unitario para `Checker` en `test_checker.py`.
## [0.2.3] - 2025-10-14
- Board actualizado para manejar fichas (Checkers) en los puntos.
- Tests agregados para verificar integración Board + Checker
## [0.2.4] - 2025-10-22
- Agregado método para dibujar tablero con triángulos.
- Agregado método para mostrar fichas de ambos jugadores en Pygame.
## [0.2.5] - 2025-10-24
- Integración de Board y Checker con la interfaz Pygame.
- Ajuste en main.py para mostrar tablero dinámico.
