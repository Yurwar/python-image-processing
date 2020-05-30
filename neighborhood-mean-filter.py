import numpy
from PIL import Image
import scipy.ndimage

originalImage = Image.open('images/man_and_child.jpg').convert('L')

koef = numpy.ones((5, 5)) / 25
b = scipy.ndimage.filters.convolve(originalImage, koef)
b = Image.fromarray(b)
b.save('images/mean_man_and_child.jpg')
