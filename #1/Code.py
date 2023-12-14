import pygame, sys

pygame.init()

screen = pygame.display.set_mode((640,480))
screen = pygame.display.set_caption("MyGame")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
