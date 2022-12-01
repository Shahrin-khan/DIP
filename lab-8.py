import numpy as np
import matplotlib.pyplot as plt
import pywt

c = pywt.data.camera()

coeffs2 = pywt.dwt2(c,'db2')

cA,(cH,cV,cD)= coeffs2

plt.subplot(2,3,1)
plt.axis('off')
plt.title('original image')
plt.imshow(c, cmap='gray')

plt.subplot(2,3,2)
plt.axis('off')
plt.title('Approximate image LL')
plt.imshow(cA,cmap='gray')

plt.subplot(2,3,3)
plt.axis('off')
plt.title('Horizontal detail image HL')
plt.imshow(cH,cmap='gray')


plt.subplot(2,3,4)
plt.axis('off')
plt.title('Vertical detail image LH')
plt.imshow(cV,cmap='gray')

plt.subplot(2,3,5)
plt.axis('off')
plt.title('Diagonal detail image HH')
plt.imshow(cD,cmap='gray')

plt.show()

