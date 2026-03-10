from microbit import *
import music
import radio

# Flexible encoding for was overkill for most things:
# Much easier to just encode each part in a dictionary

# Carol of the Bells
SONG = {
    "voice_1": ['eb4:2','d4:1','eb4:1','c4:2','eb4:2','d4:1','eb4:1','c4:2','eb4:2','d4:1','eb4:1','c4:2','eb4:2','d4:1','eb4:1','c4:2','eb4:2','d4:1','eb4:1','c4:2','eb4:2','d4:1','eb4:1','c4:2','eb4:2','d4:1','eb4:1','c4:2','eb4:2','d4:1','eb4:1','c4:2'],
    "voice_2": ['r:24','g4:2','f4:1','g4:1','eb4:2','g4:2','f4:1','g4:1','eb4:2','g4:2','f4:1','g4:1','eb4:2','g4:2','f4:1','g4:1','eb4:2'],
}

MY_PART = "voice_1"

radio.config(group=201, power=6)
radio.on()
music.set_tempo(bpm=110)

# Listen for 'go' message as in previous program
while True:
    message = radio.receive()
    if message == 'go':
        music.play(SONG[MY_PART])
    
    if button_a.was_pressed():
        radio.send('go')
        music.play(SONG[MY_PART])

