from __future__ import annotations
from random import sample
from string import ascii_letters
from memento import MementoConcreto, Memento


class Originador:
    """
    El Originador guarda un estado importante que puede cambiar con el tiempo.
    Define métodos para guardar el estado en un memento y para restaurarlo desde uno.
    """

    _estado = None

    def __init__(self, estado: str) -> None:
        self._estado = estado
        print(f"Originador: Mi estado inicial es: {self._estado}")

    def hacer_algo(self) -> None:
        """
        La lógica del negocio del Originador puede afectar su estado interno.
        Por lo tanto, el cliente debería hacer un respaldo antes de ejecutar
        estos métodos mediante el método guardar().
        """

        print("Originador: Estoy haciendo algo importante.")
        self._estado = self._generar_cadena_aleatoria(30)
        print(f"Originador: y mi estado ha cambiado a: {self._estado}")

    @staticmethod
    def _generar_cadena_aleatoria(longitud: int = 10) -> str:
        return "".join(sample(ascii_letters, longitud))

    def guardar(self) -> Memento:
        """
        Guarda el estado actual dentro de un memento.
        """
        return MementoConcreto(self._estado)

    def restaurar(self, memento: Memento) -> None:
        """
        Restaura el estado del Originador desde un objeto memento.
        """
        self._estado = memento.obtener_estado()
        print(f"Originador: Mi estado ha cambiado a: {self._estado}")
