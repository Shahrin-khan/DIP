import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.color import convert_colorspace

img_01=plt.imread('D:\\DIP\\Dataset\\misc\\4.1.04.tiff')
img_hsv = convert_colorspace(img_01, 'RGB','HSV')

h = img_01[:,:,0]
s = img_01[:,:,1]
v = img_01[:,:,2]

z_h = np.zeros_like(h)
z_s = np.zeros_like(s)
z_v = np.zeros_like(v)

h_img = np.dstack((h,z_s,z_v))
s_img = np.dstack((z_h,s,z_v))
v_img = np.dstack((z_h,z_s,v))

plt.subplot(2,5,1)
plt.axis('off')
plt.title('Hsv image')
plt.imshow(img_hsv)

plt.subplot(2,5,2)
plt.axis('off')
plt.title('hue channel image')
plt.imshow(h)

plt.subplot(2,5,3)
plt.axis('off')
plt.title('saturation channel image')
plt.imshow(s)

plt.subplot(2,5,4)
plt.axis('off')
plt.title('value channel image')
plt.imshow(v)

rcon_img = np.dstack((h,s,v))

plt.subplot(2,5,5)
plt.axis('off')
plt.title('Reconstructed hsv image')
plt.imshow(rcon_img)




plt.subplot(2,5,7)
plt.axis('off')
plt.title('hue only image')
plt.imshow(h_img)

plt.subplot(2,5,8)
plt.axis('off')
plt.title('saturation only image')
plt.imshow(s_img)

plt.subplot(2,5,9)
plt.axis('off')
plt.title('value only image')
plt.imshow(v_img)

rcon_img_02 = h_img + s_img + v_img

plt.subplot(2,5,10)
plt.axis('off')
plt.title('Reconstructed color image')
plt.imshow(rcon_img_02)

plt.show()

