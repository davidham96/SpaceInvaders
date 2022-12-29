import sys, pygame
from config import *
import player

pygame.init()
screen = pygame.display.set_mode(size)

player = player.Player(width/2)

while True:
    
    player.update()
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()
 
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.move(True)
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.move(False)
    if keys[pygame.K_w] or keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        player.shoot()

    screen.fill(black)
    player.draw(screen)
    pygame.display.flip()
