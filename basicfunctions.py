import pygame, time, sys
from random import randint
import pyganim
pygame.init()
w = 1000
h = 1000

size = (w, h)
screen = pygame.display.set_mode(size)
c = pygame.time.Clock()

def main():
    imagelist = generateList()
    levelnum = 0
    score = 0

    while levelnum<10:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        level(levelnum, imagelist)
        levelnum += 1
        imagelist = generateList()
    #c.tick(60)


def level(num1, list1):
    time = 3-(0.25*num1)

    # create the PygAnimation object, selects the images to display.
    animObj = pyganim.PygAnimation([(list1[0], time), (list1[2], time), (list1[3], time)], loop=False)
    animObj.play()

    while animObj.isFinished() != True:
        animObj.blit(screen, (100,100))
        pygame.display.update()


    

def randomCard(list1):
    randnumber = randint(0, (len(list1)-1))
    selected = list1.pop(randnumber)
    
    return selected

    
def generateList():
    count = 1
    imagelist = []
    while count <= 52:
        imagelist.append(pygame.image.load("CardPics/"+str(count)+".png"))
        count+=1
    return imagelist



main()

