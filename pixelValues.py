#!usr/bin/env python
#CST205 Project 2
#Testing how to take and use the pixel values

from PIL import Image
image = Image.open("Pikachu.png")#CHANGE TO CHOSEN IMAGE



print image
print 'height:', image.size[1], 'width:', image.size[0]

k = image.size[0]
l = image.size[1]
k = k / 2
l = l / 2
p = (k,l)
pix = image.getpixel(p)#THIS IS THE KEY PART
#pix is a list containing the values of the pixel at (k,l)
print 'middle pixel', pix
print '[0]', pix[0]
print '[1]', pix[1]


#This loop goes through each pixel and saves the pixel values as pix
for i in range(0,image.size[0]):
    for j in range(0,image.size[1]):
        k = (i, j)
        pix = image.getpixel(k) 
        
        #print i, ',', j, pix
        red = pix[0]
        blue = pix[1] #Since pix is a list of the pixel values,
                    #the values are taken by using their index
                    #The picture I tested with was an RGBA type, so
                    #the values would look like [R-val, G-val, B-val, A-val]

