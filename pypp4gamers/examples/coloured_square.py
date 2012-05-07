#! /usr/bin/env python

# simple animation -> color changing square

from pypp4gamers import *

pypp_init()

def mainLoop():
    # variables for the rgb values
	r, g, b = 0, 0, 0
	
	while True:
		#clean the screen and handle events
		get_display()
		
		#draw a rectangle to the screen
		draw_rect(name='sqr', size=(200,200), color=(r,g,b))
		
		#render the screen
		update_display()
		
        # update in the color values
		if r < 255: r += 1
		elif g < 255: g += 1
		elif b < 255: b += 1
		else: r, g, b = 0, 0, 0

mainLoop()
