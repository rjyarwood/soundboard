#!/usr/bin/env python3
import Jetson.GPIO as GPIO
from playsound import playsound
import vlc
from enum import Enum
import signal
import time

media_player = vlc.MediaPlayer()
media_player.stop()

class PINS(Enum):
    HUNGRY = 11
    OUTSIDE = 13
    WATER = 15
    MOM = 19
    WALK = 21

SOUNDS = {
    PINS.HUNGRY :vlc.Media("/home/rjyarwood/Soundboard/hungry.mp3"),
    PINS.OUTSIDE : vlc.Media("/home/rjyarwood/Soundboard/outside.mp3"),
    PINS.WATER : vlc.Media("/home/rjyarwood/Soundboard/water.mp3"),
    PINS.MOM : vlc.Media("/home/rjyarwood/Soundboard/mom.mp3"),
    PINS.WALK : vlc.Media("/home/rjyarwood/Soundboard/walk.mp3")
}


def keyboardInterruptHandler(signal, frame):
    GPIO.cleanup()
    exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

def callback_fn(channel):
    if(media_player.is_playing()):
        print("ignoring...")
        return

    if channel == PINS.HUNGRY.value:
        media_player.set_media(SOUNDS.get(PINS.HUNGRY))
        media_player.play()
            
    elif channel == PINS.OUTSIDE.value:
        media_player.set_media(SOUNDS.get(PINS.OUTSIDE))
        media_player.play()
        
    elif channel == PINS.WATER.value:
        media_player.set_media(SOUNDS.get(PINS.WATER))
        media_player.play()
            
    elif channel == PINS.MOM.value:
        media_player.set_media(SOUNDS.get(PINS.MOM))
        media_player.play()
        
    elif channel == PINS.WALK.value:
        media_player.set_media(SOUNDS.get(PINS.WALK))
        media_player.play()




def main():

    time.sleep(15)

    playsound("/home/rjyarwood/Soundboard/beep.mp3")

    GPIO.setmode(GPIO.BOARD)
    for pin in PINS:
        GPIO.setup(pin.value, GPIO.IN)
        GPIO.add_event_detect(pin.value, GPIO.RISING, callback=callback_fn)

    while 1:
        pass

if __name__ == '__main__':
    main()
