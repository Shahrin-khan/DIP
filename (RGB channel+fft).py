import numpy as np
import skimage.data as data
import skimage.exposure as ex
import matplotlib.pyplot as plt
from skimage.color import rgb2gray


img_01 = plt.imread('D:\\DIP\\Dataset\\misc\\4.2.07.tiff')

img_gray = rgb2gray(img_01)

r = img_01[:,:,0]
g = img_01[:,:,1]
b = img_01[:,:,2]

z_r = np.zeros_like(r)
z_g = np.zeros_like(g)
z_b = np.zeros_like(b)

r_img = np.dstack((r,z_g,z_b))
g_img = np.dstack((z_r,g,z_b))
b_img = np.dstack((z_r,z_g,b))

plt.subplot(2,5,1)
plt.axis('off')
plt.title('Color image')
plt.imshow(img_01)

plt.subplot(2,5,2)
plt.axis('off')
plt.title('RED channel image')
plt.imshow(r,cmap='gray')

plt.subplot(2,5,3)
plt.axis('off')
plt.title('GREEN channel image')
plt.imshow(g,cmap='gray')

plt.subplot(2,5,4)
plt.axis('off')
plt.title('BLUE channel image')
plt.imshow(b,cmap='gray')

rcon_img = np.dstack((r,g,b))

plt.subplot(2,5,5)
plt.axis('off')
plt.title('Reconstructed color image')
plt.imshow(rcon_img)


plt.subplot(2,5,6)
plt.axis('off')
plt.title('Grayscale image')
plt.imshow(img_gray, cmap='gray')

plt.subplot(2,5,7)
plt.axis('off')
plt.title('RED only image')
plt.imshow(r_img)

plt.subplot(2,5,8)
plt.axis('off')
plt.title('GREEN only image')
plt.imshow(g_img)

plt.subplot(2,5,9)
plt.axis('off')
plt.title('BLUE only image')
plt.imshow(b_img)

rcon_img_02 = r_img + g_img + b_img

plt.subplot(2,5,10)
plt.axis('off')
plt.title('Reconstructed color image')
plt.imshow(rcon_img_02)

plt.show()

c = r_img

cf = np.fft.fft2(c)
cfs = np.fft.fftshift(cf)
cfsl = np.log(1+np.abs(cfs))

plt.subplot(3,1,1)
plt.axis('off')
plt.title('Red image')
plt.imshow(c, cmap='gray')

plt.subplot(3,1,2)
plt.axis('off')
plt.title('DFT of the red image')
plt.imshow(ex.rescale_intensity(cfsl,out_range=(0.0,1.0)),cmap='gray')


plt.show()

x = g_img

xf = np.fft.fft2(x)
xfs = np.fft.fftshift(xf)
xfsl = np.log(1+np.abs(xfs))

plt.subplot(3,2,1)
plt.axis('off')
plt.title('Green image')
plt.imshow(x, cmap='gray')

plt.subplot(3,2,2)
plt.axis('off')
plt.title('DFT of the green image')
plt.imshow(ex.rescale_intensity(xfsl,out_range=(0.0,1.0)),cmap='gray')


plt.show()

y = b_img

yf = np.fft.fft2(y)
yfs = np.fft.fftshift(yf)
yfsl = np.log(1+np.abs(yfs))

plt.subplot(3,3,1)
plt.axis('off')
plt.title('Blue image')
plt.imshow(c, cmap='gray')

plt.subplot(3,3,2)
plt.axis('off')
plt.title('DFT of the blue image')
plt.imshow(ex.rescale_intensity(yfsl,out_range=(0.0,1.0)),cmap='gray')


plt.show()

