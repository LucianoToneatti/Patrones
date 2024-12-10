class Auto:
    def __init__(self):
        self.motor = None
        self.marca = None
        self.modelo = None
        self.puertas = None

    def __str__(self):
        return f"Auto [Marca={self.marca}, Modelo={self.modelo}, Motor={self.motor}, Puertas={self.puertas}]"