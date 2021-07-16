import pygame
import json


with open("test.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()


pygame.init()
map=jsonObject['map1']


win = pygame.display.set_mode((len(map[1])*32, len(map)*32))
pygame.display.set_caption("New Game!")


surf = win.convert_alpha()
surf.fill([0,0,0,0])



x = 10*32/2
y = 5*32/2
width = 32
height = 64
speed = 10

isJump = False
JumpCount = 0

left=False
right=False

animCount=0

smesh_x=-10*32/2
smesh_y=-1*32/2

walkRight=[
            pygame.image.load('pers1.png'),
            pygame.image.load('pers2.png'),
            pygame.image.load('pers3.png'),
            pygame.image.load('pers4.png'),
            pygame.image.load('pers5.png'),
            pygame.image.load('pers6.png')
         ]


image = [pygame.image.load('rfvtym.png').convert_alpha(),
         pygame.image.load('rfvtym2.png').convert_alpha()]
playerStand = pygame.image.load('pers1.png'),
bg=pygame.image.load('pygame_bg.jpg')
map_cord=[]



def map_drow():
    global map,map_cord,smesh_x,smesh_y
    y_m=0
    x_m=0
    map_cord=[]
    for i in range(len(map)):
        x_m=0
        for g in range(len(map[i])):
            
            if(map[i][g]=='-'):
                win.blit(image[1],(x_m+smesh_x,y_m+smesh_y))
                map_cord.append([x_m+smesh_x,y_m+smesh_y])
                pygame.draw.rect(surf, (0, 0, 0, 0), (x_m+smesh_x, y_m+smesh_y,32,32))
            elif(map[i][g]=='+'):
                pygame.draw.rect(win, (250,255,250), (x_m+smesh_x, y_m+smesh_y,32,32))
                map_cord.append([x_m+smesh_x,y_m+smesh_y])
                pygame.draw.rect(surf, (0, 0, 0, 0), (x_m+smesh_x, y_m+smesh_y,32,32))
            elif(map[i][g]==' '):
                win.blit(image[0],(x_m+smesh_x,y_m+smesh_y))
                pygame.draw.rect(surf, (0, 0, 0, 100), (x_m+smesh_x, y_m+smesh_y,32,32))
                
            x_m+=32
        y_m+=32
def colision_side(x,y):
    global map_cord,smesh_y,smesh_x
    print(smesh_y,smesh_x)
    for i in range(len(map_cord)):
        if x+32>=map_cord[i][0]and x<=map_cord[i][0]+32: 
            print(y)
            if y >=map_cord[i][1]-64 and y-32<=map_cord[i][1]:
                print(map_cord[i][1])
                return 1
    return 0


def colision(x,y):
    global map_cord,smesh_y

    for i in range(len(map_cord)):
        if x+32>=map_cord[i][0]and x<=map_cord[i][0]+32: 
            if y >=map_cord[i][1]-64 and y-32<=map_cord[i][1]:
                
                return 1
    return 0



def draw_window():
    global animCount,right,left
    win.blit(bg, (0,0))
    map_drow()
    win.blit(surf, (0,0))
    if animCount+1>=18:
        animCount=0
    if right:
        win.blit(walkRight[animCount//3], (x, y))
        animCount+=1
        right=False
    elif left:
        imger=walkRight[animCount//3]
        imger = pygame.transform.flip(imger, True, False)
        win.blit(imger, (x, y))
        animCount+=1
        left=False
        #win.blit(playerStand, (x, y))
    else:
        win.blit(walkRight[0], (x, y))

        
    pygame.display.update()

run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and colision(x-speed,y)==0:
        left=True
        right=False
        smesh_x += speed
    if keys[pygame.K_RIGHT] and colision(x+speed,y)==0:
        left=False
        right=True
        smesh_x -= speed
    if colision_side(x,y)==0:        
        smesh_y -= (JumpCount ** 2) / 2
        
        JumpCount -= 1
    '''if not isJump:
        if keys[pygame.K_UP] and colision(x,y,0)==0:
            isJump = True
    else:
        if JumpCount >= -10:
            if JumpCount < 0:
                y += (JumpCount ** 2) / 2    
            else:
                y -= (JumpCount ** 2) / 2
            JumpCount -= 1
        else:
            isJump = False
            JumpCount = 10    
    #if keys[pygame.K_DOWN] and y < 500 - height - 5 - 20:
    #    y += speed
'''
    draw_window()
    pygame.display.update()


pygame.quit()
