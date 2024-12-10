from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from visitor import Visitor


class Componente(ABC):
    """
    La interfaz Componente declara un método `aceptar` que debe tomar
    la interfaz del visitante base como argumento.
    """

    @abstractmethod
    def aceptar(self, visitante: Visitor) -> None:
        pass


class ComponenteConcretoA(Componente):
    """
    Cada Componente Concreto debe implementar el método `aceptar` de manera que
    llame al método del visitante correspondiente a la clase del componente.
    """

    def aceptar(self, visitante: Visitor) -> None:
        """
        Nota que llamamos a `visitar_componente_concreto_a`, que coincide con
        el nombre de la clase actual. De esta manera, dejamos que el visitante
        sepa la clase del componente con la que trabaja.
        """

        visitante.visitar_componente_concreto_a(self)

    def metodo_exclusivo_de_componente_a(self) -> str:
        """
        Los Componentes Concretos pueden tener métodos especiales que no existen
        en su clase base o interfaz. El Visitante puede usar estos métodos
        porque conoce la clase concreta del componente.
        """

        return "A"


class ComponenteConcretoB(Componente):
    """
    Lo mismo aquí: visitar_componente_concreto_b => ComponenteConcretoB
    """

    def aceptar(self, visitante: Visitor) -> None:
        visitante.visitar_componente_concreto_b(self)

    def metodo_especial_de_componente_b(self) -> str:
        return "B"


