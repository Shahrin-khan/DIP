import skimage.io as io
import matplotlib.pyplot as plt
import skimage.exposure as ex

f = io.imread('D:\\DIP\\Dataset\\misc\\4.1.04.tiff')

plt.subplot(1,2,1)
plt.axis('off')
plt.title('Original image')
plt.imshow(f, cmap='gray')

plt.subplot(1,2,2)
plt.axis('off')
plt.title('Double thresholded image')
plt.imshow(ex.rescale_intensity(((f>40)&(f<80)),out_range=(0.0,1.0)),cmap='gray')

plt.show()
