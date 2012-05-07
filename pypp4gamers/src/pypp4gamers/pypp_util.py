#       pypp_util.py is a part of the pypp4gamers project
#       
#       Copyright 2010-2011 Anderson Pierre Cardoso <apierre.cardoso@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the MIT License.
#       

import pygame
import os

class Music:
    def __init__(self, music_name="../static/default.mid", volume=1.0, play=False, loop=-1):
        self.music_name = music_name
        self.volume = volume
        self.play= play
        self.loop = loop
    
        
class Sound:
    def __init__(self, sound_path="../static/defaultsound.wav", volume=1.0, play=False, loop=0):
        self.sound_path = sound_path
        self.sound = pygame.mixer.Sound(sound_path)
        self.volume = volume
        self.loop = loop
        self.play = play
     
        
class Image:
    def __init__(self, name='default.png' ,path='../examples/static/default.png',show=False , pos=(400,300), w_center=None):
        if os.path.isfile(path):
            self.name = name
            self.path = path
            self.show = show
            self.image = pygame.image.load(path)
            self.pos = pos or (w_center[0] - self.image.get_width()/2, w_center[1] - self.image.get_height()/2)
        else:
            #raise exception
            pass
        
    def __get_width(self):
        return self.image.get_width()
    
    def __get_height(self):
        return self.image.get_height()
    
    width = property(__get_width)
    height = property(__get_height)
    
    def show_image(self, window):
        window.blit(self.image,self.pos) 
                     
class Shape:
    def __init__(self, name, shape_type=None, args={}, show = False):
        self.name = name
        self.shape_type = shape_type
        self.args = args
        self.show = show
        
    def draw_shape(self, window):
        if self.shape_type == 'rect': 
            pygame.draw.rect(window, self.args['color'], pygame.Rect(self.args['pos'], self.args['size']))
        elif self.shape_type == 'circle':
            pygame.draw.circle(window,self.args['color'],self.args['pos'],self.args['radius'])
        elif self.shape_type == 'ellipse':
            pygame.draw.ellipse(window, self.args['color'], pygame.Rect(self.args['pos'],self.args['size']))
        elif self.shape_type == 'line':
            pygame.draw.aaline(window, self.args['color'], self.args['start'], self.args['end'], self.args['smooth'])
        elif self.shape_type == 'polygon':
            pygame.draw.polygon(window, self.args['color'], self.args['points'])
        elif self.shape_type == 'point':
            pixArray = pygame.PixelArray(window)
            px,py = self.args['pos']
            pixArray[px][py] = self.args['color']
        #self.show = False

class Text:
    def __init__(self,rendered_text='', rect=None, show=False):
        self.rendered_text = rendered_text
        self.rect = rect
        self.show = show
        
