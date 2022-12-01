import skimage.io as io
import skimage.color as co


img = io.imread('D:\\DIP\\Dataset\\misc\\4.1.07.tiff')
io.imshow(img)
io.show()

#[r,c] = co.rgb2ind(img)

io.imshow(co.rgb2ind(img))
io.show()
