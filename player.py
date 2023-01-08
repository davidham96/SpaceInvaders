from config import width
import pygame
from bullet import Bullet

class Player:
    def __init__(self, x, game):
        self.x = x
        self.game = game
        self.y = 1300
        self.shooting = False
        self.width = 50
        self.height = 50
        self.speed = 2
        self.bullet = None

    def update(self): 
        if self.game.enemies.y + self.game.enemies.height >= self.y:
            self.game.gameover = True 
        if self.game.enemies.bullet is not None and (self.game.enemies.bullet.player_collision(self)):
            self.game.gameover = True
            self.game.enemies.bullet = None
        if self.bullet is not None:
            self.bullet.update()  
            for enemies_col in self.game.enemies.enemies:
                for enemy in enemies_col:
                    if (self.bullet.check_collision(enemy)):
                        enemies_col.remove(enemy)
                        self.game.score += 1                        
                        if not enemies_col:
                            self.game.enemies.enemies.remove(enemies_col)
                        self.bullet = None 
                        return
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
