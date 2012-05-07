#! /usr/bin/env python

# collision detection
from pypp4gamers import *

#setings
set_background_color(BLACK)

#initialize
pypp_init()

def mainLoop():
    x, y = 0, 0
    v = 5
    while True:
        #gets display and clean the screen
        get_display()
        
        # animation logic goes here
        draw_rect (size = (20,20) , pos=(x,y), color=(255,0,0), name='my_rect')
        
        # update display and renders the screen
        update_display()
        
        x += v
        y += v
            
mainLoop() 



