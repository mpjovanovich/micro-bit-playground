# Imports go at the top
from microbit import *
import radio
import music

# Group goes from 0-255
# Power goes from 0-7, with 6 as default
radio.config(group=201, power=6)
radio.on()

while True:
    # Non-blocking receive check
    message = radio.receive()
    if message == "a":
        music.play(['a'])
    elif message == "b":
        music.play(['b'])
        
    # If we don't want to buffer through messages
    # that came in while scrolling, uncomment this;
    # It will clear the buffer
    #while radio.receive():
        #pass
    
    # Check for button press
    if button_a.was_pressed():
        radio.send("a")
    
    if button_b.was_pressed():
        radio.send("b")

    # Small delay to prevent busy-waiting consuming battery
    sleep(10)