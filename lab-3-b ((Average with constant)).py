import numpy as np
import skimage.io as io
import skimage.data as data
import scipy.ndimage as ndi

img01= data.camera()

io.imshow(img01)
io.show()
f=np.ones((9,9))/81

img02= ndi.convolve(img01, f, mode='reflect')

io.imshow(img02)
io.show()
