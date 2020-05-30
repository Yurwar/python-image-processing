import cv2.cv2 as cv2
from matplotlib import pyplot

image = cv2.imread('images/man_feels_aversion.jpg', 0)

sobelX = cv2.Sobel(image, -1, 1, 0, ksize=5)

sobelY = cv2.Sobel(image, -1, 0, 1, ksize=5)

pyplot.imshow(sobelX, cmap='gray')
# pyplot.imshow(sobelY, cmap='gray')
pyplot.show()
