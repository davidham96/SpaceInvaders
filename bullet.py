import pygame

class Bullet:
    def __init__(self, x):
        self.x = x
        self.y = 1300
        self.speed = 6
        self.width = 6
        self.height = 16
        self.delete = False

    def update(self):
        self.y -= self.speed
        if self.y <= 0:
            self.delete = True

    def draw(self, ctx):
        pygame.draw.rect(ctx,(100,100,200),(self.x,self.y,self.width,self.height))

    def check_collision(self, enemy):
        if (self.x + self.width) >= enemy.x and self.x <= (enemy.x + enemy.width):
            if (self.y <= enemy.y + enemy.height) and (self.y + self.height >= enemy.y):
                return True
        return False
