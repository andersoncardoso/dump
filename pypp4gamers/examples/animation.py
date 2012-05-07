#! /usr/bin/env python

# animation
from pypp4gamers import *

#setings
set_background_color(BLACK)

#initialize
pypp_init()

# defines main loop
def mainLoop():
    x=10
    y=20
    vx = 5
    vy = 5
    width, height = get_screen_width(), get_screen_height()
    
    while True:
        #gets display and clean the screen
        get_display()
        
        # animation logic goes here
        x = x+vx
        y = y+vy
        #draw_rect(name = 'square', size = (20,20) , pos=(x,y), color=(255,0,0))
        draw_circle('a', radius=20, pos=(x,y), color=(255,0,0))
        
        # update display and renders the screen
        update_display()
        
        
        if x > width-20 or x<0:
            vx = -vx
        if y > height-20 or y<0:
            vy = -vy
            
mainLoop() 



