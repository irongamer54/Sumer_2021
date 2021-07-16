import pygame
from pygame import *

image = [image.load('rfvtym.png'),
         image.load('rfvtym2.png'),
         image.load('box.png'),
         image.load('wood_pol.png'),
         ]

class Platform(sprite.Sprite):
    def __init__(self,x,y,width,hight,a,img_nam):
        sprite.Sprite.__init__(self)
        self.image=Surface((width,hight))
        self.image = image[img_nam]
        self.rect = Rect(x,y,width,hight)
        self.col = a
