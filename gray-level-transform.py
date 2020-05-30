from PIL import Image
from pylab import *

INTERVAL_END = 255.0
INTERVAL_START = 100.0
NEGATION_C = 255

originalImage = array(Image.open('images/doctor.jpg').convert('L'))
gray()
negativeImage = NEGATION_C - originalImage
clampedImage = (INTERVAL_START / NEGATION_C) * originalImage + INTERVAL_START
transformedImage = INTERVAL_END * (originalImage / INTERVAL_END) ** 2

imshow(transformedImage)
show()
