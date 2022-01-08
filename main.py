from lib.lifx import matchDesktopBackground
from lifxlan.multizonelight import MultiZoneLight

MAC_ADDRESS = "YOUR_MAC_ADDRESS"
IP_ADDRESS = "YOUR_IP_ADDRESS"

light = MultiZoneLight(MAC_ADDRESS, IP_ADDRESS)
light.set_power(True)
matchDesktopBackground(light)