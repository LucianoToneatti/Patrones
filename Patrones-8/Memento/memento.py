from abc import ABC, abstractmethod
from datetime import datetime


class Memento(ABC):
    """
    La interfaz Memento proporciona una manera de recuperar los metadatos
    del memento, como la fecha de creación o el nombre. Sin embargo, no expone
    el estado del Originador.
    """

    @abstractmethod
    def obtener_nombre(self) -> str:
        pass

    @abstractmethod
    def obtener_fecha(self) -> str:
        pass


class MementoConcreto(Memento):
    def __init__(self, estado: str) -> None:
        self._estado = estado
        self._fecha = str(datetime.now())[:19]

    def obtener_estado(self) -> str:
        """
        El Originador usa este método al restaurar su estado.
        """
        return self._estado

    def obtener_nombre(self) -> str:
        """
        Los demás métodos son usados por el Cuidador para mostrar metadatos.
        """
        return f"{self._fecha} / ({self._estado[:9]}...)"

    def obtener_fecha(self) -> str:
        return self._fecha
