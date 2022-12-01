import skimage.io as io
import skimage.filters as fl
import matplotlib.pyplot as plt
import skimage.exposure as ex
import skimage.util as ut

f = io.imread('D:\\DIP\\Dataset\\misc\\7.1.05.tiff')

s = ut.img_as_float(f)

s_lap = abs(fl.laplace(s))

plt.subplot(2,1,1)
plt.axis('off')
plt.title('Original image')
plt.imshow(ex.rescale_intensity(f,out_range=(0.0,1.0)),cmap='gray')

plt.subplot(2,1,2)
plt.axis('off')
plt.title('Filtered image with Laplacian filter')
plt.imshow(ex.rescale_intensity(s_lap,out_range=(0.0,1.0)),cmap='gray')

plt.show()




