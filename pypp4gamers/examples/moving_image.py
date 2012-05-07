#! /usr/bin/env python

# a moving image animation
from pypp4gamers import *

# settings (before initialize)
set_window_size((400,400))

# initialize
pypp_init()

# main loop definition
def mainLoop():
    x, y = 0, 0
    w, h = get_screen_width(), get_screen_height()
    
    while True:
        # gets the display, clean and handle events
        get_display()
        
        # display a image in a given position
        image('tux.png', (x,y))
        
        # update the display, and draws everything to the screen
        update_display()
        
        print x,y
        if x < w: x += 2
        if y < h: y += 2
        if x >= w and y >= h: x, y = 0, 0

mainLoop()

