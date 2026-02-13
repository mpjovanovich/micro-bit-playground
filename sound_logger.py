from microbit import *
import log

SECONDS_TO_RUN = 20

def log_data():
    log.add({
      'sound': microphone.sound_level(),
    })
    
for _ in range(SECONDS_TO_RUN):
    log_data()
    sleep(1000)
