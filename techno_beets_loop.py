from microbit import *
import music

# Techno beets crescendo program!
# (Mentally insert dance fighting scene)

# Don't do more than ~6 steps; it just... doesn't work well
CRESCENDO_STEPS = 4 
num_notes = 2
pitch = 150
duration = 800


for i in range(1, CRESCENDO_STEPS+1, 1):
    for j in range(num_notes):
        music.pitch(pitch, duration)

    # Make "note" higher
    pitch += 10

    # Cut duration of each note in half
    # Must cast to int because "pitch" funtion needs guaranteed int type
    duration = int(duration/2)

    # Double the amount of notes
    num_notes *= 2

audio.play(Sound.YAWN)
