class Player:
    """Jugador de Backgammon.
    Guarda el nombre y la cantidad de fichas del jugador y permite sumar o quitar fichas.
    """
class Player:
    """Representa a un jugador con sus fichas."""

    def __init__(self, nombre: str):
        self.__nombre__ = nombre
        self.__fichas__ = 15

    def add_checker(self):
        self.__fichas__ += 1
        return self.__fichas__

    def remove_checker(self):
        """
        Resta una ficha al jugador (si tiene fichas disponibles).
        """
        if self.__fichas__ > 0:
            self.__fichas__ -= 1
        return self.__fichas__


 
   
