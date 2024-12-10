from abc import ABC, abstractmethod

# Clase base para Triángulos
class Triangulo(ABC):
    def __init__(self, lados):
        self.lados = lados

    @abstractmethod
    def tipo(self):
        pass


# Productos concretos
class Equilatero(Triangulo):
    def tipo(self):
        return "Equilátero"


class Isosceles(Triangulo):
    def tipo(self):
        return "Isósceles"


class Escaleno(Triangulo):
    def tipo(self):
        return "Escaleno"


# Clase abstracta Factory
class TrianguloFactory(ABC):
    @abstractmethod
    def crear_triangulo(self, lados):
        pass


# Implementación concreta de la fábrica
class TrianguloConcretoFactory(TrianguloFactory):
    def crear_triangulo(self, lados):
        if lados[0] == lados[1] == lados[2]:
            return Equilatero(lados)
        elif lados[0] == lados[1] or lados[1] == lados[2] or lados[0] == lados[2]:
            return Isosceles(lados)
        else:
            return Escaleno(lados)


# Uso del patrón Factory Method
lados = [3, 3, 6]
fabrica = TrianguloConcretoFactory()
triangulo = fabrica.crear_triangulo(lados)
print(f"Triángulo de tipo: {triangulo.tipo()}")
