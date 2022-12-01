import skimage.io as io
import matplotlib.pyplot as plt


img = io.imread('D:\\DIP\\Dataset\\misc\\5.1.12.tiff')

io.imshow(img,cmap='gray')
io.show()

bps = [(img>>i)%2 for i in range(8)]
for i in range(8):
    plt.subplot(3,3,i+1)
    io.imshow(bps[i], cmap='gray')
    plt.axis('off')
io.show()
        
    
