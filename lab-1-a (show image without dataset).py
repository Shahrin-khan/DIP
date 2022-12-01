import skimage.data as data
import matplotlib.pyplot as plt

img_01 = data.astronaut()
img_02 = data.brick()
img_03 = data.camera()
img_04 = data.cell()
img_05 = data.chelsea()
img_06 = data.clock()
img_07 = data.coffee()
img_08 = data.coins()
img_09 = data.colorwheel()
img_10 = data.grass()

plt.subplot(5,5,1)
plt.axis('off')
#plt.title('Color image of the astronaut Eileen Collins.')
plt.imshow(img_01)

plt.subplot(5,5,2)
plt.axis('off')
#plt.title('Brick wall.')
plt.imshow(img_02,cmap='gray')

plt.subplot(5,5,3)
plt.axis('off')
#plt.title('Gray-level “camera” image.')
plt.imshow(img_03,cmap='gray')

plt.subplot(5,5,4)
plt.axis('off')
#plt.title('Cell floating in saline.')
plt.imshow(img_04,cmap='gray')

plt.subplot(5,5,5)
plt.axis('off')
#plt.title('Chelsea the cat.')
plt.imshow(img_05)

plt.subplot(5,5,6)
plt.axis('off')
#plt.title('Motion blurred clock.')
plt.imshow(img_06,cmap='gray')

plt.subplot(5,5,7)
plt.axis('off')
#plt.title('Coffee cup.')
plt.imshow(img_07)

plt.subplot(5,5,8)
plt.axis('off')
#plt.title('Greek coins from Pompeii.')
plt.imshow(img_08,cmap='gray')

plt.subplot(5,5,9)
plt.axis('off')
#plt.title('Color Wheel.')
plt.imshow(img_09)

plt.subplot(5,5,10)
plt.axis('off')
#plt.title('Grass.')
plt.imshow(img_10,cmap='gray')

plt.show()

