import pygame, sys
import pygame.font

pygame.init()
w = 1000
h = 1000

size = (w, h)
screen = pygame.display.set_mode(size)

font = pygame.font.Font("fonts/PressStart2p.ttf", 26)

text = font.render("Hi", True, (255, 255, 255))
screen.blit(text,
        (320 - text.get_width() // 2, 240 - text.get_height() // 2))
pygame.display.flip()
