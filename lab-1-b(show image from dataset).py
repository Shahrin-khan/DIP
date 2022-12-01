import skimage.io as io
import matplotlib.pyplot as plt

img_01 = io.imread('D:\\DIP\\Dataset\\misc\\4.1.01.tiff')
img_02 = io.imread('D:\\DIP\\Dataset\\misc\\distorted.png')
img_03 = io.imread('D:\\DIP\\Dataset\\misc\\fuzzied.png')
img_04 = io.imread('D:\\DIP\\Dataset\\misc\\swirled.png')


plt.subplot(5,5,1)
plt.axis('off')
#plt.title('Color image ... .')
plt.imshow(img_01)

plt.subplot(5,5,2)
plt.axis('off')
#plt.title('Grayscale image.')
plt.imshow(img_02,cmap='gray')

plt.subplot(5,5,3)
plt.axis('off')
#plt.title('Grayscale image.')
plt.imshow(img_03,cmap='gray')

plt.subplot(5,5,4)
plt.axis('off')
#plt.title('Grayscale image.')
plt.imshow(img_04,cmap='gray')

plt.show()

