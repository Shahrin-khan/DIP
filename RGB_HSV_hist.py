import skimage.io as io
import matplotlib.pyplot as plt
from skimage.color import convert_colorspace
import skimage.exposure as ex

img = io.imread('D:\\DIP\\Dataset\\misc\\4.2.07.tiff')
io.imshow(img)
io.show()

f1 = plt.figure()
f1.show(plt.hist(img.flatten(), bins=256))
plt.show()

img_hsv = convert_colorspace(img, 'RGB','HSV')
io.imshow(img_hsv)
io.show()

f2 = plt.figure()
f2.show(plt.hist(img_hsv.flatten(), bins=256))
plt.show()

img2= ex.equalize_hist(img_hsv)

io.imshow(img2)
io.show()
f3 = plt.figure()
f3.show(plt.hist(img2.flatten(), bins=256))
plt.show()

img_rgb = convert_colorspace(img2, 'HSV','RGB')
io.imshow(img_rgb)
io.show()
