import pygame
import settings


class Button(pygame.sprite.Sprite):
    def __init__(self, text, game, x, y, color):
        super().__init__()
        self.text = text
        self.width = 150
        self.height = 50
        self.game = game
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        #self.rect.topleft = (x+offset[0], y+offset[1])
        self.rect.midleft = (x,y)
        self.textsurface = self.game.font.render(text, False, (0, 0, 0))
        self.image.blit(self.textsurface, (0, 0))

    def click(self):
        pass


class StartButton(Button):
    def __init__(self, text, game, x, y, color):
        super().__init__(text, game, x, y, color)
        

    def click(self):
        self.game.gamestate["playing"] = True
        self.game.gamestate["paused"] = False
        self.game.gamestate["menu"] = False

class ContinueButton(Button):
    def __init__(self, text, game, x, y, color):
        super().__init__(text, game, x, y, color)

    def click(self):
        self.game.gamestate["playing"] = True
        self.game.gamestate["paused"] = False
        self.game.gamestate["menu"] = False
        self.game.mouseoffset = (0, 0)


class QuitButton(Button):
    def __init__(self, text, game, x, y, color):
        super().__init__(text, game, x, y, color)

    def click(self):
        if not self.game.gamestate["playing"]:
            self.game.running = False
        else:
            """
            To do: Implement are you sure you wish to quit with a sprite box.
            """

            self.game.running = False


class Menu:
    def __init__(self, game):
        self.game = game
        self.buttons = pygame.sprite.Group()


class Pause(Menu):
    def __init__(self, game):
        super().__init__(game)

        self.image = pygame.Surface((420, 90))
        self.get_buttons()
        self.run()
    def get_buttons(self):
        self.buttons.add(ContinueButton("Continue", self.game, 10, 40, settings.BLUE))
        self.buttons.add(QuitButton("Quit", self.game, 200, 40, settings.GREEN))
    def run(self):
        self.game.gamestate["menu"] = True
        if "paused" in self.game.gamestate:
            self.game.mouseoffset = (170,200)

            self.game.buttons = self.buttons
            pygame.display.flip()
            self.image.fill(settings.WHITE)
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
        self.buttons.add(StartButton("New Game", self.game, 20, 150, settings.BLUE))
        self.buttons.add(QuitButton("Quit", self.game, 420, 159, settings.BLUE))

    def run(self):
        self.game.mouseoffset = (0, 0)
        self.game.buttons = self.buttons
        self.image.fill(settings.WHITE)
        self.buttons.draw(self.image)
        self.game.camera.blit(self.image, (0,0))
        pygame.display.flip()
