import skimage.transform as tr
import skimage.restoration as re
import skimage.data as data
import matplotlib.pyplot as plt

c = data.camera()

head = c[60:210, 150:300]

plt.figure()

plt.subplot(2,2,1)
plt.axis('off')
plt.title('Head')
plt.imshow(head, cmap='gray')



head4a = tr.rescale(head,2,order=0)
plt.subplot(2,2,2)
plt.axis('off')
plt.title('Nearest')
plt.imshow(head4a,cmap='gray')



head4b = tr.rescale(head,2,order=1)
plt.subplot(2,2,3)
plt.axis('off')
plt.title('Bilinear')
plt.imshow(head4b,cmap='gray')


head4c = tr.rescale(head,2,order=3)
plt.subplot(2,2,4)
plt.axis('off')
plt.title('Bicubic')
plt.imshow(head4c,cmap='gray')


plt.show()




