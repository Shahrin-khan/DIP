import numpy as np
import skimage.io as io
import skimage.exposure as ex
from skimage.util import img_as_float,img_as_ubyte
from numpy.fft import ifft2,fft2,fftshift
import math

g = io.imread('D:\\DIP\\Dataset\\misc\\7.1.05.tiff')
io.imshow(g)
io.show()

r,c=g.shape
x,y=np.mgrid[0:r,0:c].astype('float32')
p=np.sin(x/3+y/3)+1.0
gp=(2*img_as_float(g)+p/2)/3
io.imshow(gp)
io.show()

gf=fftshift(fft2(gp))
temp=ex.rescale_intensity(abs(gf), out_range=(0,1))
gf2=img_as_ubyte(temp)
gf2[200,200]=0
i,j=np.where(gf2==gf2.max())
c=np.sqrt((i-200)**2+(j-200)**2)
cf=fftshift(ifft2(c))


z=np.sqrt((x-200)**2+(y-200)**2)
k=1
d=math.sqrt(610.0)
br=(z<np.floor(d-k))|(z>np.ceil(d+k))
cfr=cf*br
io.imshow(cfr)
io.show()
