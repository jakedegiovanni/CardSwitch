from random import randint
import pygame, sys, time
import pyganim
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


# make some Surface objects for the animation frames:
surf1 = pygame.Surface((100, 100))

surf2 = pygame.Surface((100, 100))

surf3 = pygame.Surface((100, 100))

# create the PygAnimation object
animObj = pyganim.PygAnimation([(imagelist[0], 0.2), (imagelist[2], 0.2), (imagelist[3], 1.0)])
animObj.play()

while True: # main loop
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    animObj.blit(screen, (0, 0))
    pygame.display.update()

# while True:
# 	screen.blit(imagelist[i], (200,200))
# 	pygame.display.flip()
# 	c.tick(5)
# 	for event in pygame.event.get():
# 		if event.type == pygame.KEYDOWN:
# 			if event.key == pygame.K_ESCAPE:
# 				pygame.quit()
# 	i+=1
# 	if i == 52:
# 		pygame.quit()
#       break

		



	

