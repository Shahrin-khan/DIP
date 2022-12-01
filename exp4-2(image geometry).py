import skimage.transform as tr
import skimage.restoration as re
import skimage.data as data
import matplotlib.pyplot as plt

c = data.camera()

crc = tr.rotate(c,60,order=3)

plt.subplot(2,2,1)
plt.axis('off')
plt.title('anticlock wise')
plt.imshow(crc, cmap='gray')

crc1 = tr.rotate(c,-60,order=1)

plt.figure()

plt.subplot(2,2,2)
plt.axis('off')
plt.title('clock wise')
plt.imshow(crc1, cmap='gray')


plt.imshow(crc1)
plt.show()
