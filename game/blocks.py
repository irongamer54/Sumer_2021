import pygame
from pygame import *
from pygame import sprite



MOVE_SPEED = 5
GRAVITY=0.35

image = [image.load('kam.png'),            #0        
         image.load('kam_flag.png'),        #1       
         image.load('kam_pol_cverxy.png'),   #2       
         image.load('kam_pol_cnizy.png'),     #3      
         image.load('kam_plitka.png'),         #4     
         image.load('kam_plitka_flag.png'),     #5   
         image.load('kam_plitka_fakel.png'),     #6  
         image.load('kam_polyb.png'),             #7 
         image.load('kam_polyb_flag.png'),         #8
         image.load('box.png'),                     #9
         image.load('leca.png'),                     #10
         image.load('wood.png'),                      #11
         image.load('wood_plank.png'),                 #12
         image.load('wood_plank_pol.png'),              #13
         image.load('wood_plank_pol_flag.png'),          #14
         ]

class Platform(sprite.Sprite):
    def __init__(self,x,y,width,hight,a,img_nam):
        sprite.Sprite.__init__(self)
        self.image=Surface((width,hight))
        self.image = image[img_nam]
        self.rect = Rect(x,y,width,hight)
        self.col = a




class Block(sprite.Sprite):
    def __init__(self,x,y,width,hight):
        sprite.Sprite.__init__(self)
        self.image=Surface((width,hight))
        self.image = image[9]
        self.rect = Rect(x,y,width,hight)
        self.col = True

    def update(self,left,right,platforms):
        if left:
            self.xvel= -MOVE_SPEED
        if right:
            self.xvel= -MOVE_SPEED
           
        if not self.onGround:
            self.yvel+=GRAVITY
            
        self.onGround=False
        self.rect.y+=self.yvel
        self.collide(0,self.yvel,platforms)

        self.rect.x += self.xvel
        self.collide(self.xvel,0,platforms)


    def collide(self,xvel,yvel,platforms):
        for p in platforms:
            if sprite.collide_rect(self,p):
                if p.col==True:
                    if xvel>0:
                        self.rect.right = p.rect.left

                    if xvel<0:
                        self.rect.left = p.rect.right


                    if yvel>0:
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.yvel=0

                    if yvel<0:
                        self.rect.top = p.rect.bottom  
                        self.yvel=0