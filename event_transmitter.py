# Test write to usb serial program
from microbit import *

def show_health_message():
    display.show(Image.HEART)
    sleep(200)
    display.clear()

while True:
    if button_a.was_pressed():
        show_health_message()
        print("BTN_A:The fox hunts at midnight.")
    elif button_b.was_pressed():
        show_health_message()
        print("BTN_B:The whale whistles mournfully.")
