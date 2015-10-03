import pygame, time, sys, pyganim
from random import randint
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
    while levelnum < 10:
        global correctlist
        correctlist = []
        level(levelnum, imagelist)
        levelnum += 1
        print correctlist
        time.sleep(10)
        imagelist = generateList()
        
def level(num1, list1):
    time = num1*0.5
    count = 0
    while count < 10:
        screen.blit(randomCard(list1), (200,0))
        print count
        pygame.display.flip()
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

