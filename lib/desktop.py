from winreg import CloseKey, OpenKeyEx, QueryValueEx
from winreg import HKEY_CURRENT_USER

from PIL import Image
from colorsys import rgb_to_hsv, hsv_to_rgb

''' Use Windows registry to find path to current desktop background'''
def getDesktopBackgroundPath():
	try:
		key = OpenKeyEx(HKEY_CURRENT_USER, r'Control Panel\\Desktop')
		value = QueryValueEx(key, 'WallPaper')
		if key:
			CloseKey(key)
		return value[0]
	except Exception as e:
		print(e)

''' 
	Use Pillow module to analyse pixels of image. Returns average of MAX_COLOURS most 
	common pixel colours in the image in HSB format (decimals).
'''
def getAverageColour(background_path, max_colours=None):
	image = Image.open(background_path).convert('RGB') # open in RGB format due to additive property
	size = image.size
	colors = list(image.getcolors(size[0]*size[1]))
	colors.sort(key = lambda x: x[0], reverse=True)

	total_pixels = 0
	skipped_pixels = 0
	red_channel = 0
	green_channel = 0
	blue_channel = 0

	if not max_colours:
		max_colours = len(colors)

	for i in range(max_colours):
		num_pixels = colors[i][0]
		# hsv format easier for deducing saturation and brightness
		hsv = rgb_to_hsv(*map(lambda x: x/255, colors[i][1]))

		# skip overly white/black pixels as they corrupt average LED colour
		if hsv[2] < 0.2 or hsv[1] < 0.08:
			skipped_pixels += num_pixels
			continue

		red_channel += num_pixels*colors[i][1][0]
		green_channel += num_pixels*colors[i][1][1]
		blue_channel += num_pixels*colors[i][1][2]
		total_pixels += num_pixels

	print('Total number of pixels: {}, number of pixels ignored due to being too white or black: {}'.
	format(total_pixels, skipped_pixels))
	MAX_VALUE = 255 # max of RGB
	average_rgb = (red_channel, green_channel, blue_channel)
	average_rgb = list(map(lambda x: x/total_pixels/MAX_VALUE, average_rgb))
	return rgb_to_hsv(*average_rgb)