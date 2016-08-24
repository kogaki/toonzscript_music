# -*- coding: utf-8 -*-
import argparse
import scipy.io.wavfile
import pylab
import math

FREQ = 44100

parser = argparse.ArgumentParser()
parser.add_argument("music_file")
args = parser.parse_args()


"""
@see http://bastian.rieck.ru/blog/posts/2014/simple_experiments_speech_detection/
"""
def shortTermEnergy(frame):
  return sum( [ abs(x)**2 for x in frame ] ) / len(frame)


def calc_energy(sound, framelen=10, skip=10000):
    frame = [0 for i in range(framelen)]
    energy = []
    for i, val in enumerate(sound):
        frame.append(val)
        frame.pop(0)
        if(i % skip == 0):
            energy.append(shortTermEnergy(frame))
    return energy

data = scipy.io.wavfile.read( "Test.wav" )[1][:, 0]
energy = calc_energy(data, skip=int(float(FREQ)/30))

# pylab.plot(energy)
# pylab.show()

