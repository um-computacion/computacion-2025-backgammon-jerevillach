"""Tests unitarios para la clase BackgammonGame."""

import pytest
from backgammon.core.game import BackgammonGame
from backgammon.core.checker import Checker


@pytest.fixture
def juego():
    """Crea un juego nuevo para pruebas."""
    return BackgammonGame("Jugador 1", "Jugador 2")


def test_tirar_dados_rango_valido(juego):
    """Verifica que los dados estén entre 1 y 6."""
    dados = juego.tirar_dados()
    assert len(dados) == 2
    assert all(1 <= d <= 6 for d in dados)


def test_movimiento_valido_y_turno(juego):
    """Comprueba que un movimiento válido se ejecute correctamente."""
    juego.dados = [3]
    origen = 23
    destino = 20
    juego.board.puntos[23] = [Checker(1, 23)]
    assert juego.movimiento_valido(origen, destino) is True
    assert len(juego.board.puntos[20]) == 1


def test_movimiento_invalido_por_turno(juego):
    """Evita mover fichas del jugador equivocado."""
    juego.turno_actual = 2
    juego.dados = [2]
    juego.board.puntos[23] = [Checker(1, 23)]
    assert juego.movimiento_valido(23, 21) is False


def test_cambio_turno_automatico(juego):
    """Verifica el cambio de turno al usar ambos dados."""
    juego.dados = [3, 4]
    juego.board.puntos[23] = [Checker(1, 23)]
    juego.movimiento_valido(23, 20)
    juego.dados = []
    juego.cambiar_turno()
    assert juego.turno_actual == 2


def test_guardar_y_cargar_en_redis(juego):
    """Guarda y carga correctamente el estado del juego."""
    juego.dados = [2, 5]
    juego.guardar_en_redis()

    nuevo_juego = BackgammonGame("Jugador 1", "Jugador 2")
    nuevo_juego.cargar_desde_redis()

    assert nuevo_juego.dados == [2, 5]
    assert nuevo_juego.turno_actual == juego.turno_actual

