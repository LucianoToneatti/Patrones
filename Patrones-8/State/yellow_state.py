
from traffic_light_state import TrafficLightState

class YellowState(TrafficLightState):
    def switch(self):
        print("Esta en amarillo")