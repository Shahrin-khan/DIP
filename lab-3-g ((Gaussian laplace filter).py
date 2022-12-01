import numpy as np
import skimage.io as io
import skimage.data as data
import scipy.ndimage as ndi

img01= data.camera()

io.imshow(img01)
io.show()

img02= ndi.gaussian_laplace(img01,2)

io.imshow(img02)
io.show()
