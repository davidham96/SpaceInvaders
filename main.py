import sys, pygame
from config import *
from game import Game

pygame.init()
screen = pygame.display.set_mode(size)

game = Game()


font = pygame.font.Font('freesansbold.ttf', 32)

while not game.gameover:

    game.update()
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        game.move(True)
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        game.move(False)
    if keys[pygame.K_w] or keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        game.shoot()

    text = font.render('Score: ' + str(game.score), True, (255,255,255))
    textRect = text.get_rect()
    textRect.topleft = (0,0)
    
    screen.fill(black)
    game.draw(screen)
    screen.blit(text, textRect)
    pygame.display.flip()
