from traffic_light import TrafficLight
from red_state import RedState
from green_state import GreenState
from yellow_state import YellowState

trafficLight = TrafficLight()

trafficLight.cambiar_state(RedState())
trafficLight.switch()

trafficLight.cambiar_state(YellowState())
trafficLight.switch()

trafficLight.cambiar_state(GreenState())
trafficLight.switch()