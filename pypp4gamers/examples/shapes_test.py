#! /usr/bin/env python

# drawing shapes
from pypp4gamers import *

pypp_init()

def mainLoop():
    while True:
        #clean the screen and handle events
        get_display()

        if 'enter' in keyboard():
            draw_rect(name='sqr', size=(50,50), color=(255,0,0))
            draw_circle('circ', radius=30, pos=(40,40), color=(0,255,0))
            draw_ellipse(name='el', size=(100,50), pos=(300,400), color=(0,0,255))
            draw_line('l', start=(600,10), end=(600, 300))
            draw_polygon('poly', points=[(250,100),(250,300),(350,200)], color=(125,125,125))
            draw_point('pto', pos= (500,500), color=(255,0,0))

        if 'space' in keyboard():
            hide_shape('sqr')
            hide_shape('circ')
            hide_shape('el')
            hide_shape('l')
            hide_shape('poly')
            hide_shape('pto')

        #render the screen
        update_display()

mainLoop()
