#! /usr/bin/env python

# moving tux around
from pypp4gamers import *

pypp_init()

def mainLoop():
    x, y = 0, 0
    width, height = get_screen_width(), get_screen_height()
	
    while True:
        # gets display and clean the screnn
        get_display()
        
        # draw image 
        image('tux.png', (x,y))
        
        # updates display and renders to screen
        update_display()
        
        #change direction given event input
        if 'left' in keyboard():
            if x>0: x -= 2
        if 'right' in keyboard():
            if x < width: x += 2
        if 'down' in keyboard():    
            if y < height: y += 2
        if 'up' in keyboard():
            if y>0: y -= 2    

mainLoop()





