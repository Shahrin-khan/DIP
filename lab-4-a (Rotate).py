import skimage.io as io
import skimage.data as data
import skimage.transform as tr

c = data.camera()
cr = tr.rotate(c,-50,order=3)

io.imshow(cr, cmap='gray')
io.show()



