import scipy.ndimage
from PIL import Image

originalImage = Image.open('images/man_and_child.jpg')
b = scipy.ndimage.filters.median_filter(originalImage, size=5, footprint= None,output=None, mode='reflect', cval=0.0, origin=0)
b = Image.fromarray(b)

b.save('images/median_man_and_child.jpg')
