from pygame import *
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

    def kill(self,bulets):
        for bl in bulets:
            bulets.pop(bulets.index(bl))
            del self 


    def update(self,platforms,blocks,bulets):
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
                        self.kill(bulets)
                        self.xvel=0
                    
                    if xvel<0:
                        self.rect.left = p.rect.right
                        self.kill(bulets)
                        self.xvel=0

                    if yvel>0:
                        self.rect.bottom = p.rect.top
                        self.kill(bulets)
                        self.yvel=0

                    if yvel<0:
                        self.rect.top = p.rect.bottom
                        self.kill(bulets)
                        self.yvel=0      
        for b in blocks:
            if sprite.collide_rect(self,b):
                if b!=self:
                    if xvel>0:
                        self.rect.right = b.rect.left
                        self.kill(bulets)
                        self.xvel=0
                    if xvel<0:
                        self.rect.left = b.rect.right
                        self.kill(bulets)
                        self.xvel=0
                    if yvel>0:
                        self.rect.bottom = b.rect.top
                        self.kill(bulets)
                        self.yvel=0
                    if yvel<0:
                        self.rect.top = b.rect.bottom 
                        self.kill(bulets)
                        self.yvel=0
                


