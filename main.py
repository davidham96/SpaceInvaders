import sys, pygame

pygame.init()
size = width, height = 2560, 1440
black = 0, 0, 0
screen = pygame.display.set_mode(size)

class Player:
    def __init__(self,x):
        self.x = x
        self.y = 1300
        self.shooting = False
        self.alive = True
        self.width = 50
        self.height = 50
        self.speed = 2

    def move(self, left):
        if left:
            self.x -= self.speed
        else:
            self.x += self.speed

    def update(self):
        pass

    def draw(self,ctx):
        pygame.draw.rect(ctx,(255,0,0),(self.x,self.y,width,height))   

player = Player(width/2)

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.move(True)
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.move(False)


    screen.fill(black)
    player.draw(screen)
    pygame.display.flip()
