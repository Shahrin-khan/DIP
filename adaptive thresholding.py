import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import skimage.exposure as ex

f = io.imread('D:\\DIP\\Dataset\\misc\\7.1.05.tiff')


r,c = f.shape

x,y = np.mgrid[0:r, 0:c]

p = 255 - f + y/2

io.imshow(ex.rescale_intensity(p,out_range=(0.0,1.0)),cmap='gray')
io.show()
