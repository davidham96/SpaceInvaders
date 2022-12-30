import pygame
from config import width, height, padding
import sys
import random

class EnemyBullet:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.speed = 2
        self.width = 6
        self.height = 16
        self.delete = False

    def update(self):
        self.y += self.speed
        if self.y >= height-self.height:
            self.delete = True

    def draw(self, ctx):
        pygame.draw.rect(ctx,(0,255,17),(self.x,self.y,self.width,self.height))


class Enemies:
    def __init__(self, enemies_x, enemies_y):
        self.enemies_x = enemies_x
        self.enemies_y = enemies_y        
        self.enemies = []
        for y in range(enemies_y):
            for x in range(enemies_x):
                self.enemies.append(Enemy((padding + ((width-2*padding)/enemies_x)*0.5 + ((width-2*padding)/enemies_x) * x) - (50/2), padding + y*144))
        self.x = self.enemies[0].x
        self.y = self.enemies[0].y
        self.height = 144 * (enemies_y-1)+50
        self.width = (width-2*padding)/enemies_x*(enemies_x-1) + 50
        self.speed = [-0.5,25]
        self.bullet = None 

    def draw(self,ctx):
        # pygame.draw.rect(ctx,(0,200,200),(self.x,self.y,self.width,self.height))   
        for enemy in self.enemies:
            enemy.draw(ctx) 
        if self.bullet is not None:
            self.bullet.draw(ctx)
        

    def update(self):
        self.x += self.speed[0]
        if self.x <= 0 or self.x+self.width >= width:
            self.speed[0] *= -1
            self.y += self.speed[1]
        if self.y+self.height >= height:
            sys.exit()
        for enemy in self.enemies:
            if self.x <= 0 or self.x+self.width >= width:
                enemy.update(self.speed[0],self.speed[1])
            else: enemy.update(self.speed[0],0)
        self.shoot()
        if self.bullet is not None:
            self.bullet.update()
            if self.bullet.delete:
                self.bullet = None

    def shoot(self):
        if self.bullet is None:
            first_enemy = self.enemies_x*(self.enemies_y-1)
            last_enemy = first_enemy + (self.enemies_x-1)
            i = random.randint(first_enemy,last_enemy)
            enemy = self.enemies[i]
            self.bullet = EnemyBullet(enemy.x+(enemy.width/2),enemy.y+(enemy.height))
        

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shooting = False
        self.alive = True
        self.width = 50
        self.height = 50
        
    def draw(self,ctx):
        pygame.draw.rect(ctx,(90,70,100),(self.x,self.y,self.width,self.height))   

    def update(self, speed_x, speed_y):
        self.x += speed_x
        self.y += speed_y
