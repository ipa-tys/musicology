from music21 import *
from midi2audio import FluidSynth

import pdb

legalIntervals = []
intervalNames = 
i = interval.Interval('M3')

fs = FluidSynth('Papelmedia_Irina_Brochin.sf2')

note1 = note.Note('D4')
note1.duration = note.duration.Duration(4.0)

stream1 = stream.Stream()
stream1.append(note1)

notes=[]
for i in range(10):
    note2 = note.Note('D3')
    note2.duration = note.duration.Duration(4.0)
    stream1.append(note2)


# fp = s.write('midi', fp='bla.mid')

# pdb.set_trace()

cadence_midi = stream1.write('midi')
fs = FluidSynth('Papelmedia_Irina_Brochin.sf2') # arch
fs.midi_to_audio(cadence_midi, 'canon.wav')


