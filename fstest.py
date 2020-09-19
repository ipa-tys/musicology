import time
import fluidsynth
import pdb
# from midi2audio import FluidSynth

# note: at the moment, this only works with fluidsynth 1.1.11
# newer versions do not work with pyfluidsynth

fs = fluidsynth.Synth()
# fs.start()
fs.start(driver='coreaudio')

sfid = fs.sfload("../soundfonts/Papelmedia_Irina_Brochin.sf2")
fs.program_select(0, sfid, 0, 0)


# pdb.set_trace()

for i in range(10):
    fs.noteon(0, 60, 30)
    fs.noteon(0, 67, 30)
    fs.noteon(0, 76, 30)
    time.sleep(3.0)

#for i in range(100000):
#    print('hello')
#    time.sleep(0.1)
time.sleep(10.0)

fs.noteoff(0, 60)
fs.noteoff(0, 67)
fs.noteoff(0, 76)

time.sleep(1.0)

fs.delete()

