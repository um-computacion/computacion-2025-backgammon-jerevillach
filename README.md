# Backgammon Project
Este proyecto implementa el juego de **Backgammon** en Python.  
Incluye una versión de línea de comando (CLI) y una versión gráfica con Pygame.
## Requisitos
- Python 3.12 o superior  
- Pygame (`pip install pygame`)  
- Redis (`sudo apt install redis-server`)  
- pytest (`pip install pytest`)
## Estructura del proyecto
backgammon/core/ → lógica del juego
backgammon/cli/ → interfaz por consola
backgammon/pygame_ui/ → interfaz gráfica con Pygame
backgammon/tests/ → pruebas unitarias
yaml
## Cómo ejecutar en modo CLI
```bash
python -m backgammon.cli.cli
"para jugar desde la terminal"
"inicia el servidor redis"
sudo service redis-server start
ejecuta el juego
python main.py
elegi el jugar nueva partida
y despues si queres iniciar una nueva partida haces lo mismo o reaunudas la partida que estabas jugando

