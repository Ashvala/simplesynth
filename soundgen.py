import math
import wave
import struct
import sys

def freq_gen(freq, file, octave, sin_wave_move):
  size = 10000
  frate = 11025.0
  amp = 8000.0
  new_list = [x*octave for x in freq]

  sines = []
  for y in new_list:
    for x in range(size):
      sines.append(math.sin(sin_wave_move*math.pi*y*(x/frate)))
  wav_file = wave.open(file, "w")

  nchannels = 1
  samples = 2
  framer = int(frate)
  wav_file.setparams((nchannels, samples, framer, size, "NONE", "not compressed"))
  print "Generating!"
  for s in sines:
      wav_file.writeframes(struct.pack('h', int(s*amp/2)))
      print ".",
  wav_file.close()


C = 32
CSharp = 35
D = 37
DSharp = 39
E = 41
F = 44
FSharp = 46
G = 49
GSharp = 51
A = 55
ASharp = 58
B = 62
C2 = 65

note_list = [C,D,E,F,G, A, B, C2]

freq_gen(note_list, "t1.wav", 4, 6)


