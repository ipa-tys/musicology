# ockeghem
Some practise and analysis tools for improvised counterpoint, canons, Renaissance polyphony etc

Ideas are based on the books:
* Peter Schubert: Modal Counterpoint, Renaissance Style
* Barnabé Janin: Chanter sur le livre

## Requirements

* For printing a score from the MIDI:
    - MuseScore

* For realizing audio from the MIDI:
    - FluidSynth (at the moment version 1.1.11); newer versions do not work with pyfluidsynth
    - pyfluidsynth (Python bindings)
    - A soundfont, e.g. papelmedia_Irina_Brochin.sf2

* Python modules
    - music21
    - midi2audio
