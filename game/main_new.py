#from bulets import Bulet
#from blocks import *
import json
import pygame
from pygame import *
from pygame import sprite

WIN_WIDTH=700
WIN_HIGHT=500
DISPLAY = (WIN_WIDTH,WIN_HIGHT)
BACKGROUND_COLOR="#004400"



#####################player#####################
MOVE_SPEED = 5
WIDTH = 20
HEIGHT = 63
COLOR= "#888888"

JUMP_POWER=8
GRAVITY=0.35



ANIMATION_DELAY = 0.1 # скорость смены кадров
ANIMATION_RIGHT =[
            pygame.image.load('pers2.png'),
            pygame.image.load('pers3.png'),
            pygame.image.load('pers4.png'),
            pygame.image.load('pers5.png'),
            pygame.image.load('pers6.png')
         ]
ANIMATION_STAY = pygame.image.load('pers1.png')
ANIMATION_CKN =[
            [
                pygame.image.load('ckn_1.png'),
                pygame.image.load('ckn_2.png'),
                pygame.image.load('ckn_3.png'),
                pygame.image.load('ckn_4.png'),
                pygame.image.load('ckn_5.png'),
                pygame.image.load('ckn_6.png'),
                pygame.image.load('ckn_7.png')
            ],
            [
                pygame.image.load('ckn_1_h.png'),
                pygame.image.load('ckn_2_h.png'),
                pygame.image.load('ckn_3_h.png'),
                pygame.image.load('ckn_4_h.png'),
                pygame.image.load('ckn_5_h.png'),
                pygame.image.load('ckn_6_h.png'),
                pygame.image.load('ckn_7_h.png')
            ],
            [
                pygame.image.load('ckn_1_s.png'),
                pygame.image.load('ckn_2_s.png'),
                pygame.image.load('ckn_3_s.png'),
                pygame.image.load('ckn_4_s.png'),
                pygame.image.load('ckn_5_s.png'),
                pygame.image.load('ckn_6_s.png'),
                pygame.image.load('ckn_7_s.png')
            ]

         ]
animCount=0
###################################################
ckn_c=0
fon=Surface((WIN_WIDTH,WIN_HIGHT))   
fon = pygame.image.load('fon.png')
fon= pygame.transform.scale(fon, (WIN_WIDTH,WIN_HIGHT))

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)
	
    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIN_WIDTH / 2, -t+WIN_HIGHT / 2

    l = min(0, l)                           # Не движемся дальше левой границы
    l = max(-(camera.width-WIN_WIDTH), l)   # Не движемся дальше правой границы
    t = max(-(camera.height-WIN_HIGHT), t) # Не движемся дальше нижней границы
    t = min(0, t)                           # Не движемся дальше верхней границы

    return Rect(l, t, w, h)      
left_b=right_b=False
m_c=0
def map_new (a):
    global flag,shot,left,right,up,entities,platforms,blocks,bulets,level,hero,camera,m_c,btn_prs,bg_map,bg_map_e,turels,ckn,reload,ckn_c
    flag=shot=left=right=up=reload=False
    if a>0:
        m_c=a

    if a == 0:
        ckn_c=[]
    entities = pygame.sprite.Group()
    platforms=[]
    blocks=[]
    bulets=[]
    turels=[]
    ckn=[]
    btn_prs=0
    x=y=0
    for row in level[m_c]:
        print('da')
        for col in row:
            #if col==" ":
            #   pf=Platform(x,y,32,32,False,0)
            #  entities.add(pf)
            # platforms.append(pf)
            if col=="p":
                hero=Player(x,y,m_c+1)
            if col=="0":
                pf=Platform(x,y,32,32,True,10)
                entities.add(pf)
                platforms.append(pf)
            if col=="1":
                pf=Platform(x,y,32,32,True,1)
                entities.add(pf)
                platforms.append(pf)
            if col=="2":
                pf=Platform(x,y,32,32,True,2)
                entities.add(pf)
                platforms.append(pf)
            if col=="3":
                pf=Platform(x,y,32,32,True,3)
                entities.add(pf)
                platforms.append(pf)
            if col=="4":
                pf=Platform(x,y,32,17,True,4)
                entities.add(pf)
                platforms.append(pf)
            if col=="5":
                pf=Platform(x,y,32,32,True,5)
                entities.add(pf)
                platforms.append(pf)
            if col=="6":
                pf=Platform(x,y,32,32,True,6)
                entities.add(pf)
                platforms.append(pf)
            if col=="7":
                pf=Platform(x,y,32,32,True,7)
                entities.add(pf)
                platforms.append(pf)
            if col=="8":
                pf=Platform(x,y,32,17,True,8)
                entities.add(pf)
                platforms.append(pf)
            if col=="9":
                bl=Block(x,y,32,32)
                entities.add(bl)
                blocks.append(bl)
            if col=="-":
                pf=Platform(x,y,32,32,True,0)
                entities.add(pf)
                platforms.append(pf)
            if col=="+":
                pf=Platform(x,y,32,32,True,11)
                entities.add(pf)
                platforms.append(pf)
            if col=="*":
                pf=Platform(x,y,32,32,True,12)
                entities.add(pf)
                platforms.append(pf)
            if col=="@":
                pf=Platform(x,y,32,17,True,13)
                entities.add(pf)
                platforms.append(pf)
            if col=="%":
                pf=Platform(x,y,32,32,True,14)
                entities.add(pf)
                platforms.append(pf)
            if col=="$":
                pf=Platform(x-2,y,32+2,32,True,15)
                entities.add(pf)
                platforms.append(pf)
            if col=="^":
                pf=Platform(x,y,32,32,True,16)
                entities.add(pf)
                platforms.append(pf)
            if col==">":
                pf=Platform(x+1,y,32,32,True,17)
                entities.add(pf)
                platforms.append(pf)
            if col=="<":
                pf=Platform(x-1,y,32,32,True,18)
                entities.add(pf)
                platforms.append(pf)
            if col=="|":
                pf=Platform(x+20,y,10,64,True,19)
                entities.add(pf)
                platforms.append(pf)
            if col=="#":
                pf=Platform(x,y,32,32,True,21)
                entities.add(pf)
                platforms.append(pf)
            if col==".":
                pf=Platform(x,y,32,32,True,22)
                entities.add(pf)
                platforms.append(pf)
            if col=="T":
                pf=Turel(x,y,'left')
                entities.add(pf)
                turels.append(pf)
            if col=="t":
                pf=Turel(x,y,'right')
                entities.add(pf)
                turels.append(pf)
            if col=="c":
                pf=NPC(x+10,y-5,10,15,True,0)
                entities.add(pf)
                ckn.append(pf)
            if col=="C":
                pf=NPC(x+10,y-5,10,15,True,1)
                entities.add(pf)
                ckn.append(pf)
            if col=="S":
                pf=NPC(x+10,y-5,10,15,True,2)
                entities.add(pf)
                ckn.append(pf)
            if col=="!":
                pf=Platform(x,y+10,32,20,True,23)
                entities.add(pf)
                platforms.append(pf)
            x+=32
        y+=32
        x=0
    print(entities)
    entities.add(hero)
    total_level_width  = len(level[m_c][0])*32 # Высчитываем фактическую ширину уровня
    total_level_height = len(level[m_c])*32   # высоту
    
    camera = Camera(camera_configure, total_level_width, total_level_height) 



def main():
    global left_b,right_b,flag,shot,left,right,up,entities,platforms,bulets,level,hero,blocks,camera,m_c,bg_map,bg_map_e,ckn,reload
    pygame.init()
    screen=pygame.display.set_mode(DISPLAY)
    bg=Surface((WIN_WIDTH,WIN_HIGHT))
    #bg.fill(Color(BACKGROUND_COLOR))
    #hero=Player(100,55)
    flag=shot=left=right=up=False
    font = pygame.font.Font('open-sans.ttf', 25)
    with open("test.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
    level=[jsonObject['map1'],jsonObject['map2'],jsonObject['map3'],jsonObject['map4']]
    timer=pygame.time.Clock()
    
    map_new(0)
    while 1:
        timer.tick(60)
                 
        for e in pygame.event.get():

            if e.type == KEYDOWN and e.key==K_a:
                left=True
            if e.type == KEYDOWN and e.key==K_d:
                right=True
            if e.type == KEYDOWN and e.key==K_w:
                up=True
            if e.type == KEYDOWN and e.key==K_SPACE and flag==False:
                flag=True
                shot=True
            if e.type == KEYDOWN and e.key==K_r:
                reload=True

            if e.type == KEYUP and e.key==K_a:
                left=False
            if e.type == KEYUP and e.key==K_d:
                right=False
            if e.type == KEYUP and e.key==K_w:
                up=False
            if e.type == KEYUP and e.key==K_r:
                reload=False
            if e.type == KEYUP and e.key==K_SPACE and flag==True:
                flag=False
                shot=False
            if e.type==QUIT:
                raise SystemExit


        screen.blit(fon,(0,0))
        c_x=WIN_WIDTH
        
                          

        hero.update(left,right,up,shot,reload,platforms,blocks,entities,turels,ckn)
        for tr in turels:
            tr.update()
        if btn_prs>=6:
            for pl in platforms:
                if pl.img_n==19:
                    pl.rect.right-=20
                    pl.image=pygame.image.load('dor_open.png')
                    pl.col=False
                    pl.img_n=20
        shot=False
        
        camera.update(hero)
        for ck in ckn:
            ck.update()
        for e in entities:
            screen.blit(e.image, camera.apply(e))


        for i in range(len(ckn_c)):
            pf=ANIMATION_CKN[ckn_c[i]][3]
            screen.blit(pf,(c_x-32,32))
            c_x-=32
        hp_l=2*hero.hp
        pf= Surface((hp_l,20))
        pl= Surface((64,64))
       
        pl=pygame.image.load('pulya.png')
        text = font.render(str(hero.mgz)+"/15",True,"#e4cf45")
        screen.blit(pl,(85,WIN_HIGHT-62))
        screen.blit(text, [100,WIN_HIGHT-70])
        if hero.hp>0:
            if hero.hp>75:
                pl=pygame.image.load('heat_1.png')
                pf.fill(Color("#7FFF00"))
            elif hero.hp>50:
                pl=pygame.image.load('heat_2.png')
                pf.fill(Color("#c0d81f"))
            elif hero.hp>25:
                pl=pygame.image.load('heat_3.png')
                pf.fill(Color("#d8b71f"))
            elif hero.hp>0:
                pl=pygame.image.load('heat_4.png')
                pf.fill(Color("#d8461f"))
            screen.blit(pl,(5,WIN_HIGHT-70))
            screen.blit(pf,(70,WIN_HIGHT-30))


        pygame.display.update()

##################################player
class Player(sprite.Sprite):
    def __init__(self,x,y,a):
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
        self.tren=8        
        self.hp=100
        self.mgz=15
        self.a=a
        self.flag_r=False
        self.b=0

    def update(self,left,right,up,shot,reload,platforms,blocks,entities,turels,ckn):
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
            if self.lastdir=="right":
                self.image=ANIMATION_STAY
            if self.lastdir=="left":
                self.image=ANIMATION_STAY
                self.image = transform.flip(self.image, True, False)
        if not (left or right):
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
                
        if shot and self.mgz>0 and not  self.flag_r:
            if  self.lastdir=="left":
                bult=Bulet(self.rect.x-20,self.rect.y,32,self.lastdir)
            else:
                bult=Bulet(self.rect.x,self.rect.y,32,self.lastdir)
            self.mgz-=1
            bulets.append(bult)  
            entities.add(bult)
        if reload and self.mgz<15:
            self.flag_r=True
        if self.flag_r==True:
            self.b+=1
            if self.b%12==0 and self.mgz<15:
                self.mgz+=1
            if self.b>180 or  self.mgz>=15:
                self.b=0
                #self.mgz=15
                self.flag_r=False
        if not self.onGround:
            self.yvel+=GRAVITY
        if self.hp<=0:
            map_new(0)
            print("lox")
            self.yvel=0
            self.xvel=0
        self.onGround=False
        self.tren=0.03
        self.rect.y+=self.yvel
        self.collide(0,self.yvel,platforms,blocks,ckn,bulets,turels)

        self.rect.x += self.xvel
        self.collide(self.xvel,0,platforms,blocks,ckn,bulets,turels)
        for bu in bulets:
            bu.update(platforms,blocks,bulets,entities,turels)

    def collide(self,xvel,yvel,platforms,blocks,ckn,bulets,turels):
        global level,ckn_c
        for t in turels:
            if sprite.collide_rect(self,t):
                if xvel>0:
                    self.rect.right = t.rect.left
                    self.xvel=0

                if xvel<0:
                    self.rect.left = t.rect.right
                    self.xvel=0


                if yvel>0:
                    self.rect.bottom = t.rect.top
                    self.onGround = True
                    self.tren=8
                    self.yvel=0
                if yvel<0:
                    self.rect.top = t.rect.bottom 
                    self.yvel=0


        for p in platforms:
            if sprite.collide_rect(self,p):
                if p.col==True:
                    if xvel>0:
                        if p.img_n!=10 :
                            self.rect.right = p.rect.left
                            if p.img_n==18 :
                                self.xvel= -8
                            else:
                                self.xvel=0

                    if xvel<0:
                        if p.img_n!=10 :
                            self.rect.left = p.rect.right
                            if p.img_n==17 :
                                self.xvel=8
                            else:
                                self.xvel=0


                    if yvel>0:
                        if p.img_n==23:
                            self.hp=0
                        if p.img_n==22:
                            map_new(self.a)
                        if p.img_n!=10 :
                            self.rect.bottom = p.rect.top
                        if p.img_n==16 :
                            self.yvel=-11
                        else:
                            if p.img_n==10 :
                                self.onGround = True
                                self.tren=8
                            else:  
                                self.onGround = True
                                self.tren=8
                                self.yvel=0
                    if yvel<0:
                        if p.img_n!=10 :
                            self.rect.top = p.rect.bottom 
                            self.yvel=0
        left=False
        right=False
        MOVE_SPEED = 5
        for c in ckn:
            if sprite.collide_rect(self,c):
                c.kill(ckn)
                ckn_c.append(c.an_n)
        for b in bulets:
            if sprite.collide_rect(self,b):
                if self.hp>0:
                    self.hp-=b.dmg
                b.kill()
        for b in blocks:
            if self.rect.right>=len(level[self.a-1][0])*32:
                self.rect.right = len(level[self.a-1][0])*32-32
                self.xvel=0 
            elif self.rect.right<=0:
                self.rect.right = 0
                self.xvel=0 
            elif sprite.collide_rect(self,b):
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
                        self.tren=8
                        self.onGround = True
                        self.yvel=0 
                        b.yvel = self.yvel

                    if yvel<0:
                        self.rect.top = b.rect.bottom
                        self.yvel=0
                        b.yvel = self.yvel
            if yvel==0:
                 m_s=self.rect.x
                 b.right=left
                 b.left=right
                 b.update(m_s,left,right,platforms,blocks)


class Turel(sprite.Sprite):
    def __init__(self,x,y,dir):
        sprite.Sprite.__init__(self)   
        self.image = Surface((32,32))
        if dir=="right":
            self.image=pygame.image.load('turel.png')
        if dir=="left":
            self.image=pygame.image.load('turel.png')
            self.image = transform.flip(self.image, True, False)
        self.rect = Rect(x, y, 32,32)
        self.hp=64
        self.dir=dir
        print(dir)
        self.i=0
        self.shot=False

    def kill(self):
        global entities, turels
        for tr in turels:
            if tr == self:
                turels.pop(turels.index(tr))
        for e in entities:
            if e == self:
                entities.remove(e)


    def update(self):
        if self.hp<=0:
            self.kill()
        if self.i>=60:
            self.i=0
            self.shot=True
        if self.shot:
            if self.dir=="right":
                a=32
            if self.dir=="left":
                a=-20
            bult=Bulet(self.rect.x+a,self.rect.y-13,10,self.dir)
            bulets.append(bult)  
            entities.add(bult)
        self.shot=False 
        self.i+=1  
        



class Bulet(sprite.Sprite):
    def __init__(self,x,y,dmg,lastdir):
        sprite.Sprite.__init__(self)   
        self.xvel=20
        self.yvel=0
        self.startX=x+10
        self.startY=y-10
        self.dir=lastdir
        self.image = Surface((15,15))
        self.image= pygame.image.load("pul.png")
        if self.dir=='left':
            self.image = transform.flip(self.image, True, False)
            self.xvel= -self.xvel
        if self.dir=='right':
            self.xvel= self.xvel
       
        
        self.rect = Rect(x+10+self.xvel, y+20, 10, 10)
        self.dmg=dmg

    def kill(self):
        global entities, bulets
        for bl in bulets:
            if bl == self:
                bulets.pop(bulets.index(bl))
        for e in entities:
            if e == self:
                entities.remove(e)


    def update(self,platforms,blocks,bulets,entities,turels):
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
        self.collide(platforms,blocks,0,self.yvel,bulets,turels)
        self.yvel+=0.35
        self.rect.x += self.xvel
        self.collide(platforms,blocks,self.xvel,0,bulets,turels)



    def collide(self,platforms,blocks,xvel,yvel,bulets,turels):
        if self.yvel==0 and self.xvel==0:
            self.kill()
                        
        for p in platforms:
            if p.img_n!=10:
                if sprite.collide_rect(self,p):
                    if p.col==True:
                        if p.img_n==15:
                            p.kill()
                        self.kill()
                        self.yvel=0
                        self.xvel=0
        for b in blocks:
            if sprite.collide_rect(self,b):
                    self.kill()
                    self.xvel=0
                    self.yvel=0
        for t in turels:
            if sprite.collide_rect(self,t):
                self.kill()
                self.xvel=0
                self.yvel=0
                t.hp-=self.dmg

                
##############################block
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
         image.load('jump_bust.png'),                      #16
         image.load('jump_bust.png'),                      #17
         image.load('jump_bust.png'),                      #18
         image.load('dor_cl.png'),                          #19
         image.load('dor_open.png'),                        #20
         image.load('btn.png'),                              #21
         image.load('kam.png'),                               #22  
         image.load('ship.png'),                               #23        
         ]
class backgrn(sprite.Sprite):
    def __init__(self,x,y,width,hight,img_nam):
        sprite.Sprite.__init__(self)
        self.s_x=x
        self.s_y=y
        self.image=Surface((width,hight))
        self.image = image[img_nam]
        self.rect = Rect(self.s_x,self.s_y,width,hight) 
class Platform(sprite.Sprite):
    def __init__(self,x,y,width,hight,a,img_nam):
        
        sprite.Sprite.__init__(self)
        self.image=Surface((width,hight))
        self.s_x=x
        self.s_y=y
        if img_nam == 16 or img_nam == 17 or img_nam == 18:
            self.image = image[img_nam]
            if img_nam == 17:
                self.dir="right"
                self.image = pygame.transform.rotate(self.image, 270)
                self.rect = Rect(self.s_x,self.s_y,32,hight)
            elif img_nam == 18:
                self.dir="left"
                self.image = pygame.transform.rotate(self.image, 90)
                self.rect = Rect(self.s_x,self.s_y,32,hight)
            else:
                self.rect = Rect(self.s_x,self.s_y,32,hight)
        else:
            self.image = image[img_nam]
            self.rect = Rect(self.s_x,self.s_y,width,hight)
        self.col = a
        self.img_n=img_nam
        self.flag=False
        if img_nam==15:
            self.die=True
        else:
            self.die=False

    def kill(self):
        global entities, platforms
        if self.img_n==15:
            for p in platforms:
                if sprite.collide_rect(self,p) and p.img_n==15 and p!=self:
                    for e in entities:
                        if e == self:
                             entities.remove(e)
                    for bl in platforms:
                        if bl == self:
                            platforms.pop(platforms.index(bl)+1)
                    p.kill()
                for bl in platforms:
                        if bl == self:
                            platforms.pop(platforms.index(bl))
                for e in entities:
                        if e == self:
                             entities.remove(e)
        
class NPC(sprite.Sprite):
     def __init__(self,x,y,width,hight,tcbl,an_n):
        sprite.Sprite.__init__(self)
        self.s_x=x
        self.s_y=y
        self.image=Surface((width,hight))
        self.image = ANIMATION_CKN[an_n]
        self.rect = Rect(self.s_x,self.s_y,width,hight) 
        self.tcbl = tcbl
        self.animCount=0
        self.an_n=an_n
        self.animVel=1

     def update(self):
        if (self.animCount+1>=35 and self.animVel>0) or (self.animCount-1<=0and self.animVel<0):
            self.animVel =- self.animVel
        self.image=ANIMATION_CKN[self.an_n][self.animCount//5]
        self.animCount+=self.animVel

     def kill(self,ckn):
        global entities
        for ck in ckn:
            if ck == self:
                ckn.pop(ckn.index(ck))
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
        global btn_prs
        for t in turels:
            if sprite.collide_rect(self,t):
                if xvel>0:
                    self.rect.right = t.rect.left
                    self.xvel=0

                if xvel<0:
                    self.rect.left = t.rect.right
                    self.xvel=0


                if yvel>0:
                    self.rect.bottom = t.rect.top
                    self.onGround = True
                    self.tren=8
                    self.yvel=0
                if yvel<0:
                    self.rect.top = t.rect.bottom 
                    self.yvel=0
        for p in platforms:
            if sprite.collide_rect(self,p):
                if p.col==True and p.img_n!=23:
                    
                    if xvel>0:
                        self.rect.right = p.rect.left
                        self.right=False
                        if p.img_n==18 :
                            self.xvel=-8
                        else:
                            self.xvel=0
                    
                    if xvel<0:
                        
                        self.rect.left = p.rect.right
                        if p.img_n==17 :
                            self.xvel=8
                        else:
                            self.xvel=0
                        self.left=False

                    if yvel>0:
                        if p.img_n==18 :
                            self.xvel=-8
                        if p.img_n==17 :
                            self.xvel=8
                        self.rect.bottom = p.rect.top
                        if p.img_n==16 :
                            self.tren=0.1
                            self.yvel=-JUMP_POWER
                        elif p.img_n==21 and p.flag==False:
                            btn_prs+=1
                            p.flag=True
                            print(btn_prs)
                            self.tren=8
                            self.onGround = True
                            self.yvel=0
                        else:
                            self.tren=8
                            self.onGround = True
                            self.yvel=0

                    if yvel<0:
                        if p.img_n!=17 and p.img_n!=18:
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
                        self.tren=TREN
                        self.onGround = True
                        self.yvel=0

                    if yvel<0:
                        self.rect.top = b.rect.bottom  
                        self.yvel=0
                    b.right=left
                    b.left=right
                    b.update(0,left,right,platforms,blocks)



if __name__ == "__main__":
    main()