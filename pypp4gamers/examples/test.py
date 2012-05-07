#this is a junkie test for development, dont bother understanding
#better examples will be put here latter

from pypp4gamers import *

#set_window_size((800,100))
pypp_init()

def mainLoop():
    is_on = False
    s = 'helloooo pypp world!!!'
    num = ''
    while True: 
        get_display()
        if "enter" in keyboard():
            print num
            hide_text(num) 
            num = str(rand(type='float'))
            print_text(num)
#            draw_rect(keep=True, name='')
#        draw_rect()
#        draw_line(start=(10,10), end=(790,10))
        if mouse_click('left'): 
            print_text(s)
#            sound()
#            music()
#            draw_circle(pos=(300,300), radius=50, color=(0,0,155), keep=True)
#            image()
        if mouse_click('right'):
            hide_text(s)
            stop_music()
#            hide_image('default.png')
#        draw_circle(pos=(300,300), radius=50, color=(0,0,155))
        update_display()

mainLoop()
