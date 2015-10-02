from random import randint
import pygame, sys, time
pygame.init()
w = 640
h = 480
size=(w,h)
screen = pygame.display.set_mode(size)
c = pygame.time.Clock()
i = 0


imagelist = [pygame.image.load("HEARTS\heart2.gif"),
             pygame.image.load("HEARTS\heart3.gif"),
             pygame.image.load("HEARTS\heart4.gif"),
             pygame.image.load("HEARTS\heart5.gif")]

while True:
    screen.blit(imagelist[i], (200,0))
    pygame.display.flip()
    c.tick(2)
    i+=1
    if i == 4:
        i = 0
