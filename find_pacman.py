## FIND PACMAN GAME
# Pacman is hidden on the board at the specified target coordinates
# Your player must find him as fast as possible
from microbit import *
import music

# These constants will never change, unless you want to change
# the target coordinates
BOARD_SIZE = 5
TARGET_X = 1
TARGET_Y = 1

# This is the program's state
x = 0
y = 0

# This loop runs repeatedly and keeps the program alive indefinitely
while True:

    # #############################
    # CHECK CURRENT STATE
    # #############################
    
    # Check for hit
    if x == TARGET_X and y == TARGET_Y:
        # If we're on the target coordinates then show the image
        # and play the sound
        display.show(Image.PACMAN)
        music.play(music.POWER_UP)        
        display.clear()
        
        # This will exit the program, since there is no more code
        # after the while loop
        break
    else:
        # Otherwise, just light up the current pixel to its max value, 9
        display.set_pixel(x, y, 9)

    # #############################
    # HANDLE EVENTS
    # #############################
    
    # Move X
    if button_a.was_pressed():
        # Clear the screen so the last coordinate doesn't stay
        # lit up
        display.clear()

        # Use a "circular array" technique to push us back to coordinate
        # zero if we spill off the edge
        x = (x + 1) % BOARD_SIZE

        # Give the user audio feedback
        music.pitch(500, 100)

    # Move Y
    if button_b.was_pressed():
        display.clear()
        y = (y + 1) % BOARD_SIZE
        music.pitch(500, 100)
        
