#! /usr/bin/env python
from pypp4gamers import *

pypp_init()

def mainLoop():
    while True:
        # gets display
        get_display()
        
        # your logic
        sleep(3*1000)
        sound()
     
        # update display and renders to screen
        update_display()

mainLoop()



