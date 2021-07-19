#from bulets import Bulet
from blocks import *
import json
from player import *

WIN_WIDTH=800
WIN_HIGHT=640
DISPLAY = (WIN_WIDTH,WIN_HIGHT)
BACKGROUND_COLOR="#004400"


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


def main():
    global left_b,right_b
    pygame.init()
    screen=pygame.display.set_mode(DISPLAY)
    bg=Surface((WIN_WIDTH,WIN_HIGHT))
    bg.fill(Color(BACKGROUND_COLOR))

    #hero=Player(100,55)
    flag=shot=left=right=up=False

    entities = pygame.sprite.Group()
    platforms=[]
    blocks=[]
    bulets=[]
    with open("test.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
<<<<<<< HEAD
    level=[jsonObject['map1']]
=======
    level=[jsonObject['map1'],jsonObject['map1_bg']]
>>>>>>> 78b501e4f0d6dd0dd360b657ed45ab036c61ebae

    timer=pygame.time.Clock()
    
    
    
    
    x=y=0
    for i in range(len(level)):
        for row in level[i]:
            for col in row:
                #if col==" ":
                #   pf=Platform(x,y,32,32,False,0)
                #  entities.add(pf)
                # platforms.append(pf)
<<<<<<< HEAD
                if col=="p":
                    hero=Player(x,y)
                if col=="0":
                    pf=Platform(x,y,32,32,True,10)
                    entities.add(pf)
                    platforms.append(pf)
=======
>>>>>>> 78b501e4f0d6dd0dd360b657ed45ab036c61ebae
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
<<<<<<< HEAD
                    blocks.append(bl)
=======
                    platforms.append(bl)
>>>>>>> 78b501e4f0d6dd0dd360b657ed45ab036c61ebae
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
                if col=="!":
                    pf=Platform(x,y,32,32,True,14)
                    entities.add(pf)
                    platforms.append(pf)
                x+=32
            y+=32
            x=0
    entities.add(hero)
    total_level_width  = len(level[0][0])*32 # Высчитываем фактическую ширину уровня
    total_level_height = len(level[0])*32   # высоту
    
    camera = Camera(camera_configure, total_level_width, total_level_height) 
    while 1:
        timer.tick(60)
                 
        for e in pygame.event.get():

            if e.type == KEYDOWN and e.key==K_LEFT:
                left=True
            if e.type == KEYDOWN and e.key==K_RIGHT:
                right=True
            if e.type == KEYDOWN and e.key==K_UP:
                up=True
            if e.type == KEYDOWN and e.key==K_LSHIFT and flag==False:
                flag=True
                shot=True

            if e.type == KEYUP and e.key==K_LEFT:
                left=False
            if e.type == KEYUP and e.key==K_RIGHT:
                right=False
            if e.type == KEYUP and e.key==K_UP:
                up=False
            if e.type == KEYUP and e.key==K_LSHIFT and flag==True:
                flag=False
                shot=False
            if e.type==QUIT:
                raise SystemExit
        screen.blit(bg,(0,0))

        hero.update(left,right,up,shot,platforms,blocks,entities, 1)
        shot=False
        camera.update(hero)
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        pygame.display.update()


if __name__ == "__main__":
    main()