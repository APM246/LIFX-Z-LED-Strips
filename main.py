from lib.lifx import matchDesktopBackground
from lifxlan.multizonelight import MultiZoneLight

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, help='path to image file instead of reading windows registry for current desktop background image')
args = parser.parse_args()

MAC_ADDRESS = "YOUR_MAC_ADDRESS"
IP_ADDRESS = "YOUR_IP_ADDRESS"

light = MultiZoneLight(MAC_ADDRESS, IP_ADDRESS)
light.set_power(True)
matchDesktopBackground(light, args.path)