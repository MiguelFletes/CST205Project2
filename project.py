#!/usr/bin/env python
from PIL import Image
import math
#import numpy
import pyaudio

#This loop goes through each pixel and saves the pixel values as pix
def smallImage(image):
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            print "------", i, j
            location = (i, j)
            pix = image.getpixel(location) 

            #change frequency
            FREQUENCY = 1000 + (15.625 * pix[0])
            #change length
            LENGTH = 0.002 * pix[1]

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
                            channels = 1, rate = BITRATE, 
                            output = True)
            stream.write(WAVEDATA)
            stream.stop_stream()
            stream.close()
    p.terminate()

def bigImage(image):
    r = []
    g = []
    #b = []
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            print "------", x, y
            location = (x, y)
            pix = image.getpixel(location)

            r.append(pix[0])
            g.append(pix[1])

        r.sort
        g.sort
        mid = image.size[0] / 2

        FREQUENCY = 1000 + (15.625 * r[mid])
        LENGTH = 0.002 * g[mid]

        r = []
        g = []

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
                        channels = 1, rate = BITRATE, 
                        output = True)
        stream.write(WAVEDATA)
        stream.stop_stream()
        stream.close()
    p.terminate()

PyAudio = pyaudio.PyAudio
BITRATE = 10000
FREQUENCY = 1
#LENGTH = 1.0000001

#image = Image.open("pokemon.png")

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

path = raw_input("Enter name of image: ")
image = Image.open(path)
print image.size

if(image.size[0] > 100 or image.size[1] > 100):
    bigImage(image)
else:
    smallImage(image)
