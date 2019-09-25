import pygame
import time
import random
from pygame.locals import*
WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)
TEXTCOLOR = (  0,   0,  0)



pygame.init()
pygame.font.init()
font1 = pygame.font.SysFont('arial', 42)
pygame.font.Font.set_underline(font1, True)
thefont = pygame.font.SysFont('Comic Sans MS', 30)
ragefont = pygame.font.SysFont('rage', 50)

sur = pygame.display.set_mode((900,500))
sur.fill(WHITE)

mousecords = pygame.mouse.get_pos()
(x1,y1)= mousecords
circle1 = pygame.draw.circle(sur, BLUE, mousecords, 20,0)

direction = 'down'

x2 = random.randint(100,800)
y2 = random.randint(50,450)

pygame.display.set_caption('Tracking game')
clock = pygame.time.Clock()
score = 0
counter, timetext = 10, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)


def game_menu():
    intro = True
    sur.fill(WHITE)
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()   
                quit()
            if 426 < pygame.mouse.get_pos()[0] < 426+52 and 211 < pygame.mouse.get_pos()[1] < 211+31:
                global playbutton
                playbutton = thefont.render('Play', False, (0,200,0))
            else:
                playbutton = thefont.render('Play', False, (0,0,0))
            if 426 < pygame.mouse.get_pos()[0] < 426+52 and 277 < pygame.mouse.get_pos()[1] < 277+31:
                global quitbutton
                quitbutton = thefont.render('Quit', False, (200,0,0))
            else:
                quitbutton = thefont.render('Quit', False, (0,0,0,))
            if event.type == pygame.MOUSEBUTTONUP:
                if 426 < mousecords[0] < 426+52 and 211 < mousecords[1] < 211+31:
                    game_loop()
            if event.type == pygame.MOUSEBUTTONUP:
                if 426 < pygame.mouse.get_pos()[0] < 426+52 and 277 < pygame.mouse.get_pos()[1] < 277+31:
                    pygame.quit()
                    quit()

        menusurface = font1.render('Main Menu',False, (0,0,0))
        titlesurface = ragefont.render('Tracking Game', False, (0,0,0))
        playrect = pygame.Rect(426,211,52,31)
        quitrect = pygame.Rect(426,277, 52, 31)
    

        mousecords = pygame.mouse.get_pos()
        

        sur.blit(menusurface, (380,120))
        sur.blit(titlesurface, (320, 50))
        sur.blit(quitbutton, (425, 277))
        sur.blit(playbutton, (425, 200))
        
        pygame.display.update()

        
def game_loop():
    game = True
    x2 = random.randint(100,800)
    y2 = random.randint(50,450)

    clock = pygame.time.Clock()
    counter, timetext = 10, '10'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    score = 0
    while game:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.USEREVENT:
                    counter -= 1
                    timetext = str(counter).rjust(3) if counter > 0 else game_menu()
                if event.type == pygame.MOUSEMOTION:
                    sur.fill(WHITE)
                    mousecords = pygame.mouse.get_pos()
                    (x1,y1)= mousecords
                    circle1 = pygame.draw.circle(sur, BLUE, mousecords, 20,0)
                    crect1 = pygame.Rect(x1-20,y1-20,40,40)
                    circle2 = pygame.draw.circle(sur, RED, (x2,y2), 20, 0)
                    crect2 = pygame.Rect(x2-20,y2-20,40,40)
                    if  crect1.colliderect(crect2):
                        sur.fill(WHITE)
                        x2 = random.randint(100,800)
                        y2 = random.randint(50,450)
                        circle2 = pygame.draw.circle(sur, RED, (x2,y2), 20, 0)
                        crect2 = pygame.Rect(x1-20,y1-20,40,40) 
                        score = score + 1
    ##        if direction == 'right':
    ##            x2 += 5
    ##            if x2 == 700:
    ##                direction = 'down'
    ##        elif direction == 'down':
    ##            y2 += 5
    ##            if y2 == 450:
    ##                direction = 'left'
    ##        elif direction == 'left':
    ##            x2 -= 5
    ##            if x2 == 100:
    ##                direction = 'up'
    ##        elif direction == 'up':
    ##            y2 -= 5
    ##            if y2 == 50:
    ##                direction = 'right'
                scoretext = thefont.render('Score: ' + str(score), False, (0,0,0))
                sur.blit(scoretext, (50,50))
                timesurface = thefont.render('Time left: ' + timetext, False, (0,0,0))
                sur.blit(timesurface, (100,100))
                pygame.display.update()

game_menu()
pygame.quit()
quit()            


