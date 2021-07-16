from pygame import *
import pyganim
MOVE_SPEED = 5
WIDTH = 32
HEIGHT = 64
COLOR= "#888888"

JUMP_POWER=11
GRAVITY=0.35

ANIMATION_DELAY = 0.1 # скорость смены кадров
ANIMATION_RIGHT =[
            image.load('pers2.png'),
            image.load('pers3.png'),
            image.load('pers4.png'),
            image.load('pers5.png'),
            image.load('pers6.png')
         ]
ANIMATION_STAY = image.load('pers1.png')
animCount=0


class Player(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.xvel=0
        self.yvel=0
        self.startX=x
        self.startY=y
        self.animCount=0
        self.lastdir="right"
        self.onGround=False
        self.image=Surface((WIDTH,HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x,y,WIDTH,HEIGHT)
        self.image.set_colorkey(Color(COLOR))
        

    def update(self,left,right,up,platforms):
        if self.animCount+1>=15:
            
            self.animCount=0
        if left:
            self.image=ANIMATION_RIGHT[self.animCount//3]
            self.image = transform.flip(self.image, True, False)
            self.animCount+=1
            self.xvel= -MOVE_SPEED
            self.lastdir="left"
        if right:
            self.image=ANIMATION_RIGHT[self.animCount//3]
            self.animCount+=1
            self.xvel= MOVE_SPEED
            self.lastdir="right"
        if up:
            if self.onGround:
                self.yvel=-JUMP_POWER
        
        if not (left or right):
            self.xvel=0
            if self.lastdir=="right":
                self.image=ANIMATION_STAY
            if self.lastdir=="left":
                self.image=ANIMATION_STAY
                self.image = transform.flip(self.image, True, False)
            
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
        