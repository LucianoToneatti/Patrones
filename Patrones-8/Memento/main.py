from originator import Originador
from caretaker import Cuidador

if __name__ == "__main__":
    originador = Originador("Estado-inicial-del-Originador")
    cuidador = Cuidador(originador)

    cuidador.hacer_respaldo()
    originador.hacer_algo()

    cuidador.hacer_respaldo()
    originador.hacer_algo()

    cuidador.hacer_respaldo()
    originador.hacer_algo()

    print()
    cuidador.mostrar_historial()

    print("\nCliente: ¡Ahora retrocedamos!\n")
    cuidador.deshacer()

    print("\nCliente: ¡Una vez más!\n")
    cuidador.deshacer()
