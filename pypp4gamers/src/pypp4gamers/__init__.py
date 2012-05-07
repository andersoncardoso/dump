#  __init__.py is part of the pypp4gamers project 
#
# this program is licensed under the MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# copyright 2010/2011 Anderson
#
"""facade for pypp4gamers"""

import os
import pypp

#------------ constants and references section ----------

p = None
WINDOW_SIZE = (800,600)
WHITE = (255,255,255)
BLACK = (0,0,0)
BACKGROUNDCOLOR = WHITE
FPS = 60
#STATIC_IMAGE_PATH = '/../../static/image'
#STATIC_SOUND_PATH = '/../../static/sound'
STATIC_IMAGE_PATH = '/static/image'
STATIC_SOUND_PATH = '/static/sound'

#------------- facade definitions section ----------------

#--------- window, construction and running section ------

def set_window_size(size=(800,600)):
    global WINDOW_SIZE
    WINDOW_SIZE = size
    if p : p.SCREEN_SIZE = {'width':size[0],'height':size[1]}

def get_screen_width():
    return WINDOW_SIZE[0]
    
def get_screen_height():
    return WINDOW_SIZE[1]

def set_background_color(color=WHITE):
    global BACKGROUNDCOLOR
    BACKGROUNDCOLOR = color
    if p: p.BACKGROUNDCOLOR = color

def set_frames_per_second(fps=60):    
    global FPS
    FPS = fps
   
def pypp_init():
    global p
    p = pypp.Pypp(WINDOW_SIZE, BACKGROUNDCOLOR, FPS)
    
def get_display():
    p.get_display()
    
def update_display():
    p.update_display()
    
def run():
    p.run()
    
#--------------------- drawings section -------------------------------
    
def hide_shape(name=''):
    p.hide_shape(name)

def draw_rect(name, size=(100,100), pos=None, color=BLACK):
    """
    draws a rectangle
    usage:
        draw_rect(size, pos, color)
            size: tuple with width and height (default: (100,100).
            pos: tuple with the x and y position of the left upper corner of the rect (default: rect keep in the center of the screen)
            color: tuple with the r,g,b values for the color (default: Black)
            keep : boolean that sets if the shape shoud keep on the screnn (after an event) (default: False)
            
    """
    p.draw_rect(name, size, pos, color)
    
def draw_circle(name, radius=(50), pos=None, color=BLACK):
    """
    draws a circle
    usage:
        draw_circle(radius, pos, color)
            radius : integer for the radius of the circle (default: 50)
            pos : tuple with the x and y position  (default: circle keep in the center of the screen)
            color: tuple with the r,g,b values for the color (default: Black)
            keep : boolean that sets if the shape shoud keep on the screnn (after an event) (default: False)

            
    """ 

    p.draw_circle(name, radius, pos, color)
    
def draw_ellipse(name, size=(200,100), pos=None, color=BLACK):
    """
    draws an ellipse
    usage: 
        draw_ellipse(size,pos,color)
            size: tuple for the size of the x and y axis of the ellipse (default: 200,100)
            pos: tuple for the x and y position for the ellipse (default: keep the ellipse in the center)
            color: tuple with the r,g,b values for the color (default: Black)
            keep : boolean that sets if the shape shoud keep on the screnn (after an event) (default: False)
    """         
    p.draw_ellipse(name, size, pos, color)
    
def draw_line(name, start=None, end=None, color=BLACK, smooth=False):
    """
    draws a line
    usage:
        draw_line(start,end,color,smooth)
            start: tuple for the the start point position, x and y, of the line 
            end: tuple for the the end point position, x and y, of the line
            color:  tuple with the r,g,b values for the color (default: Black)
            smooth: 'True' for an anti-alised line or 'False' to a nom-anti-alised line (default:True)
            keep : boolean that sets if the shape shoud keep on the screnn (after an event) (default: False)
    """
    p.draw_line(name, start, end, color, smooth)
    
def draw_polygon(name, points=[(300,200),(320,330),(470,280),(490,200)], color=BLACK):
    """
    draws a polygon
    usage:
        draw_polygon(points, color)
            points: a list of points(tuples) for the vertices of the polygon
            color:  tuple with the r,g,b values for the color (default: Black)
            keep : boolean that sets if the shape shoud keep on the screnn (after an event) (default: False)
    """
    p.draw_polygon(name, points, color)
    
def draw_point(name, pos=None, color=BLACK ):
    """
    Draws a point.
    usage:
        draw_point(pos,color)
            pos: tuple for the x and y position for the point.
            color:  tuple with the r,g,b values for the color (default: Black)
            keep : boolean that sets if the shape shoud keep on the screnn (after an event) (default: False)
    """
    p.draw_point(name, pos, color)
    
#---------------------- input  section ----------------------------------

def keyboard():
    """
    Return the key pressed.
    usage:
        keyboard()
        return: String with the name of the key pressed.
    """
    return p.keyboard()
    
def mouse_pos(axis=''):
    """
    Return the position of the mouse in the given axis (or the tuple for both axis).
    usage:
        mouse_pos(axis)
        return: Return the 'axis' x or y position of the mouse,
            if not specified returns a tuple (x,y) with mouse's position. 
            (default: returns a tuple (x,y) with mouse's)
        arguments: 'x' | 'y'
    """
    return p.mouse_pos(axis)
    
def mouse_click(button='left'):
    """
    Verifies if a specified mouse's button was pressed.
    usage:
        mouse_click(button)
            Returns: True when the desired mouse button's is clicked the button. 
            arguments: 'left'| 'rigth' | 'middle' | 'any'
    """       
    return p.mouse_click(button)

#--------------------- image section ---------------------------

def image(image_name='default.png', pos=None):
    """
    Shows an image on the screen.
    usage:
       image(image_name,pos)
            image_name: String containing the file's name without patch. (image should be previously imported before its use)
            pos: tuple with x and y position of the image (default: Shows the image in the screen's center point)
    """
    if not isinstance(image_name, str): return
    #configure path
    image_path = os.path.join(os.path.dirname(__file__) + STATIC_IMAGE_PATH , image_name)  
    p.image(image_path, pos)     
    
def hide_image(image_name='default.png'):
    """
    Hides a, previously showed, image.
    usage:
        hide_image(image_name)
            image_name: String containing the file's name without patch (returns a log error if no image is being showed)
    """
    p.hide_image(image_name)
    
#------------------- music and sound section --------------------

def music(file_name='default.mid',volume=1.0,loop=1):
    '''
    Plays a music. Supports .ogg and .mid, the mp3 support is limited (you can try, but it depends from music to music)
    usage:
        music(music,volume,loop)
            music: String containing the music's name without patch. (music should be previously imported before its use)
            volume: Sets the music volume (0.0 to 0%) and (1.0 to 100%)
            loop: Number of times that the music will be repeated (-1 to infinite loop) (0 to play once) (1 to repeat once)
    '''  
    if not isinstance(file_name,str): return
    #configure path
    music_path=os.path.join(os.path.dirname(__file__) + STATIC_SOUND_PATH,  file_name)
    p.music(music_path, volume, loop)
    
def stop_music(file_name='default.mid'):
    """
    Stops a music in execution.
    usage:
        stop_music(file_name)
            file: String containing the name of the music to be stoped(returns a log error if no music is being played)
    """
    p.stop_music(file_name)

def sound(file_name='defaultsound.wav',volume=1.0,loop=0):
    """
    Plays a sound.
        usage:
           sound(file,volume,loop)
                file_name: String containing the file's name without patch. (sound should be previously imported before its use)
                volume: Sets the sound volume (0.0 to 0%) and (1.0 to 100%)
                loop: Number of times that the music will be repeated (-1 to infinite loop) (0 to play once) (1 to repeat once)
    """
    if not isinstance(file_name, str): return
    sound_path=os.path.join(os.path.dirname(__file__) + STATIC_SOUND_PATH,  file_name)
    p.sound(sound_path, volume, loop)

#----------------------- text section ------------------------------

def  print_text(text='', color=BLACK, pos=None, font_size=30):
    """
    Prints a text on the screen.
    usage:
        print_text(text,color,pos,font_size)
            text: string containing the text to be showed
            color:  tuple with the r,g,b values for the color (default: Black)
            pos: tuple for the x and y position for the text (default: keep the text in the center)
            font_size: set the text's size.
    """
    p.print_text(text, color, pos, font_size)
    
def hide_text(text=''):
    """
    hides an already loaded text
    usage:
        hide_text(text)
            text: string of the text object to be hidden
    """
    p.hide_text(text)

#--------------------- utility section -----------------------------

def rand(low = 0.0, high=10.0, type= 'int'):
    """
    Returns a random number.
    usage:
        rand(low,high,type)
            low: The lowest intervalue's number.
            high: The highest intervalue's number.
            type: 'int' | 'float'
    """
    return p.rand(low,high,type)
    
def sleep(milliseconds=1000): 
    """
    sleeps for an amount of time given by milliseconds
    usage:
        sleep(milliseconds)
            milliseconds: integer representing the milliseconds to be waited
    """
    p.sleep(milliseconds)
    
def collision_dect(obj1 = None, obj2 = 'window'):
    """
    Test if the objects(rect) passed have collided
    usage:
        collision_dect(obj1, obj2)
            obj1: is an object (image, shape, etc)
            obj2: another object (image,shape,etc)
    """
    p.collision_dect(obj1, obj2)
