from os import listdir
from ctypes import windll
from time import sleep
from lib.lifx import matchDesktopBackground
from lifxlan.multizonelight import MultiZoneLight

MAC_ADDRESS = "YOUR_MAC_ADDRESS"
IP_ADDRESS = "YOUR_IP_ADDRESS"

light = MultiZoneLight(MAC_ADDRESS, IP_ADDRESS)

PATH = "D:\\Media\\Photos\\Backgrounds\\LIFX"
photos = listdir(PATH)
photos = map(lambda x: '{0}\\{1}'.format(PATH, x), photos)
for photo in photos:
	windll.user32.SystemParametersInfoW(20, 0, photo, 0)
	matchDesktopBackground(light, photo)
	sleep(2.6)