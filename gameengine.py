import pygame
import random
import settings
from gameobjects import Particle
from KeyHandler import *

## initialize pygame
pygame.init()
pygame.mixer.init()
bg = pygame.image.load("view_topdown.png")
dts = bg.get_rect().size
bg = pygame.transform.scale(bg,(dts[0]*5,dts[1]*5))
bg2 = pygame.transform.scale(bg,(dts[0]*5,dts[1]*5))
vect = pygame.math.Vector2

class Menu:
    def __init__(self, game):
        self.game = game

class Game:
    def __init__(self,player):
        self.camhandler = Camera()
        self.player = player
        self.camera = self.camhandler.get_camera()
        #self.world = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.bg = bg
        self.world = self.bg
        self.clock = pygame.time.Clock()     ## For syncing the FPS
        ## group all the sprites together for ease of update
        self.all_sprites = pygame.sprite.Group()


    ## Game loop
        
    def get_menu(self):
        ###TODO implement menu
        print("Implement Menu")
        return Menu()

    def run(self,keyhandler):
        self.keyhandler = keyhandler
        self.running = True
        self.paused = False
        while self.running:
            self.keyhandler.get_events()
            if not self.paused:
                #1 Process input/events
                self.clock.tick(settings.FPS)     ## will make the loop run at the same speed all the time
                #2 Update
                self.all_sprites.update()

                #3 Draw/render
                self.camera.fill(settings.BLACK)
                self.world.blit(bg2, (0, 0))
                self.all_sprites.draw(self.world)
                self.camera.blit(self.world,(0,0),self.camhandler.get_pos())
                self.camhandler.x = self.player.rect.x - settings.WIDTH/2
                self.camhandler.y = self.player.rect.y - settings.HEIGHT/2
                pygame.display.flip()
                ## Done after drawing everything to the screen
                #pygame.display.update()
            else:
                pauseimage = pygame.Surface((settings.WIDTH,settings.HEIGHT))
                pauseimage.fill(settings.WHITE)
                self.camera.blit(pauseimage,(0,0))
                pygame.display.flip()
        pygame.quit()



class Menu:
     def __init__(self):
         pass


class Camera:
    def __init__(self):
        self.camera = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))#,pygame.FULLSCREEN)
        pygame.display.set_caption("Tower Defense")

        self.x = 0
        self.y = 0

    def get_pos(self):
        return (self.x,self.y,settings.WIDTH,settings.HEIGHT)

    def get_camera(self):
        return self.camera