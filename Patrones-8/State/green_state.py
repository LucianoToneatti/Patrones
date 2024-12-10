
from traffic_light_state import TrafficLightState

class GreenState(TrafficLightState):
    def switch(self):
        print("Esta en verde")