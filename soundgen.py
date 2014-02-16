import math
import wave
import struct
import sys


# Usage: python soundgen.1.py wave_filename

filename = sys.argv[1]
frate = 11025
quarter_note = 4000
half_note = 8000
whole_note = 16000
eighth = 2000
sixteenth = 1000

# The Fundamental Frequencies: A=55, r=1.0594 = exp(log(2)/12)

C=32.7
Csharp= Dflat= 34.65
D=36.71
Dsharp=Eflat=38.89
E=41.20
F=43.65
Fsharp=Gflat=46.25
G=49
Gsharp=Aflat=51.91
A=55
Asharp=Bflat=58.27
B=61.74
C2=65.41

##

def save_as_wav(file, lst, size):
  amp = 8000.0
  nchannels = 1
  samples = 2  
  wav_file = wave.open(file, "w")
  wav_file.setparams((nchannels, samples, frate, size, "NONE", "not compressed"))
  print "Generating file"
  for s in lst:
      wav_file.writeframes(struct.pack('h', int(s*amp/2)))
  wav_file.close()
  print "Saved to ", file

def freq_gen(freq, octave, sin_wave_move,size):
  actual_freq = [x*octave for x in freq]
  sines = [math.sin(sin_wave_move*math.pi*y*x/frate) for y in actual_freq for x in range(size)]
  return sines

# Arpeggiator of Major chords!
def note_arp(note_name):
  return [note_name, note_name + 5, note_name + 10, note_name + 5, note_name]

# Now Compose Music!

note_list=[A,B,C*2,D*2,E*2,F*2,G*2,A*2]


# take the note_list and play it at different ocatves.
signal = freq_gen(note_list, 12, 4, 3200)
save_as_wav(filename, signal, 3200)
