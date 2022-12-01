import numpy as np
import skimage.io as io
import skimage.exposure as ex
import matplotlib.pyplot as plt

img01= io.imread('D:\\DIP\\Dataset\\misc\\7.2.01.tiff')

io.imshow(img01)
io.show()

img02= ex.adjust_gamma(img01,0.5)

io.imshow(img02)
io.show()

f = plt.figure()
f.show(plt.hist(img02.flatten(), bins=256))

plt.show()
