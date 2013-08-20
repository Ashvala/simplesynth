import math
import wave
import struct
import sys

# arpeggiation 
# Given a Note, I should be able to arpeggiate its corresponding major chord.

def freq_gen(freq, file, octave, sin_wave_move):
  size = 4000
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
  wav_file.close()

#Arpeggiator of Majors!
def note_arp(note_name):
  arp=[note_name, note_name + 10, note_name + 20, note_name + 10, note_name]
  return arp

#Fundamental Frequencies

C = 32
Csharp = 35
D = 37
Dsharp = 39
E = 41
F = 44
Fsharp = 46
G = 49
Gsharp = 51
A = 55
Asharp = 58
B = 62
C2 = 65

#Enharmonic schtuff

Dflat = Csharp
EFlat = Dsharp
Gflat = Fsharp
Aflat = Gsharp
Bflat = Asharp

note_list = note_arp(C*2) + note_arp(F*2) + note_arp(G*2) + note_arp(G*2) + note_arp(F*2) + note_arp(C*2)

freq_gen(note_list, "t1.wav", 4, 6)


