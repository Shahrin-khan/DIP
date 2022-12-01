import numpy as np
import skimage.io as io
import skimage.data as data
import skimage.util.noise as noise
import scipy.ndimage as ndi


img01= data.camera()

io.imshow(img01)
io.show()

img02= noise.random_noise(img01,mode='speckle') 
io.imshow(img02)
io.show()


img03=ndi.gaussian_filter(img02,5,truncate=3) 
io.imshow(img03,cmap='gray')
io.show()
