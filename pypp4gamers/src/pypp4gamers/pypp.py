#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       pypp.py is a part of the pypp4gamers project
#       
#       Copyright 2010-2011 Anderson Pierre Cardoso <apierre.cardoso@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the MIT License 
#
'''
pypp does all the heavy work for the pypp4gamers project
this module defines the Pypp class with wraps pygame and other modules functions 
the access is made by the __init__ module (which is an interface for our project)
'''
import sys
import os
import pygame
from pygame.locals import *
from pypp_util import *
import random
 
WHITE = (255,255,255)
BLACK = (0,0,0)
# keyboard constants
keys = {K_BACKSPACE:'backspace', K_TAB:'tab', K_CLEAR:'clear', K_RETURN:'enter',
      K_PAUSE:'pause', K_ESCAPE:'esc' , K_SPACE:'space', K_EXCLAIM: '!', 
      K_QUOTEDBL:'"', K_HASH:'#', K_DOLLAR:'$', K_AMPERSAND:'&', K_QUOTE:"'",
      K_LEFTPAREN:'(', K_RIGHTPAREN:')', K_ASTERISK:'*', K_PLUS:'+', 
      K_COMMA:',', K_MINUS:'-', K_PERIOD:'.', K_SLASH:'/', K_0:'0', K_1:'1', 
      K_2:'2', K_3:'3', K_4:'4', K_5:'5', K_6:'6', K_7:'7', K_8:'8', K_9:'9',
      K_COLON:':', K_SEMICOLON:';', K_LESS:'<', K_EQUALS:'=', K_GREATER:'>', 
      K_QUESTION:'?', K_AT:'@', K_LEFTBRACKET:'[', K_BACKSLASH:'\\', 
      K_RIGHTBRACKET:']', K_CARET:'^', K_UNDERSCORE:'_', K_BACKQUOTE:'`', 
      K_a:'a', K_b:'b', K_c:'c', K_d:'d', K_e:'e', K_f:'f', K_g:'g', K_h:'h',
      K_i:'i', K_j:'j', K_k:'k', K_l:'l', K_m:'m', K_n:'n', K_o:'o', K_p:'p', 
      K_q:'q', K_r:'r', K_s:'s', K_t:'t', K_u:'u', K_v:'v', K_w:'w', K_x:'x', 
      K_y:'y', K_z:'z', K_DELETE:'delete', K_KP0:'keypad 0', K_KP1:'keypad 1',
      K_KP2:'keypad 2', K_KP3:'keypad 3', K_KP4:'keypad 4', K_KP5:'keypad 5',
      K_KP6:'keypad 6', K_KP7:'keypad 7', K_KP8:'keypad 8', K_KP9:'keypad 9', 
      K_KP_PERIOD:'keypad .', K_KP_DIVIDE:'keypad /', K_KP_MULTIPLY:'keypad *',
      K_KP_MINUS:'keypad -', K_KP_PLUS:'keypad +', K_KP_ENTER:'keypad enter', 
      K_KP_EQUALS:'keypad =', K_UP:'up', K_DOWN:'down', K_RIGHT:'right', 
      K_LEFT:'left',K_INSERT:'insert',K_HOME:'home',K_END:'end',K_PAGEUP:'PgUp',
      K_PAGEDOWN:'PgDn', K_F1:'F1', K_F2:'F2', K_F3:'F3',K_F4:'F4', K_F5:'F5', 
      K_F6:'F6', K_F7:'F7', K_F8:'F8', K_F9:'F9', K_F10:'F10', K_F11:'F11', 
      K_F12:'F12', K_F13:'F13', K_F14:'F14', K_F15:'F15', #K_NUMLOCK:'NumLock', 
      K_CAPSLOCK:'CapsLock', K_SCROLLOCK:'ScrollLock', K_RSHIFT:'shift r', 
      K_LSHIFT:'shift l', K_RCTRL:'ctrl r', K_LCTRL:'ctrl l', K_RALT:'alt r', 
      K_LALT:'alt l', K_RMETA:'meta r', K_LMETA:'meta r', K_LSUPER:'super l', 
      K_RSUPER:'super r',K_MODE:'mode shift',K_HELP:'help',K_PRINT:'PrintScreen',
      K_SYSREQ:'sysrq',K_BREAK:'break',K_MENU:'menu',K_POWER:'power',K_EURO:'euro'
      }


class Pypp:
  
    @classmethod
    def __hash_name(cls):
        """
        defines a random name for indenfying entitys and other features
        returns a string with the generated name
        """
        ##XXX:  unusefull in the new implementation?
        chars = 'abcdefghijklmnopkrstuvxywzABCDEFGHIJKLMNOPQRSTUVXYWZ1234567890'
        return ''.join([ chars[random.randint(0,len(chars)-1)] for i in xrange(7)])
        
    def __init__(self, size=(800,600), background=(255,255,255), fps=60):
        self.images = {}  # image_name -> Image()
        self.sounds = {}  # sound_name -> Sound()
        self.musics = {}  # music_name -> Music()
        self.texts = {}   # text -> Text()
        self.shapes = {}  # shape_name -> Shape()
        
        self.clock = pygame.time.Clock()
        
        pygame.init()
        
        self.SCREEN_SIZE = {'width':size[0],'height':size[1]}
        self.CENTER = (self.SCREEN_SIZE['width']/2, self.SCREEN_SIZE['height']/2) #image center
        self.BACKGROUNDCOLOR = background
        self.FPS = fps
        
        self.w = pygame.display.set_mode(tuple(self.SCREEN_SIZE.values()))
        pygame.display.set_caption("pypp 4 gamers")
        
        #self.run()      
 
    def __check_quit_event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
   
    def get_display(self): 
        self.w.fill(self.BACKGROUNDCOLOR) 
    
    def update_display(self):
        self.__draw_shapes()
        self.__show_images()
        self.__show_texts()
        self.__play_musics()
        self.__play_sounds()
        pygame.display.update()
        self.clock.tick(self.FPS)
        self.__check_quit_event()
    
    def run(self, has_mainLoop=True):
        pass
        
    #------------ drawings -----------------
    
    def __draw(self, shape_type, name, args):
        if not name in self.shapes: 
            self.shapes[name] = Shape(name=name, shape_type=shape_type, args=args, show=True)
        else:
            self.shapes[name].args = args
            self.shapes[name].show = True

    def hide_shape(self, name):
        if name in self.shapes:
            self.shapes[name].show = False

    def draw_rect(self, name, size=(100,100), pos=None, color=BLACK):
        """
        draws a rectangle
        usage:
            draw_rect(size, pos, color)
                size: tuple with width and height (default: (100,100).
                pos: tuple with the x and y position of the left upper corner of the rect (default: rect keep in the center of the screen)
                color: tuple with the r,g,b values for the color (default: Black)
                
        """
        pos = pos or (self.CENTER[0]-size[0]/2, self.CENTER[1]-size[1]/2) 
        self.__draw('rect', name, {'pos':pos, 'size': size, 'color':color})    
        
            
    def draw_circle(self, name, radius=(50), pos=None, color=BLACK, keep=False):
        """
        draws a circle
        usage:
            draw_circle(radius, pos, color)
                radius : integer for the radius of the circle (default: 50)
                pos : tuple with the x and y position  (default: circle keep in the center of the screen)
                color: tuple with the r,g,b values for the color (default: Black)
                
        """        
        pos = pos or (self.CENTER[0]-radius/2, self.CENTER[1]-radius/2)
        self.__draw('circle', name, {'radius' : radius, 'pos': pos, 'color': color})
              
    def draw_ellipse(self, name,  size=(200,100), pos=None, color=BLACK):
        """
        draws an ellipse
        usage: 
            draw_ellipse(size,pos,color)
                size: tuple for the size of the x and y axis of the ellipse (default: 200,100)
                pos: tuple for the x and y position for the ellipse (default: keep the ellipse in the center)
                color: tuple with the r,g,b values for the color (default: Black)
    
        """         
        pos = pos or (self.CENTER[0]-size[0]/2, self.CENTER[1]-size[1]/2)
        self.__draw('ellipse', name, {'size':size, 'pos':pos, 'color':color})  
             
    def draw_line(self, name, start=None, end=None, color=BLACK, smooth=False):
        """
        draws a line
        usage:
            draw_line(start,end,color,smooth)
                start: tuple for the the start point position, x and y, of the line 
                end: tuple for the the end point position, x and y, of the line
                color:  tuple with the r,g,b values for the color (default: Black)
                smooth: 'True' for an anti-alised line or 'False' to a nom-anti-alised line (default:True)
        """
        start = start or (self.CENTER[0]-100, self.CENTER[1]-100)
        end = end or (self.CENTER[0]+100, self.CENTER[1]+100)  
        self.__draw('line', name, {'start':start, 'end':end, 'color':color, 'smooth':smooth})
        
    def draw_polygon(self, name, points=[(300,200),(320,330),(470,280),(490,200)], color=BLACK):
        """
        draws a polygon
        usage:
            draw_polygon(points, color)
                points: a list of points(tuples) for the vertices of the polygon
                color:  tuple with the r,g,b values for the color (default: Black)
        """
        self.__draw('polygon', name, {'points':points, 'color':color})
        
    def draw_point(self, name, pos=None, color=BLACK ):
        """
        Draws a point.
        usage:
            draw_point(pos,color)
                pos: tuple for the x and y position for the point.
                color:  tuple with the r,g,b values for the color (default: Black)
        """
        pos = pos or self.CENTER  
        self.__draw('point', name, {'pos':pos, 'color':color})      
        
    def __draw_shapes(self): 
        [shape.draw_shape(self.w) for shape in self.shapes.itervalues() if shape.show]
        
    #----------- input Functions --------------------------
    
    def keyboard(self, keys=keys):
        """
        Return the key pressed.
        usage:
            keyboard()
            return: String with the name of the key pressed.
        """
        key_pressed = pygame.key.get_pressed()
        return [keys[key] for key in keys if key_pressed[key]]
    
    def mouse_pos(self, axis=''):
        """
        Return the position of the mouse in the given axis (or the tuple for both axis).
        usage:
            mouse_pos(axis)
            return: Return the 'axis' x or y position of the mouse,
                if not specified returns a tuple (x,y) with mouse's position. 
                (default: returns a tuple (x,y) with mouse's)
            arguments: 'x' | 'y'
        """
        x_pos,y_pos = pygame.mouse.get_pos()
        if axis == 'x': return x_pos
        elif axis == 'y': return y_pos
        else: return (x_pos, y_pos)
           
    def mouse_click(self, button='left'):
        """
        Verifies if a specified mouse's button was pressed.
        usage:
            mouse_click(button)
                Returns: True when the desired mouse button's is clicked the button. 
                arguments: 'left'| 'rigth' | 'middle' | 'any'
        """        
        (L,M,R) = pygame.mouse.get_pressed()
        if button == 'left' and L: return L
        elif button == 'middle' and M: return M
        elif button == 'right' and R: return R
        elif button == 'any' and (L or M or R): return True
        else: return False
   
    #------------ images ----------------------
   
    def image(self, image_path, pos):
        """
        Shows an image on the screen.
        usage:
           image(image_path,pos)
                image_name: String containing the file's path. (image should be previously imported before its use)
                pos: tuple with x and y position of the image (default: Shows the image in the screen's center point)
        """ 
        image_name = image_path.split('/')[-1]
        if not image_name in self.images:
            self.images[image_name] = Image(name=image_name, path=image_path, pos=pos, w_center=self.CENTER, show=True)
        else:
            self.images[image_name].show = True

    def hide_image(self, image_name):
        """
        Hides a, previously showed, image.
        usage:
            hide_image(image_name)
                image_name: String containing the file's name without patch (returns a log error if no image is being showed)
        """
        if image_name in self.images:
            self.images[image_name].show = False
                
    def __show_images(self):
        # shows all the stored images if active (img.show)
        [img.show_image(self.w) for img in self.images.itervalues() if img and img.show]
        
    #------------------ music and sound -----------------------------
    
    def music(self, music_path='',volume=1.0,loop=1):    
        '''
        Plays a music. Supports .ogg and .mid, the mp3 support is limited (you can try, but it depends from music to music)
        usage:
            music(music,volume,loop)
                music: String containing the music's name without patch. (music should be previously imported before its use)
                volume: Sets the music volume (0.0 to 0%) and (1.0 to 100%)
                loop: Number of times that the music will be repeated (-1 to infinite loop) (0 to play once) (1 to repeat once)
        '''  
        music = music_path.split('/')[-1]  
        if not music in self.musics : 
            self. musics[music]=Music(music_name = music_path, volume = volume, loop=loop,  play=True)
        elif not self.musics[music].play :
            self.musics[music].play = True
            
    def stop_music(self, file_name='default.mid'):
        """
        Stops a music in execution.
        usage:
            stop_music(file_name)
                file: String containing the name of the music to be stoped(returns a log error if no music is being played)
        """
        if file_name in self.musics:
            self.musics[file_name].play = False
            pygame.mixer.music.stop() 
            
    def __play_musics(self):
        def __play(music):
            pygame.mixer.music.load(music.music_name)
            pygame.mixer.music.set_volume(music.volume)
            pygame.mixer.music.play(music.loop)   
            music.play = False
        map(lambda music: __play(music), 
            filter(lambda music: music.play, self.musics.itervalues()))

    def sound(self, sound_path='',volume=1.0,loop=0):
        """
        Plays a sound.
            usage:
               sound(file,volume,loop)
                    file_name: String containing the file's name without patch. (sound should be previously imported before its use)
                    volume: Sets the sound volume (0.0 to 0%) and (1.0 to 100%)
                    loop: Number of times that the music will be repeated (-1 to infinite loop) (0 to play once) (1 to repeat once)
        """
        if not pygame.mixer.get_init(): 
            pygame.mixer.init() 
        sound = sound_path.split('/')[-1] 
        if not sound in self.sounds:    
            self.sounds[sound]=Sound(sound_path = sound_path, volume = volume, loop=loop, play=True)
        else:
            self.sounds[sound].play = True

    def __play_sounds(self):
        def __play(sound):
            sound.sound.play(sound.loop)
            # I really dont like this...
            while pygame.mixer.get_busy():
                self.clock.tick(self.FPS)
            sound.play = False
        map(lambda sound: __play(sound), 
            filter(lambda sound: sound.play, self.sounds.itervalues()))

    
    #----------------------- text ----------------------------
    
    def  print_text(self, text='', color=BLACK, pos=None, font_size=30):
        """
        Prints a text on the screen.
        usage:
            print_text(text,color,pos,font_size)
                text: string containing the text to be showed
                color:  tuple with the r,g,b values for the color (default: Black)
                pos: tuple for the x and y position for the text (default: keep the text in the center)
                font_size: set the text's size.
        """
        pos = pos or self.CENTER
        try: 
            text = text if isinstance(text,str) else repr(text)
            if not text in self.texts:
                font_ = pygame.font.SysFont(None, font_size)
                rendered_text = font_.render(text, True, color)
                text_rect = rendered_text.get_rect()
                text_rect.center=pos
                self.texts[text] = Text(rendered_text = rendered_text, rect = text_rect, show = True)
            else:
                self.texts[text].show = True
        except: 
            pass
        
    def __show_texts(self):
        map(lambda text: self.w.blit(text.rendered_text, text.rect),
            filter(lambda text: text.show, self.texts.itervalues()))

    def hide_text(self, text=''):
        """
        hides an already loaded text
        usage:
            hide_text(text)
                text: string of the text object to be hidden
        """
        if text and text in self.texts:
            self.texts[text].show = False
            
    #------------------------ utilitys ----------------------------------
    
    def rand(self, low = 0.0, high=10.0, type= 'int'):
        """
        Returns a random number.
        usage:
            rand(low,high,tipe)
                low: The lowest intervalue's number.
                high: The highest intervalue's number.
                tipe: 'int' | 'float'
        """
        low,high = (low,high) if low < high else (high,low)
        return random.randint(low,high) if type == 'int' else random.uniform(low,high)
    
    def sleep(self, milliseconds=1000): 
        """
        sleeps for an amount of time given by milliseconds
        usage:
            sleep_time(milliseconds)
                milliseconds: integer representing the milliseconds to be waited
        """
        if isinstance(milliseconds, int):
            pygame.time.wait(milliseconds) 
            
    def collision_dect(self, obj1 = None, obj2 = 'window'):
        """
        Test if the objects(rect) passed have collided
        usage:
            collision_dect(obj1, obj2)
                obj1: is an object (image, shape, etc)
                obj2: another object (image,shape,etc)
        """
        #TODO: implement-me
        # use Rect.colliderect
        if(obj2 == 'window'): 
            #implement default
            pass
        else:
            pass
        pass
            
