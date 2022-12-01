import numpy as np
import skimage.io as io
import scipy.ndimage as ndi

img01= io.imread('D:\\DIP\\Dataset\\misc\\7.2.01.tiff')

io.imshow(img01)
io.show()

f=np.ones((3,3))/9

img02= ndi.convolve(img01, f, mode='constant')

io.imshow(img02)
io.show()
