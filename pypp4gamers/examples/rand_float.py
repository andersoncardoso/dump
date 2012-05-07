#! /usr/bin/env python

from pypp4gamers import *

#settings
set_background_color(BLACK)
set_window_size((300,500)) 

pypp_init()  
 
def mainLoop():
    num = None
    while True:
        get_display()
        if 'enter' in keyboard():
            hide_text(num)
            num = str(rand(low=0.0, high=20.0,type='float'))
            print_text(text=num,color=WHITE,font_size=40)

        update_display()

       
mainLoop()
            
        
        
            
            
            


