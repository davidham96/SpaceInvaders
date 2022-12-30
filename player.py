from config import width
import pygame
from bullet import Bullet

class Player:
    def __init__(self, x):
        self.x = x
        self.y = 1300
        self.shooting = False
        self.alive = True
        self.width = 50
        self.height = 50
        self.speed = 2
        self.bullet = None

    def update(self):
        if self.bullet is not None:
            self.bullet.update()
            if self.bullet.delete:
                self.bullet = None

    def move(self, left):
        if left and self.x >= 0:
            self.x -= self.speed
        elif left == False and (self.x + self.width) <= width:
            self.x += self.speed

    def shoot(self):
        if self.bullet is None:
            self.bullet = Bullet(self.x + (self.width/2))

    def draw(self,ctx):
        pygame.draw.rect(ctx,(255,0,0),(self.x,self.y,self.width,self.height))   
        if self.bullet is not None:
            self.bullet.draw(ctx)

