import numpy as np
import skimage.io as io
import skimage.exposure as ex
import matplotlib.pyplot as plt

img1= io.imread('D:\\DIP\\Dataset\\misc\\7.2.01.tiff')

io.imshow(img1)
io.show()

f1 = plt.figure()
f1.show(plt.hist(img1.flatten(), bins=256))
plt.show()

img2= ex.equalize_hist(img1)

io.imshow(img2)
io.show()

f2 = plt.figure()
f2.show(plt.hist(img2.flatten(), bins=256))
plt.show()
