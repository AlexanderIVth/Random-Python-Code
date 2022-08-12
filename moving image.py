import random, sys, time, pygame
from pygame.locals import *

FPS = null
WINDOWWIDTH = null
WINDOWHEIGHT = null
BUTTONSIZE = null

WHITE        = (255, 255, 255)
BLACK        = (  0,   0,   0)
BRIGHTRED    = (255,   0,   0)
RED          = (155,   0,   0)
BRIGHTGREEN  = (  0, 255,   0)
GREEN        = (  0, 155,   0)
BRIGHTBLUE   = (  0,   0, 255)
BLUE         = (  0,   0, 155)
BRIGHTYELLOW = (255, 255,   0)
YELLOW       = (155, 155,   0)
DARKGRAY     = ( 40,  40,  40)

FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Ball')

XMARGIN = 10
YMARGIN = 10

#Frame by Frame animation
Frame0 = pygame.image.load("Image here.img")


def main():
    global FPSCLOCK, DISPLAYSURF, XMARGIN, YMARGIN, HHOG, DIRECTION , Frame0 

    pygame.init()

    direction = 'right'
    while True: # main game loop
        checkForQuit()
        clickedButton = None # button that was clicked (set to YELLOW, RED, GREEN, or BLUE)
        #Animate OBJECTRECT
        if direction == 'right': #move object right
            XMARGIN = XMARGIN + 5
            if XMARGIN == 480:
                direction = 'down'
        elif direction == 'down':  #move object down
            YMARGIN = YMARGIN + 5
            if YMARGIN == 480:
                direction = 'left'
        elif direction == 'left':  #move object left
            XMARGIN = XMARGIN - 5
            if XMARGIN == -30:
                direction = 'up'
        elif direction == 'up':  # move object up
            YMARGIN = YMARGIN - 5
            if YMARGIN == -10:
               direction = 'right'

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(Frame0, (XMARGIN,YMARGIN))
        pygame.display.update()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(Frame1, (XMARGIN,YMARGIN))
        pygame.display.update()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(Frame2, (XMARGIN,YMARGIN))
        pygame.display.update()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(Frame3, (XMARGIN,YMARGIN))
        pygame.display.update()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(Frame4, (XMARGIN,YMARGIN))
        pygame.display.update()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(Frame5, (XMARGIN,YMARGIN))
        pygame.display.update()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(Frame6, (XMARGIN,YMARGIN))
        pygame.display.update()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(Frame7, (XMARGIN,YMARGIN))
        pygame.display.update()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(Frame8, (XMARGIN,YMARGIN))
        pygame.display.update()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(Frame9, (XMARGIN,YMARGIN))
        pygame.display.update()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(Frame10, (XMARGIN,YMARGIN))
        pygame.display.update()
        FPSCLOCK.tick(FPS)



def terminate():  #ends game
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back


if __name__ == '__main__':
    main()
