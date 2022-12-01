import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt

img = io.imread('D:\\DIP\\Dataset\\misc\\7.2.01.tiff')

io.imshow(img)
io.show()
f = plt.figure()
f.show(plt.hist(img.flatten(), bins=256))

plt.show()
