from auto import Auto

class AutoBuilder:
    def __init__(self):
        self.auto = Auto()

    def set_motor(self, motor):
        self.auto.motor = motor

    def set_marca(self, marca):
        self.auto.marca = marca

    def set_modelo(self, modelo):
        self.auto.modelo = modelo

    def set_puertas(self, puertas):
        self.auto.puertas = puertas

    def get_auto(self):
        return self.auto