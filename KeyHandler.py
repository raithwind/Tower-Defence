import pygame
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
                    self.game.player.up = True
                elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
                    self.game.player.left = True
                elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                    self.game.player.down = True
                elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
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
                    print(f"X value: {self.game.camhandler.x}, argument: {self.game.camhandler.get_pos()}")
                    self.game.player.spawn()
                else:
                    print(f"Mouse event: {event.button}")