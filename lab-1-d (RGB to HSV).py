import skimage.io as io
from skimage.viewer import ImageViewer as IV
from skimage.color import convert_colorspace

img = io.imread('D:\\DIP\\Dataset\\misc\\4.2.07.tiff')

img_hsv = convert_colorspace(img, 'RGB','HSV')

viewer = IV(img_hsv)

viewer.show()

