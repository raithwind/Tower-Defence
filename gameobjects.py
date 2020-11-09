import pygame
import random

pygame.init()

class Particle(pygame.sprite.Sprite):

    type = "particle"
    drag = 0.05
    def __init__(self,x,y,vx,vy,game):
        """

        :param x: int x coord
        :param y: int y coord
        :param vx: int/float x velocity
        :param vy: int/float y velocity
        :param game: Game()
        """
        pygame.sprite.Sprite.__init__(self)
        self.width = 10
        self.game = game
        self.height = 10
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.velx = vx
        self.vely = vy
    
    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
        if abs(self.velx) >1.5:
            self.velx *= 1-self.drag
            #print(f"x: {self.velx}")
        else:
            self.velx = 0
        if abs(self.vely) >1.5:
            self.vely *= 1-self.drag
            #print(f"y = {self.vely}")
        else:
            self.vely = 0
        if self.velx == 0 and self.vely == 0:
            self.game.all_sprites.remove(self)
class Player(pygame.sprite.Sprite):
    drag = 0.1
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 10
        self.height = 10
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (0,0)
        self.velx = 0
        self.vely = 0
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.acc = 3
        self.maxvel = 5
        self.game = None

    def update(self):
        if self.up and abs(self.vely) < self.maxvel:
            self.vely -= self.acc
        if self.down and abs(self.vely) < self.maxvel:
            self.vely += self.acc
        if self.left and abs(self.velx) < self.maxvel:
            self.velx -= self.acc
        if self.right and abs(self.velx) < self.maxvel:
            self.velx += self.acc

        self.rect.x += self.velx
        self.rect.y += self.vely
        if abs(self.velx) <1.5:
            self.velx = 0
        else:
            self.velx *= 1-self.drag

        if abs(self.vely) < 1.5:
            self.vely = 0
        else:
            self.vely *= 1 - self.drag
    def spawn(self):
        self.game.all_sprites.add(Particle(self.rect.x, self.rect.y,3,3,self.game))

