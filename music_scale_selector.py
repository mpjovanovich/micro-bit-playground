from microbit import *
import music

# We are treating this string like a list / array, and accessing
# it by index to get the current scale
SCALE_VALUES = 'ABCDEFG'

# These are the actual notes for each major scale
SCALES = {
    "A": ['A4', 'B4', 'C#5', 'D5', 'E5', 'F#5', 'G#5', 'A5'],
    "B": ['B4', 'C#5', 'D#5', 'E5', 'F#5', 'G#5', 'A#5', 'B5'],
    "C": ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5'],
    "D": ['D4', 'E4', 'F#4', 'G4', 'A4', 'B4', 'C#5', 'D5'],
    "E": ['E4', 'F#4', 'G#4', 'A4', 'B4', 'C#5', 'D#5', 'E5'],
    "F": ['F4', 'G4', 'A4', 'Bb4', 'C5', 'D5', 'E5', 'F5'],
    "G": ['G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F#5', 'G5'],
}

# We will adjust this to change the scale letter
scale_index = 0

while True:
    display.show(SCALE_VALUES[scale_index])
    
    if button_a.was_pressed():
        # Increment scale
        scale_index = scale_index - 1
        
        # Check if we overflowed on low range
        if scale == -1:
            scale = len(SCALE_VALUES) - 1

    if button_b.was_pressed():
        # Increment scale
        scale_index = scale_index + 1
        
        # Check if we overflowed on high range
        if scale == len(SCALE_VALUES):
            scale = 0

    # This button is our actual "play" button
    if pin_logo.is_touched():
        # Get the correct scale letter from the SCALE_VALUES string
        # using the index
        current_scale = SCALE_VALUES[scale_index]

        # Play the scale
        music.play(SCALES[current_scale])
        
