import skimage.io as io
import matplotlib.pyplot as plt
import skimage.exposure as ex
import skimage.filters as fl

f = io.imread('D:\\DIP_python\\Dataset\\misc\\7.1.05.tiff')

plt.subplot(2,1,1)
plt.axis('off')
plt.title('Original image')
plt.imshow(f, cmap='gray')

t = fl.threshold_otsu(f)

print(t)

plt.subplot(2,1,2)
plt.axis('off')
plt.title('Single thresholded image')
plt.imshow(ex.rescale_intensity(f<t,out_range=(0.0,1.0)),cmap='gray')

plt.show()




