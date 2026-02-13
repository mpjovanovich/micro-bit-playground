from microbit import *
import music

# TODO
MAJOR_SCALES = {
    "C": ['C4:3', 'D4', 'E4', 'F4', 'G4'],
    "D": ['C4:3', 'D4', 'Eb4', 'F4', 'G4'],
}

# TODO
MINOR_SCALES = {
    "A": [],
    "B": [],
    "C": ['C4:3', 'D4', 'E4', 'F4', 'G4'],
    "D": [],
}

is_major = True

while True:
    # TODO: button a toggles key
    # Button B toggles maj/min
    # Display should should key (Upper major, lower minor)
  if pin_logo.is_touched():
    # todo 
    #music.play(SCALES["C_MAJ"])