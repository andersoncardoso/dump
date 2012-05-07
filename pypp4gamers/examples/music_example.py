#! /usr/bin/env python
from pypp4gamers import *

pypp_init()

def mainLoop():
    while True:
        # gets display
        get_display()
        
        # your logic
        if 'enter' in keyboard():
            music()
        if 'space' in keyboard():
            stop_music()
            
        # update display and renders to screen
        update_display()

mainLoop()



