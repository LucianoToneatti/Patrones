from abc import ABC, abstractmethod
from component import ComponenteConcretoA, ComponenteConcretoB


class Visitante(ABC):
    """
    La Interfaz Visitante declara un conjunto de métodos de visita que
    corresponden a las clases de los componentes. La firma de un método
    de visita permite al visitante identificar la clase exacta del componente
    con el que está trabajando.
    """

    @abstractmethod
    def visitar_componente_concreto_a(self, elemento: ComponenteConcretoA) -> None:
        pass

    @abstractmethod
    def visitar_componente_concreto_b(self, elemento: ComponenteConcretoB) -> None:
        pass


class VisitanteConcreto1(Visitante):
    def visitar_componente_concreto_a(self, elemento: ComponenteConcretoA) -> None:
        print(f"{elemento.metodo_exclusivo_de_componente_a()} + VisitanteConcreto1")

    def visitar_componente_concreto_b(self, elemento: ComponenteConcretoB) -> None:
        print(f"{elemento.metodo_especial_de_componente_b()} + VisitanteConcreto1")


class VisitanteConcreto2(Visitante):
    def visitar_componente_concreto_a(self, elemento: ComponenteConcretoA) -> None:
        print(f"{elemento.metodo_exclusivo_de_componente_a()} + VisitanteConcreto2")

    def visitar_componente_concreto_b(self, elemento: ComponenteConcretoB) -> None:
        print(f"{elemento.metodo_especial_de_componente_b()} + VisitanteConcreto2")
