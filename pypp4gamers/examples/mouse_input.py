#! /usr/bin/env python

# mouse input example
from pypp4gamers import * 

pypp_init()

def mainLoop():
    R, G, B = 255, 255, 255
    x,y = mouse_pos()
    
    while True:
        set_background_color((R,G,B))
        get_display()
        
        image('ball.png', (x,y))
        
        update_display()
        
        #Using the mouse's click to change the background collor
        if mouse_click('left'): 
            if R<255: R+=5
            else: R=0
        if mouse_click('middle'): 
            if G<255: G+=5
            else: G=0
        if mouse_click('right'):
            if B<255: B+=5
            else: B = 0
        #Using the mouse position to move the ball
        x , y = mouse_pos()
          
mainLoop()
        
