import pygame
from config import width, height, padding
import random

class EnemyBullet:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.speed = 6
        self.width = 6
        self.height = 16
        self.delete = False

    def update(self):
        self.y += self.speed
        if self.y >= height-self.height:
            self.delete = True

    def draw(self, ctx):
        pygame.draw.rect(ctx,(0,255,17),(self.x,self.y,self.width,self.height))

    def player_collision(self, player):
        if (self.x + self.width) >= player.x and self.x <= (player.x + player.width):
            if (self.y <= player.y + player.height) and (self.y + self.height >= player.y):
                return True
        return False

class Enemies:
    def __init__(self, enemies_x, enemies_y):
        self.enemies_x = enemies_x
        self.enemies_y = enemies_y        
        self.enemies = []
        for x in range(enemies_x):
            col = []
            for y in range(enemies_y):
                col.append(Enemy((padding + ((width-2*padding)/enemies_x)*0.5 + ((width-2*padding)/enemies_x) * x) - (50/2), padding + y*144))
            self.enemies.append(col)
        self.x = self.enemies[0][0].x
        self.y = self.enemies[0][0].y
        self.height = 144 * (enemies_y-1)+50
        self.width = (width-2*padding)/enemies_x*(enemies_x-1) + 50
        self.speed = [-0.5,25]
        self.bullets = []
        self.timer = 100

    def draw(self,ctx):
        # pygame.draw.rect(ctx,(0,200,200),(self.x,self.y,self.width,self.height))   
        for enemy_col in self.enemies:
            for enemy in enemy_col:
                enemy.draw(ctx) 
        for bullet in self.bullets:
            bullet.draw(ctx)
        

    def update(self):
        self.x += self.speed[0]
        if self.x <= 0 or self.x+self.width >= width:
            self.speed[0] *= -1
            self.y += self.speed[1]
        for enemy_col in self.enemies:
            for enemy in enemy_col:
                if self.x <= 0 or self.x+self.width >= width:
                    enemy.update(self.speed[0],self.speed[1])
                else: enemy.update(self.speed[0],0)
        self.timer -= 1
        if self.timer == 0:
            self.shoot()
            self.timer = 100
        for bullet in self.bullets:
            bullet.update()
            if bullet.delete:
                self.bullets.remove(bullet)

    def shoot(self):
        i = random.randint(0,len(self.enemies)-1)
        enemy = self.enemies[i][len(self.enemies[i])-1]
        self.bullets.append(EnemyBullet(enemy.x+(enemy.width/2),enemy.y+(enemy.height)))
        

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
