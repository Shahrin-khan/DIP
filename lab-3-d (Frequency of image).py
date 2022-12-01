import numpy as np
import skimage.io as io
import skimage.data as data
import scipy.ndimage as ndi

img01= data.camera()

io.imshow(img01)
io.show()

f = np.array([[1.5,6,1.5],[6,-30,6],[1.5,6,1.5]])

img02= ndi.convolve(img01,f)

io.imshow(img02)
io.show()
