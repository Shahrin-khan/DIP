import numpy as np
from skimage.morphology import binary_dilation as bwdilate
import skimage.data as data
import skimage.exposure as ex
import matplotlib.pyplot as plt
import skimage.io as io


from skimage.morphology import closing, opening, binary_closing as bwclose, binary_opening as bwopen

c = data.binary_blobs()
sel = np.ones((3,3))

test_open = bwopen(c,sel)

test_close = bwclose(c,sel)


io.imshow(test_open)
io.show()

io.imshow(test_close)
io.show
