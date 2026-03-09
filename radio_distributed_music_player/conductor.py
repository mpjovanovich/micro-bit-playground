from microbit import *
import music
from typing import Dict, List, Tuple
from time import sleep

'''
BROADCAST
'''

# Here is one measure:
SONG = [
    "c4:4",
    "",
    "",
    "",
    "d4:4",
    "",
    "",
    "",
    "eb4:4",
    "",
    "",
    "",
    "c4:4,eb4:4",
    "",
    "",
    "",
]

# Not sure if we need this yet..
BEATS_PER_MINUTE = 120
SIXTEENTH_NOTES_PER_MINUTE = BEATS_PER_MINUTE * 4
SLEEP_TIME_SECONDS = 60 / SIXTEENTH_NOTES_PER_MINUTE

'''
SUBSCRIBER
'''

#LISTENING_FOR_NOTE = "c4"
LISTENING_FOR_NOTE = "eb4"

# Returns note that is subscribed to, else None
def get_my_note_from_payload(payload: str) -> str:
    for tone in payload.split(","):
        note = tone.split(":")[0]
        if note == LISTENING_FOR_NOTE:
            return tone
    return ""

'''
SIMULATED EVENT LOOP
'''

current_tick = 0
queue = []

while current_tick < len(SONG):
    # Broadcast at regular intervals
    queue.append(SONG[current_tick])

    # Receive messages
    if len(queue) > 0:
        my_note = get_my_note_from_payload(queue.pop(0))
        if my_note:
            music.play(my_note)

    # Sleep for 1 tick
    current_tick += 1
    sleep(SLEEP_TIME_SECONDS)
