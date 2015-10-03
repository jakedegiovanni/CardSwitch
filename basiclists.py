from random import randint
import pygame, sys, time
pygame.init()
w = 640
h = 480
size=(w,h)
screen = pygame.display.set_mode(size)
c = pygame.time.Clock()
i = 0

count = 1
imagelist = []



while count <= 52:
	imagelist.append(pygame.image.load("CardPics/"+str(count)+".png"))
	count+=1
				  

while True:
	screen.blit(imagelist[i], (200,200))
	pygame.display.flip()
	c.tick(2)
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
	i+=1
	if i == 52:
		pygame.quit()
		



	

