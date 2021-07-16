import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("New Game!")
image = pygame.image.load('rfvtym.png').convert_alpha()
win.blit(image,(0,0))

map=["---------",
     "-+      -",
     "-+      -",
     "-+      -",
     "-+      -",
     "---------",
    ]

y=0
x=0
for i in range(len(map)):
    x=0
    y+=32
    for g in range(len(map[i])):
        x+=32
        if(map[i][g]=='-'):
            win.blit(image,(x,y))
        if(map[i][g]=='+'):
            pygame.draw.rect(win, (250,255,250), (x, y,32,32))
        
pygame.display.update()
while 1:
    continue

pygame.quit()