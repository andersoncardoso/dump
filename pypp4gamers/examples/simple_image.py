#! /usr/bin/env python
from pypp4gamers import *

pypp_init()

def mainLoop():
    while True:
        # gets display
        get_display()
        
        # your logic
        if 'space' in keyboard():
            image()
        if 'enter' in keyboard():
            hide_image()
            
        # update display and renders to screen
        update_display()

mainLoop()
