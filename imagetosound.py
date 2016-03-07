from PIL import Image
import math
import numpy
import pyaudio

im = Image.open('yosemite.jpg') #example
width, height = im.size #example
rgb = im.convert('RGB') #example

print width
print height
chunks = []
RATE = 44100


def sine(frequency, length, RATE):

    length = int(length * RATE)
    factor = float(frequency) * (math.pi * 2) / RATE
    return numpy.sin(numpy.arange(length) * factor)


def play_tone(stream, frequency, length):
    chunks.append(sine(frequency, length, RATE))

    chunk = numpy.concatenate(chunks) * 0.25

    stream.write(chunk.astype(numpy.float32).tostring())


if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format = pyaudio.paFloat32,
                    channels = 1, rate = 44100, output = 1)
    play_tone(stream, frequency = 540, length = 1) #outputs the sound
    ''' 
    Tried to figure out how to set each pixel a frequency
    Modify this part of the code
    ****************************************************************
    for x in range(width):
		for y in range(height):
			r, g, b = rgb.getpixel((x,y))
			
			if (r >= 0 and r <= 50):
    				play_tone(stream, frequency = 300, length = .5)
    		if (r >= 51 and r <= 100):
    				play_tone(stream, frequency = 350, length = .5)
    		if (r >= 101 and r <= 150):
    				play_tone(stream, frequency = 400, length = .5)
    		if (r >= 151 and r <= 200):
    				play_tone(stream, frequency = 450, length = .5)
    		if (r >= 201 and r <= 250):
    				play_tone(stream, frequency = 500, length = .5)
    		if (r >= 251 and r <= 255):
    				play_tone(stream, frequency = 600, length = .5)
	'''	
    stream.close()
    p.terminate()