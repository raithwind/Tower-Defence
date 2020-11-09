import pygame
import random
import settings
from gameobjects import Particle


## initialize pygame
pygame.init()
pygame.mixer.init()
bg = pygame.image.load("view_topdown.png")
dts = bg.get_rect().size
bg = pygame.transform.scale(bg,(dts[0]*5,dts[1]*5))

class Menu:
    def __init__(self, game):
        self.game = game
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT),pygame.NOFRAME)
        self.clock = self.game.clock
        self.sprites = pygame.sprite.Group()
        self.screen.fill(settings.GREEN)

class Game:
    def __init__(self):
        self.screen = Camera().get_camera()
        self.world = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT),pygame.FULLSCREEN)
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
        while self.running:
            self.keyhandler.get_events()
            #1 Process input/events
            self.clock.tick(settings.FPS)     ## will make the loop run at the same speed all the time

            #2 Update
            self.all_sprites.update()

            #3 Draw/render
            self.screen.blit(bg, (0,0))
            self.all_sprites.draw(self.screen)
            pygame.display.update()
            ## Done after drawing everything to the screen
            pygame.display.flip()       
        pygame.quit()

class KeyHandler:
    def __init__(self,game):
        self.game = game
    def get_events(self):
        for event in pygame.event.get():  # gets all the events which have occured till now and keeps tab of them.
            ## listening for the the X button at the top
            # print(event)
            if event.type == pygame.QUIT:
                self.game.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.running = False
                if event.key == pygame.K_UP:
                    self.game.get_menu()

                else:
                    print(event.key)
            if event.type == pygame.KEYUP:
                pass
            if event.type == pygame.K_w:
                pass
            if event.type == pygame.K_a:
                pass
            if event.type == pygame.K_s:
                game.world -=
            if event.type == pygame.K_d:
                pass

            if event.type == pygame.MOUSEMOTION:
                print(f"Mouse position: {event.pos}, buttons: {event.buttons}")
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                print(event)

class Menu:
     def __init__(self):
         pass


class Camera:
    def __init__(self):
        self.camera = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT),pygame.FULLSCREEN)

    def get_camera(self):
        return self.camera