from red_state import RedState

class TrafficLight:
    def __init__(self):
        self.state = None

    def cambiar_state(self, state):
        self.state = state

    def switch(self):
        if self.state:
            self.state.switch()
        else:
            print("El semaforo esta apagado")

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state