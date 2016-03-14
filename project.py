#!/usr/bin/env python
from PIL import Image
import math
#import numpy
import pyaudio

PyAudio = pyaudio.PyAudio
BITRATE = 10000
FREQUENCY = 1
LENGTH = 1.0000001

image = Image.open("pokemon.png")

print image
print 'height:', image.size[1], 'width:', image.size[0], "\n\n\n\n"

"""
w = image.size[0]
h = image.size[1]
w = w / 2
h = h / 2
p = (w,h)
pix = image.getpixel(p)#THIS IS THE KEY PART
#pix is a list containing the values of the pixel at (k,l)
print 'middle pixel', pix
print '[0]', pix[0]
print '[1]', pix[1]
"""




#This loop goes through each pixel and saves the pixel values as pix
for i in range(0,image.size[0]):
    for j in range(0,image.size[1]):
        print "------", i, j
        w = (i, j)
        pix = image.getpixel(w) 

        #change frequency
        FREQUENCY = 1000 + (15.625 * pix[0])
        #change length
        LENGTH = 0.001 * pix[1]

        NUMBEROFFRAMES = int(BITRATE * LENGTH)
        RESTFRAMES = NUMBEROFFRAMES % BITRATE
        WAVEDATA = ''    

        for x in xrange(NUMBEROFFRAMES):
         WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))    

        #fill remainder of frameset with silence
        #for x in xrange(RESTFRAMES): 
        WAVEDATA = WAVEDATA + WAVEDATA + chr(128)

        p = PyAudio()
        stream = p.open(format = p.get_format_from_width(1), 
                channels = 1, 
                rate = BITRATE, 
                output = True)
        stream.write(WAVEDATA)
        stream.stop_stream()
        stream.close()
p.terminate()
