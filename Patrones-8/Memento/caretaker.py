from originator import Originador
from memento import Memento


class Cuidador:
    """
    El Cuidador no depende de la clase MementoConcreto. Por lo tanto,
    no tiene acceso al estado del Originador guardado dentro del memento.
    Trabaja con todos los mementos a través de la interfaz base Memento.
    """

    def __init__(self, originador: Originador) -> None:
        self._mementos = []
        self._originador = originador

    def hacer_respaldo(self) -> None:
        print("\nCuidador: Guardando el estado del Originador...")
        self._mementos.append(self._originador.guardar())

    def deshacer(self) -> None:
        if not self._mementos:
            print("Cuidador: No hay estados guardados.")
            return

        memento = self._mementos.pop()
        print(f"Cuidador: Restaurando estado a: {memento.obtener_nombre()}")
        try:
            self._originador.restaurar(memento)
        except Exception as e:
            print(f"Error al restaurar: {e}")
            self.deshacer()

    def mostrar_historial(self) -> None:
        print("Cuidador: Este es el historial de mementos:")
        for memento in self._mementos:
            print(memento.obtener_nombre())
