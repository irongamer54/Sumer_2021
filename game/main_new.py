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



def main():
    pygame.init()
    screen=pygame.display.set_mode(DISPLAY)
    bg=Surface((WIN_WIDTH,WIN_HIGHT))
    bg.fill(Color(BACKGROUND_COLOR))

    hero=Player(100,55)
    left=right=up=False

    entities = pygame.sprite.Group()
    platforms=[]


    with open("test.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
    level=jsonObject['map1']

    timer=pygame.time.Clock()
    
    
    
    
    x=y=0
    for row in level:
        for col in row:
            if col=="-":
                pf=Platform(x,y,32,32,True,1)
                entities.add(pf)
                platforms.append(pf)
            if col=="+":
                pf=Platform(x,y,32,32,False,0)
                entities.add(pf)
                platforms.append(pf)
            if col=="e":
                pf=Platform(x,y,32,32,True,2)
                entities.add(pf)
                platforms.append(pf)
            if col=="r":
                pf=Platform(x,y,32,17,True,3)
                entities.add(pf)
                platforms.append(pf)
            x+=32
        y+=32
        x=0
    entities.add(hero)
    total_level_width  = len(level[0])*32 # Высчитываем фактическую ширину уровня
    total_level_height = len(level)*32   # высоту
    
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

            if e.type == KEYUP and e.key==K_LEFT:
                left=False
            if e.type == KEYUP and e.key==K_RIGHT:
                right=False
            if e.type == KEYUP and e.key==K_UP:
                up=False

            if e.type==QUIT:
                raise SystemExit
        screen.blit(bg,(0,0))
        hero.update(left,right,up,platforms)
        camera.update(hero)
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        pygame.display.update()


if __name__ == "__main__":
    main()