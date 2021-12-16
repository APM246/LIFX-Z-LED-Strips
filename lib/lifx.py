from lifxlan.multizonelight import MultiZoneLight
from lib.desktop import getDesktopBackgroundPath, getAverageColour

NUM_ZONES = 16
MAX_VALUE = 65535

def matchDesktopBackground(light: MultiZoneLight, photo: str=None):
	photo = getDesktopBackgroundPath() if not photo else photo
	average_hsbk = getAverageColour(photo)

	# LIFX Z accepts values in range 0-65535 for H, S and B
	colour = list(map(lambda x: x * MAX_VALUE, average_hsbk))

	# append colour temp to match HSBK format
	colour.append(3500)

	# set all zones to this colour with a 1 second transition
	light.set_zone_color(0, NUM_ZONES, colour, 600, rapid=False)