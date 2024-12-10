from imagen import Imagen
from imagen_real import Imagen_real


class ProxyImagen(Imagen):
    def __init__(self, archivo):
        self.archivo = archivo
        self.imagen_real = None

    def mostrar(self):
        if not self.imagen_real:
            print("[ProxyImagen] Creando la instancia de ImagenReal.")
            self.imagen_real = Imagen_real(self.archivo)
        self.imagen_real.mostrar()