import numpy as np
from skimage.morphology import binary_dilation as bwdilate
import skimage.data as data
import skimage.exposure as ex
import matplotlib.pyplot as plt
import skimage.io as io
import skimage.morphology as mo

c = data.camera()

str = mo.square(5)

cd = mo.dilation(c,str)

ce = mo.erosion(c,str)

io.imshow(cd)
io.show()

io.imshow(ce)
io.show()
