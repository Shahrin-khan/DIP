from tkinter import *
import numpy as np
import skimage.io as io
import skimage.data as data
import skimage.util.noise as noise
import scipy.ndimage as ndi
from wand.image import Image
def distort() :
    with Image(filename ="4.1.01.tiff") as img:
        img.distort('arc', (45, ))
        img.save(filename ='distorted.png')
        image=io.imread('distorted.png')
        io.imshow(image)
        io.show()
def swirl() :
    with Image(filename ="4.1.01.tiff") as img:
        img.swirl(degree = 100)
        img.save(filename ='swirled.png')
        image=io.imread('swirled.png')
        io.imshow(image)
        io.show()
def fuzzy() :
    with Image(filename ="4.1.01.tiff") as img:
        img.spread(radius=8.0)
        img.save(filename ='fuzzied.png')
        image=io.imread('fuzzied.png')
        io.imshow(image)
        io.show()
window = Tk()
window.title( 'Special Effects' )
btn_end = Button( window , text = 'Stop',command=exit )

btn_tog = Button( window , text = 'Distort',fg='black', bg='blue', command=distort )
btn_swirl = Button( window , text = 'Swirl' ,fg='black', bg='blue', command=swirl )
btn_fuzzy = Button( window , text = 'Spread' ,fg='black', bg='blue', command=fuzzy )

btn_end.pack( padx = 75 , pady = 10 )
btn_tog.pack( padx = 75 , pady = 10 )
btn_swirl.pack( padx = 75 , pady = 10 )
btn_fuzzy.pack( padx = 75 , pady = 10 )
window.mainloop()
