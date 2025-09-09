class Player:
    """Representa a un jugador con sus fichas."""
    def __init__(self, nombre: str):
        self.__nombre__ = nombre
        self.__fichas__ = 15
    def add_checker(self):
        """
        Agrega una ficha al jugador.
        """
        self.__fichas__ += 1
        return self.__fichas__

 
   
