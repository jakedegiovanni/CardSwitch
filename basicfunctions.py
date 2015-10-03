import pygame, time, sys, pyganim
from random import randint
import pyganim
pygame.init()
w = 1000
h = 1000

size = (w, h)
screen = pygame.display.set_mode(size)
c = pygame.time.Clock()
font = pygame.font.Font("fonts/PressStart2p.ttf", 26)


def main():
    menu()
    imagelist = generateList()
    levelnum = 1
    score = 0

    while levelnum<10:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        global correctlist
        correctlist = []

        level(levelnum, imagelist)
        levelnum += 1
        print correctlist
        time.sleep(10)
        imagelist = generateList()
    #c.tick(60)



def level(num1, list1):
    time = 3-(0.25*num1)

    count = 0
    while count < 10:
        # create the PygAnimation object, selects the images to display.
        animObj = pyganim.PygAnimation([(randomCard(list1), time)], loop=False)
        animObj.play()

        while animObj.isFinished() != True:
            animObj.blit(screen, (100,100))
            pygame.display.update()

        print count
      #  pygame.display.flip()
        c.tick(time)
        count += 1

def randomCard(list1):
    randnumber = randint(0, (len(list1)-1))
    selected = list1.pop(randnumber)
    print randnumber
    correctlist.append(randnumber)
    return selected


def generateList():
    count = 1
    imagelist = []
    while count <= 52:
        imagelist.append(pygame.image.load("Cards/"+str(count)+".gif"))
        count+=1
    return imagelist

def menu():
    pass


main()

