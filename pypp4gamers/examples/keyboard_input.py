#! /usr/bin/env python

# image and color manipulation trough keybard input
from pypp4gamers import *

pypp_init()

def mainLoop():
    r, g, b = 0, 0, 0
    x, y = 0, 0
    width, height = get_screen_width(), get_screen_height()
	
    while True:
        #re-set background color
        set_background_color((r,g,b))
        
        # gets and clean the screen
        get_display()
        
        #draw image
        image('ball.png', (x,y))
        
        # renders to the screen
        update_display()
        
        #change direction and backgorund color
        if 'left' in keyboard() :
            if x>0: x -= 2
        if 'right' in keyboard() :
            if x < width: x += 2
        if 'down' in keyboard():    
            if y < height: y += 2
        if 'up' in keyboard() :
            if y>0: y -= 2    
        if 'r' in keyboard() :
            r= r+5 if r<255 else 0
        if 'g' in keyboard():
            g = g+5 if g<255 else 0
        if 'b' in keyboard():    
            b = b+5 if b<255 else 0

mainLoop()
