from gameobjects import *
import pygame
vect = pygame.math.Vector2



#pygame.init()
class KeyHandler:
    def __init__(self,game):
        pygame.key.set_repeat(100)
        self.game = game

    def get_events(self):
        for event in pygame.event.get():  # gets all the events which have occured till now and keeps tab of them.
            ## listening for the the X button at the top
            if event.type == pygame.QUIT:
                self.game.running = False
            #key down events
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    self.game.paused = not self.game.paused
                elif keys[pygame.K_w] or keys[pygame.K_UP]:
                    if not self.game.player.up:
                        self.game.player.up = True
                elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
                    if not self.game.player.left:
                        self.game.player.left = True
                elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                    if not self.game.player.down:
                        self.game.player.down = True
                elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                    if not self.game.player.right:
                        self.game.player.right = True

                else:
                    print(f"Keyboard event: {event.key}")
            #key up events
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_w, pygame.K_UP]:
                    self.game.player.up = False
                if event.key in [pygame.K_a, pygame.K_LEFT]:
                    self.game.player.left = False
                if event.key in [pygame.K_s, pygame.K_DOWN]:
                    self.game.player.down = False
                if event.key in [pygame.K_d, pygame.K_RIGHT]:
                    self.game.player.right = False
            #Mouse events
            if event.type == pygame.MOUSEMOTION:
                print(f"Mouse position: {event.pos}, buttons: {event.buttons}")
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    #print(f"X value: {self.game.camhandler.x}, argument: {self.game.camhandler.get_pos()}")
                    #print(f"### Target set to: {event.pos}")
                    #print(self.game.player.vel)
                    #self.game.player.spawn()
                    x,y = event.pos
                    x+=self.game.camhandler.x
                    y+=self.game.camhandler.y
                    pos = (x,y)
                    self.game.player.set_target(pos)
                elif event.button == 3:
                    x, y = event.pos
                    x += self.game.camhandler.x
                    y += self.game.camhandler.y
                    pos = (x, y)
                    if (vect(pos) - self.game.player.rect.center).length() < 200:
                        print((vect(pos) - self.game.player.rect.center).length())

                        self.game.all_sprites.add(Tower(self.game, pos))
                else:
                    print(f"Mouse event: {event.button}")