import skimage.io as io
from skimage.viewer import ImageViewer as IV
from skimage.color import rgb2gray

img = io.imread('D:\\DIP\\Dataset\\misc\\4.2.07.tiff')

img_gray = rgb2gray(img)

viewer = IV(img_gray)

viewer.show()

