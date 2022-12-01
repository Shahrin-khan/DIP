import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import pywt

c = io.imread('D:\\DIP\\Dataset\\misc\\4.2.07.tiff')

coeffs2 = pywt.dwt2(c,'db2')

cA,(cH,cV,cD)= coeffs2

plt.subplot(2,3,1)
plt.axis('off')
plt.title('original image')
plt.imshow(c)

plt.subplot(2,3,2)
plt.axis('off')
plt.title('Approximate image LL')
plt.imshow(cA)

plt.subplot(2,3,3)
plt.axis('off')
plt.title('Horizontal detail image HL')
plt.imshow(cH)


plt.subplot(2,3,4)
plt.axis('off')
plt.title('Vertical detail image LH')
plt.imshow(cV)

plt.subplot(2,3,5)
plt.axis('off')
plt.title('Diagonal detail image HH')
plt.imshow(cD)

plt.show()

