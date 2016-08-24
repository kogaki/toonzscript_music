# -*- coding: utf-8 -*-
import argparse
import scipy.io.wavfile
import pylab
import math

# FREQ = 44100
FREQ = 48000

parser = argparse.ArgumentParser()
parser.add_argument("music_file")
args = parser.parse_args()


"""
@see http://bastian.rieck.ru/blog/posts/2014/simple_experiments_speech_detection/
"""
def shortTermEnergy(frame):
  return sum( [ abs(x)**2 for x in frame ] ) / len(frame)


def calc_energy(sound, framelen=10000, skip=10000):
    frame = [0 for i in range(framelen)]
    energy = []
    for i, val in enumerate(sound):
        frame.append(val)
        frame.pop(0)
        if(i % skip == 0):
            # energy.append(math.log(max(shortTermEnergy(frame), 0.001)))
            energy.append(shortTermEnergy(frame))
    return energy

data = scipy.io.wavfile.read( "Test.wav" )[1][:, 0]
energy = calc_energy(data, skip=int(float(FREQ)/30))
max_energy = max(energy)
normalized_energy = [max(0.1, float(e)*3/max_energy) for e in energy]

# pylab.plot(energy)
# pylab.show()

part = """
builder = new ImageBuilder();
builder.add(f_orig, (new Transform).scale({scale}));
f = builder.image;
l.setFrame({i}, f);
"""

sub = ""

for i,en in enumerate(normalized_energy):
    sub += part.format(i=i+2, scale=en)


entire = """
l = new Level("/Users/keisuke_ogaki/Documents/opentoonz/music/testras.0001.tif");
f_orig = l.getFrame(1);

{}

l.save("/Users/keisuke_ogaki/Documents/opentoonz/music/testras2.0001.tif");
"""

print(entire.format(sub))
