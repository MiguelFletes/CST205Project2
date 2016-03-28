#Getting sound to work

#Ignore this first block of comments
"""
from __future__ import division #Avoid division problems in Python 2
import math
import pyaudio
import sys

PyAudio = pyaudio.PyAudio
RATE = 16000
WAVE = 3000
data = ''.join([chr(int(math.sin(x/((RATE/WAVE)/math.pi))*127+128)) for x in xrange(RATE)])
p = PyAudio()

stream = p.open(format =
                p.get_format_from_width(1),
                channels = 1,
                rate = RATE,
                output = True)
for DISCARD in range(5):
    stream.write(data)
stream.stop_stream()
stream.close()
p.terminate()
"""

#START HERE


import math
import pyaudio

#sudo apt-get install python-pyaudio
PyAudio = pyaudio.PyAudio

#See http://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 10000 #number of frames per second/frameset.      

#See http://www.phy.mtu.edu/~suits/notefreqs.html
FREQUENCY = 2000 #Hz, waves per second, 261.63=C4-note.
LENGTH = 1.2232 #seconds to play sound

NUMBEROFFRAMES = int(BITRATE * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % BITRATE
WAVEDATA = ''    

for x in xrange(NUMBEROFFRAMES):
 WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))    

#fill remainder of frameset with silence
#for x in xrange(RESTFRAMES): 
 #WAVEDATA = WAVEDATA+chr(128)

p = PyAudio()
stream = p.open(format = p.get_format_from_width(1), 
                channels = 1, 
                rate = BITRATE, 
                output = True)
stream.write(WAVEDATA)
stream.stop_stream()
stream.close()
p.terminate()

