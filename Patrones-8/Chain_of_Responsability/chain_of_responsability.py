# Chain of Responsability
# Permite que una peticion se pase a lo largo de una cadena de objetos
# Cada objeto decide si la maneja o la pasa al siguiente en la cadena
# Reduce el acomplamiento entre el emisor de la peticion y los objetos que la procesan

# Tenemos una interfaz que se va a poder implementar en todas las clases
# Nos sirve para evitar el uso de if-else

# Interfaz

class Aprobador:
    def __init__(self, sucesor=None):
        self.sucesor = sucesor

    def aprobar(self,monto):
        if self.sucesor:
            return self.sucesor.aprobar(monto)
        else:
            print("Nadie pudo aprobar el prestamo")
            return False
    
class EjecutivoCuenta(Aprobador):
    def aprobar(self, monto):
        if monto <= 10000:
            print("El Ejecutivo de Cuenta aprueba el préstamo.")
            return True
        else:
            return super().aprobar(monto)

class Lider(Aprobador):
    def aprobar(self, monto):
        if 10000 < monto <= 50000:
            print("El Líder aprueba el préstamo.")
            return True
        else:
            return super().aprobar(monto)

class Gerente(Aprobador):
    def aprobar(self, monto):
        if 50000 < monto <= 100000:
            print("El Gerente aprueba el préstamo.")
            return True
        else:
            return super().aprobar(monto)

class Director(Aprobador):
    def aprobar(self, monto):
        if monto > 100000:
            print("El Director aprueba el préstamo.")
            return True
        else:
            return super().aprobar(monto)

# Configuración de la cadena de responsabilidad
director = Director()
gerente = Gerente(director)
lider = Lider(gerente)
ejecutivo = EjecutivoCuenta(lider)
cadena = EjecutivoCuenta(Lider(Gerente(Director())))
# Ejemplo de uso
monto = 1000000
cadena.aprobar(monto)