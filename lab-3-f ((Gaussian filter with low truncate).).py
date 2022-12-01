import numpy as np
import skimage.io as io
import skimage.data as data
import scipy.ndimage as ndi

img01= data.camera()

io.imshow(img01)
io.show()

x=np.zeros((5,5))
x[2,2]=1

f=ndi.gaussian_filter(x,1,truncate=2)

img02= ndi.convolve(img01,f)

io.imshow(img02)
io.show()
