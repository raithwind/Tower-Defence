import pygame
import random

pygame.init()

class Particle(pygame.sprite.Sprite):
    type = "particle"
    drag = 0.01
    def __init__(self,x,y,vx,vy,game):
        pygame.sprite.Sprite.__init__(self)
        self.width = 10
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
        if self.velx >1.5:
            self.velx *= 1-self.drag
            #print(f"x: {self.velx}")
        else:
            self.velx = 0
        if self.vely >1.5:
            self.vely *= 1-self.drag
            #print(f"y = {self.vely}")
        else:
            self.vely = 0