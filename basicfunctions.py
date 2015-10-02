import pygame, time, sys
from random import randint
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
    while levelnum < 10:
        level(levelnum, imagelist)
        print levelnum
        levelnum += 1

def level(num1, list1):
    time = num1*0.5
    count = 0
    while count < 10:
        screen.blit(randomCard(list1), (0,0))
        pygame.display.flip()
        c.tick(time)
        count += 1

def randomCard(list):
    selected = list.pop(randint(0, (len(list) - 1)))
    return selected

def generateList():
    count = 1
    imagelist = []
    while count <= 52:
        imagelist.append(pygame.image.load("CardPics/"+str(count)+".png"))
        count+=1
    return imagelist



main()

