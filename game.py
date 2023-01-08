from config import *
import player
from enemy import Enemies

class Game:
    def __init__(self):
        self.enemies = Enemies(6,6) 
        self.player = player.Player(width/2, self)
        self.gameover = False
        self.score = 0

    def draw(self, ctx):        
        self.player.draw(ctx)
        self.enemies.draw(ctx)

    def update(self):
        self.player.update()
        self.enemies.update()

    def move(self, left):
        self.player.move(left)

    def shoot(self):
        self.player.shoot()
