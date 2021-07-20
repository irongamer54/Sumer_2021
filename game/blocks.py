import pygame
from pygame import *
from pygame import sprite
from main_new import entities, platforms

JUMP_POWER=8
MOVE_SPEED_s= -0.001
GRAVITY=0.35
TREN=0.8
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
         image.load('wood_ras.png'),                      #15
         ]

class Platform(sprite.Sprite):
    def __init__(self,x,y,width,hight,a,img_nam):
        
        sprite.Sprite.__init__(self)
        self.image=Surface((width,hight))
        self.image = image[img_nam]
        self.rect = Rect(x,y,width,hight)
        self.col = a
        self.img_n=img_nam
        if img_nam==15:
            self.die=True
        else:
            self.die=False

    def kill(self):
        global entities, platforms
        print(len(entities))
        for bl in platforms:
            if bl == self:
                platforms.pop(platforms.index(bl))
        for e in entities:
            if e == self:
                entities.remove(e)




class Block(sprite.Sprite):
    def __init__(self,x,y,width,hight):
        sprite.Sprite.__init__(self)
        self.xvel=0
        self.yvel=0
        self.right=False
        self.left=False
        self.image=Surface((width,hight))
        self.image = image[9]
        self.rect = Rect(x,y,width,hight)
        self.onGround=False
        self.col = True
        self.tren=TREN

    def update(self,m_s,left,right,platforms,blocks):
        if self.left and left:
            self.xvel= -MOVE_SPEED_s
            
        if self.right and right:
            self.xvel= MOVE_SPEED_s
            
        if not (self.left or self.right):
            if self.xvel>0:
                if self.xvel-self.tren<0:
                    self.xvel=0
                else:
                    self.xvel-=self.tren
            if self.xvel<0:
                if self.xvel+self.tren>0:
                    self.xvel=0
                else:
                    self.xvel+=self.tren
        if not self.onGround:
            self.tren=0.01
            self.yvel+=GRAVITY
        self.onGround=False
        self.rect.y+=self.yvel

        self.collide(0,self.yvel,platforms,blocks)
        self.rect.x += self.xvel
        self.collide(self.xvel,0,platforms,blocks)
        self.right=False
        self.left=False
        
    def collide(self,xvel,yvel,platforms,blocks):
        for p in platforms:
            if sprite.collide_rect(self,p):
                if p.col==True:
                    
                    if xvel>0:
                        self.rect.right = p.rect.left
                        self.right=False
                        self.xvel=0
                    
                    if xvel<0:
                        self.rect.left = p.rect.right
                        self.left=False
                        self.xvel=0

                    if yvel>0:
                        self.rect.bottom = p.rect.top
                        if p.img_n==8 :
                            self.tren=0.1
                            self.yvel=-JUMP_POWER
                        else:
                            self.tren=TREN
                            self.onGround = True
                            self.yvel=0

                    if yvel<0:
                        self.rect.top = p.rect.bottom
                        self.onGround==False  
                        self.yvel=0
        left=False
        right=False        
        for b in blocks:
            if sprite.collide_rect(self,b):
                if b!=self:
                    if xvel>0:
                        self.rect.right = b.rect.left
                        b.xvel = self.xvel
                        right=True
                        left=False

                    if xvel<0:
                        self.rect.left = b.rect.right
                        b.xvel = self.xvel
                        left=True
                        right=False

                    if yvel>0:
                        self.rect.bottom = b.rect.top
                        self.onGround = True
                        self.yvel=0

                    if yvel<0:
                        self.rect.top = b.rect.bottom  
                        self.yvel=0
                    b.right=left
                    b.left=right
                    b.update(0,left,right,platforms,blocks)
