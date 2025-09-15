# Justificación del Proyecto Backgammon

## Resumen del diseño general
El juego se diseñó separando la **lógica central** (core) de las **interfaces de usuario** (CLI y Pygame).

## Justificación de las clases elegidas
- **Board**: Representa los puntos del tablero (24 posiciones).
- **Player**: Representa a un jugador con sus fichas.
- **Dice**: Encargado de las tiradas de dados.
- **BackgammonGame**: Coordina el flujo general del juego.

## Justificación de atributos
- `__puntos__`: para guardar el estado del tablero.  
- `__nombre__`: identifica al jugador.  
- `__fichas__`: controla cuántas fichas tiene cada jugador.  

## Decisiones de diseño relevantes
- Separación lógica/UI para poder usar CLI y Pygame sin duplicar código.  

## Excepciones y manejo de errores
A definir en próximas versiones.

## Estrategia de testing
Se comenzó con pruebas unitarias de la clase `Dice` y se agregará cobertura para el resto.

## Principios SOLID
- **S**: cada clase tiene una responsabilidad única.  
- **O**: el diseño permitirá extender interfaces sin modificar la lógica.  
### Nuevas decisiones de diseño
- Se agregó el método `remove_checker()` en Player para manejar la lógica de quitar fichas.
- Se agregaron tests correspondientes para asegurar el correcto funcionamiento.


