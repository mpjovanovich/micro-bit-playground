from microbit import *
import music

MIN_VAL = 0
MAX_VAL = 9
count = 0

def beep():
    music.pitch(500,100)

while True:
    if button_a.was_pressed():
        count = max(MIN_VAL, count-1)
        beep()
    elif button_b.was_pressed():
        count = min(MAX_VAL, count+1)
        beep()

    display.show(count)
