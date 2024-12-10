
from traffic_light_state import TrafficLightState

class RedState(TrafficLightState):
    def switch(self):
        print("Esta en rojo")