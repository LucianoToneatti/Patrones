from imagen import Imagen


class Imagen_real(Imagen):
    def __init__(self, archivo):
        self.archivo = archivo
        self.cargar_imagen()

    def cargar_imagen(self):
        print("Cargar imagen", self.archivo)

    def mostrar(self):
        print("Mostrar imagen", self.archivo)