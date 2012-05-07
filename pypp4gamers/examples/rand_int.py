from pypp4gamers import *

set_background_color(BLACK)
set_frames_per_second(5)
set_window_size((600,600))

pypp_init()

def mainLoop():
    RED = (255,0,0)
    while True:
        get_display()
        
        for i in range(0,3):
            print_text (text = i+1, color=WHITE, pos=(100+i*200,100), )
        for i in range(0,3):
            print_text (text = i+4, color=WHITE, pos=(100+i*200,400), )
        
        aux = rand(low=0,high=6,type='int')    
        
        for i in range(0,3):
            if aux == i:
                draw_circle(radius=(20), pos=(100+i*200,160) , color=RED)
        for i in range(0,3):
            if aux == i+3:
                draw_circle(radius=(20), pos=(100+i*200,460) , color=RED)
        update_display()
        
mainLoop()    
    
