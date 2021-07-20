
from pygame import *
import pyganim

MOVE_SPEED = 5
WIDTH = 20
HEIGHT = 63
COLOR= "#888888"

JUMP_POWER=8
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
        

    def update(self,left,right,up,shot,platforms,blocks,entities,a):
        
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
        if shot:
            print("DA")
            bult=Bulet(self.rect.x,self.rect.y,32,self.lastdir)
            bulets.append(bult)  
            entities.add(bult)
        if not self.onGround:
            self.yvel+=GRAVITY
        
        self.onGround=False
        self.rect.y+=self.yvel
        self.collide(0,self.yvel,platforms,blocks,0)

        self.rect.x += self.xvel
        self.collide(self.xvel,0,platforms,blocks,a)
        for bu in bulets:
            bu.update(platforms,blocks,bulets,entities)

    def collide(self,xvel,yvel,platforms,blocks,a):
        for p in platforms:
            if sprite.collide_rect(self,p):
                if p.col==True:
                    if xvel>0:
                        if p.img_n!=10 :
                            self.rect.right = p.rect.left

                    if xvel<0:
                        if p.img_n!=10 :
                            self.rect.left = p.rect.right


                    if yvel>0:
                        if p.img_n!=10 :
                            self.rect.bottom = p.rect.top
                        if p.img_n==8 :
                            self.yvel=-11
                        else:
                            if p.img_n==10 :
                                self.onGround = True
                            else:  
                                self.onGround = True
                                self.yvel=0
                    if yvel<0:
                        if p.img_n!=10 :
                            self.rect.top = p.rect.bottom 
                            self.yvel=0
        left=False
        right=False
        MOVE_SPEED = 5
        for b in blocks:
            if sprite.collide_rect(self,b):
                if b.col==True:
                    if xvel>0:
                        self.rect.right = b.rect.left
                        right=True
                        left=False
                        b.xvel = self.xvel

                    if xvel<0:
                        self.rect.left = b.rect.right
                        left=True
                        right=False
                        b.xvel = self.xvel

                    if yvel>0:
                        self.rect.bottom = b.rect.top
                        self.onGround = True
                        self.yvel=0 
                        b.yvel = self.yvel

                    if yvel<0:
                        self.rect.top = b.rect.bottom
                        self.yvel=0
                        b.yvel = self.yvel
            if a ==1 and yvel==0:
                 m_s=self.rect.x
                 b.right=left
                 b.left=right
                 b.update(m_s,left,right,platforms,blocks)







class Bulet(sprite.Sprite):
    def __init__(self,x,y,dmg,lastdir):
        sprite.Sprite.__init__(self)   
        self.xvel=20
        self.yvel=0
        self.startX=x+10
        self.startY=y-10
        self.dir=lastdir
        if self.dir=='left':
            self.xvel= -self.xvel
        if self.dir=='right':
            self.xvel= self.xvel
        self.image = Surface((10,10))
        self.image.fill(Color("#888888"))
        self.rect = Rect(x+10, y+20, 10, 10)

    def kill(self):
        global entities, bulets
        for bl in bulets:
            bulets.pop(bulets.index(bl))
            del self 
        for e in entities:
            entities.pop(bulets.index(bl))
            del self 


    def update(self,platforms,blocks,bulets,entities):
        if self.xvel>0:
            if self.xvel-0.1<0:
                self.xvel=0
            else:
                self.xvel-=0.1
        if self.xvel<0:
            if self.xvel+0.1>0:
                self.xvel=0
            else:
                self.xvel+=0.1
        self.rect.y+=self.yvel
        self.collide(platforms,blocks,0,self.yvel,bulets)
        self.yvel+=0.35
        self.rect.x += self.xvel
        self.collide(platforms,blocks,self.xvel,0,bulets)



    def collide(self,platforms,blocks,xvel,yvel,bulets):
        for p in platforms:
            if sprite.collide_rect(self,p):
                if p.col==True:
                    
                    if xvel>0:
                        self.rect.right = p.rect.left
                        self.kill
                        self.xvel=0
                    
                    if xvel<0:
                        self.rect.left = p.rect.right
                        self.kill
                        self.xvel=0

                    if yvel>0:
                        self.rect.bottom = p.rect.top
                        self.kill
                        self.yvel=0

                    if yvel<0:
                        self.rect.top = p.rect.bottom
                        self.kill
                        self.yvel=0      
        for b in blocks:
            if sprite.collide_rect(self,b):
                if b!=self:
                    if xvel>0:
                        self.rect.right = b.rect.left
                        self.kill
                        self.xvel=0
                    if xvel<0:
                        self.rect.left = b.rect.right
                        self.kill
                        self.xvel=0
                    if yvel>0:
                        self.rect.bottom = b.rect.top
                        self.kill
                        self.yvel=0
                    if yvel<0:
                        self.rect.top = b.rect.bottom 
                        self.kill
                        self.yvel=0
                