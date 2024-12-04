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
font=pygame.font.SysFont("Times New Roman",36)
text=font.render("eagle",True,(0,0,0))
text1=font.render("meerkat",True,(0,0,0))
text2=font.render("cheetah",True,(0,0,0))
text3=font.render("horse",True,(0,0,0))
screen.blit(text,(350,100))
screen.blit(text1,(350,200))
screen.blit(text2,(350,300))
screen.blit(text3,(350,400))
pygame.display.update()
r=randint(0,255)
g=randint(0,255)
b=randint(0,255)
clr=(r,g,b)
while 1:

    event=pygame.event.poll()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()
            exit(0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen,((clr)),(pos), 20, 0)
        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos()
        pygame.draw.line(screen,((clr)),(pos),(pos2),5)
        pygame.draw.circle(screen,((clr)),(pos2), 20, 0)
        pygame.display.update()            
