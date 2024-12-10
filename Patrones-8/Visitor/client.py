from typing import List
from component import Componente, ComponenteConcretoA, ComponenteConcretoB
from visitor import VisitanteConcreto1, VisitanteConcreto2


def codigo_cliente(componentes: List[Componente], visitante) -> None:
    """
    El código del cliente puede ejecutar operaciones de visitante sobre cualquier
    conjunto de elementos sin preocuparse por sus clases concretas. La operación
    aceptar dirige la llamada al método apropiado en el objeto visitante.
    """

    for componente in componentes:
        componente.aceptar(visitante)


if __name__ == "__main__":
    componentes = [ComponenteConcretoA(), ComponenteConcretoB()]

    print("El código del cliente trabaja con todos los visitantes a través de la interfaz base Visitante:")
    visitante1 = VisitanteConcreto1()
    codigo_cliente(componentes, visitante1)

    print("\nPermite que el mismo código del cliente trabaje con diferentes tipos de visitantes:")
    visitante2 = VisitanteConcreto2()
    codigo_cliente(componentes, visitante2)
