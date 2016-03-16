#!/usr/bin/env python
from PIL import Image
import math
import pyaudio

'''
Citation:
http://askubuntu.com/questions/202355/how-to-play-a-fixed-frequency-sound-using-python
The code for playing sound was modified from the code here.
'''

'''
Functions:
'''

#This fungtion goes through each pixel of an image and plays a sound
#depending on the RGB values
def normal(image):
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            print "------", i, j#for debug
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

            #play the sound
            p = PyAudio()
            stream = p.open(format = p.get_format_from_width(1), 
                            channels = 1, rate = BITRATE, 
                            output = True)
            stream.write(WAVEDATA)
            stream.stop_stream()
            stream.close()
    p.terminate()

#This function takes the median of the RGB values of each row of an image
#and plays a sound for each
def median(image):
    rVal = []
    gVal = []
    #bVal = []
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            print "------", x, y#for debug
            location = (x, y)
            pix = image.getpixel(location)

            rVal.append(pix[0])
            gVal.append(pix[1])

        rVal.sort
        gVal.sort
        mid = image.size[0] / 2

        FREQUENCY = 1000 + (15.625 * rVal[mid])
        LENGTH = 0.002 * gVal[mid]

        rVal = []
        gVal = []

        NUMBEROFFRAMES = int(BITRATE * LENGTH)
        RESTFRAMES = NUMBEROFFRAMES % BITRATE
        WAVEDATA = ''

        for x in xrange(NUMBEROFFRAMES):
            WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))    

        #fill remainder of frameset with silence
        #for x in xrange(RESTFRAMES): 
        WAVEDATA = WAVEDATA + WAVEDATA + chr(128)

        #play sound
        p = PyAudio()
        stream = p.open(format = p.get_format_from_width(1), 
                        channels = 1, rate = BITRATE, 
                        output = True)
        stream.write(WAVEDATA)
        stream.stop_stream()
        stream.close()
    p.terminate()

#This function takes the average of the RGB values and plays a sound
def average(image):
    rVal = 0
    gVal = 0
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            print "------", i, j#for debug
            location = (i, j)
            pix = image.getpixel(location) 

            rVal = rVal + pix[0]
            gVal = gVal + pix[1]

        rVal = rVal / image.size[1]
        gVal = gVal / image.size[1]

        #change frequency
        FREQUENCY = 1000 + (15.625 * rVal)
        #change length
        LENGTH = 0.002 * gVal

        NUMBEROFFRAMES = int(BITRATE * LENGTH)
        RESTFRAMES = NUMBEROFFRAMES % BITRATE
        WAVEDATA = ''    

        for x in xrange(NUMBEROFFRAMES):
            WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))    

        #fill remainder of frameset with silence
        #for x in xrange(RESTFRAMES): 
        WAVEDATA = WAVEDATA + WAVEDATA + chr(128)

        #play the sound
        p = PyAudio()
        stream = p.open(format = p.get_format_from_width(1), 
                        channels = 1, rate = BITRATE, 
                        output = True)
        stream.write(WAVEDATA)
        stream.stop_stream()
        stream.close()

        rVal = 0
        gVal = 0
    p.terminate()

'''
Main:
'''

PyAudio = pyaudio.PyAudio
BITRATE = 10000
FREQUENCY = 1
LENGTH = 1.0000001

#uncomment for default picture
image = Image.open("pokemon.png")

#uncomment for user's choice
#path = raw_input("Enter name of image: ")
#image = Image.open(path)
print image.size

#User's choice for mode
while 1:
    choice = raw_input("1. Normal 2. Median 3. Average: ")
    if choice == "1":
        normal(image)
    elif choice == "2":
        median(image)
    elif choice == "3":
        average(image)
    elif choice == "4" or choice == "exit":
        break
    else:
        print "Invalid input"

'''
if(image.size[0] > 100 or image.size[1] > 100):
    bigImage(image)
else:
    smallImage(image)
'''
