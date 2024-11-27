import pygame
from random import randint
pygame.init
screen = pygame.display.set_mode((600,600))
screen.fill((255,255,255))
pygame.display.update()
cheetah=pygame.image.load("cheetah.jpg")
eagle=pygame.image.load("eagle.jpg")
horse=pygame.image.load("horse.jpg")
meerkat=pygame.image.load("meerkat.jpg")
cheetah=pygame.transform.scale(cheetah(75,75))
eagle=pygame.transform.scale(eagle(75,75))
horse=pygame.transform.scale(horse(75,75))
meerkat=pygame.transform.scale(meerkat(75,75))
screen.blit(cheetah,(150,100))
screen.blit(eagle,(150,200))
screen.blit(horse,(150,300))
screen.blit(meerkat,(150,400))
font
