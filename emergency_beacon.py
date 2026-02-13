from microbit import *
import music

alarm_on = False

while True:
    if button_a.was_pressed():
        alarm_on = True
    elif button_b.was_pressed():
        alarm_on = False

    if alarm_on:
        display.show(Image.GHOST)
        music.pitch(400, 500)
        display.clear()
        sleep(500)
