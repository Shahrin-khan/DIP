import numpy as np
import skimage.io as io
import skimage.data as data
import skimage.util.noise as noise
import scipy.ndimage as ndi


img01= data.camera()

io.imshow(img01)
io.show()

img02= noise.random_noise(img01,mode='gaussian') 
io.imshow(img02)
io.show()

f=np.ones((3,3))/9
img03= ndi.convolve(img02, f, mode='constant')
io.imshow(img03,cmap='gray')
io.show()
