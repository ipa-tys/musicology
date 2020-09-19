from music21 import *
from midi2audio import FluidSynth
import random
import pdb
import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='generate canon antecedents.')
    parser.add_argument('-o','--output',help='File stem for output files',required=True)
    parser.add_argument('-t','--type', help='Type of canon', required=True)
    # todo: add difficulty levels (e.g. only a subset of steps, etc)
    # let choose the soundfont
    args = parser.parse_args()
    filestem = args.output
    canon_type = args.type

    legalNoteNamesTenor = ['B-2','B2','C3','D3','E3','F3','G3','A3','B-3','B3','C4','D4','E4','F4','G4','A4']
    legalNoteNamesSoprano = ['B-3','B3','C4','D4','E4','F4','G4','A4','B-4','B4','C5','D5','E5','F5','G5','A5']
    legalNotes = []
    for legalNote in legalNoteNamesSoprano:
        note1 = note.Note(legalNote)
        note1.duration = note.duration.Duration(4.0)
        legalNotes.append(note1)


    if canon_type == 'l8':   
        intervalNames = ['m-3','M-3','P-4','m3','M3','P5']
    if canon_type == 'l5':
        intervalNames = ['m-3','M-3','P-5','m2','M2','P4']
    intervals = []
    for intervalName in intervalNames:
        intervals.append(interval.Interval(intervalName))

    fs = FluidSynth('Papelmedia_Irina_Brochin.sf2')

    note1 = note.Note('D4')
    note1.duration = note.duration.Duration(4.0)

    stream1 = stream.Stream()
    stream1.append(note1)

    for i in range(10):
        legal = False

        while not legal:
            i = random.choice(intervals)
            i.noteStart = stream1[-1]
            if i.noteEnd in legalNotes:
                legal = True
                note1 = i.noteEnd
                note1.duration = note.duration.Duration(4.0)
                stream1.append(note1)



    fp = stream1.write('midi', fp=filestem + '.mid')
    stream1.show()
    # stream1.show(filestem + '.pdf')

    my_tempo = tempo.MetronomeMark(number=40)
    stream1.insert(0, my_tempo)
    cadence_midi = stream1.write('midi')
    fs = FluidSynth('~/soundfonts/papelmedia_Irina_Brochin.sf2') 
    fs.midi_to_audio(cadence_midi, filestem + '.wav')

    # todo: command line parser, e.g. with option for tempo, ornamentation etc.
    # other canons, e.g. in upper octave, fifth, fourth, ...
    # antecedent for canon around a cantus firmus
    # try aubio for pitch detection

