# from microbit import *
# import music
from time import sleep

SONG = [
    "c4:4",
    "",
    "",
    "",
    "eb4:4",
    "",
    "",
    "",
    "c4:4",
    "",
    "",
    "",
    "c4:4,eb4:4",
    "",
    "",
    "",
]

MY_NOTE = "c4"
#MY_NOTE = "eb4"

# Returns note that is subscribed to, else None
def get_my_note_from_payload(payload: str) -> str:
    for tone in payload.split(","):
        note = tone.split(":")[0]
        if note == MY_NOTE:
            return tone
    return ""

def decode(song: list[str]) -> list[str]:
    result = []
    i = 0
    while i < len(song):
        tick = song[i]
        match = get_my_note_from_payload(tick)
        if match:
            # If this is our note, add it to the score
            result.append(match)
            duration = int(match.split(":")[1])
            # This is in here so that we don't treat the sustained ticks as rests
            i += duration
        else:
            # Rest for one tick
            result.append("r:1")
            i += 1
    return result

# Decode song on startup
score = decode(SONG)
print(score)
# music.play(score)