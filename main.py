import pygame, sys
black = 0,0,0,0
pygame.init()
screen = pygame.display.set_mode((320,240))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        screen.fill(black)