import pygame
import settings
from Buttons import *

class Menu:
    def __init__(self, game):
        self.game = game
        self.buttons = pygame.sprite.Group()


class Pause(Menu):
    def __init__(self, game):
        super().__init__(game)

        self.image = pygame.Surface((settings.WIDTH, 180),pygame.SRCALPHA)
        self.get_buttons()
        self.run()
    def get_buttons(self):
        self.buttons.add(ContinueButton("Continue", self.game, 10, 80, settings.BLUE))
        self.buttons.add(QuitButton("Quit", self.game, 200, 80, settings.GREEN))
    def run(self):
        self.game.gamestate["menu"] = True
        if "paused" in self.game.gamestate:
            self.game.mouseoffset = (0,0)
            self.game.buttons = self.buttons
            pygame.display.flip()
            self.image.fill((100,100,100,60))
            self.textsurface = self.game.font.render("Paused", False, (255, 255, 255))
            self.image.blit(self.textsurface, (0, 0))
            self.buttons.draw(self.image)
            self.game.camera.blit(self.image, self.game.mouseoffset)
            pygame.display.flip()


class Start(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.image = pygame.Surface((settings.WIDTH, settings.HEIGHT))
        self.display_offset = (0,0)
        self.buttons = pygame.sprite.Group()
        self.get_buttons()
        self.run()

    def get_buttons(self):
        self.buttons.add(StartButton("New Game", self.game, 40, 150, settings.BLUE))
        self.buttons.add(QuitButton("Quit", self.game, 40, 220, settings.BLUE))

    def run(self):
        self.game.mouseoffset = (0, 0)
        self.game.buttons = self.buttons
        self.image.fill(settings.WHITE)
        self.buttons.draw(self.image)
        self.game.camera.blit(self.image, (0,0))
        pygame.display.flip()

class Inventory(Menu):
    def __init__(self,game):
        super().__init__(self,game)
        pass