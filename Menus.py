import pygame
import settings


class Button(pygame.sprite.Sprite):
    def __init__(self, text, game, x, y, color):
        """
        Abstract Class, Do not call, instead call ContinueButton, QuitButton, NewGameButton, OptionsButton etc
        :param text:
        :param game:
        :param x:
        :param y:
        :param color:
        """
        super().__init__()
        self.text = text
        self.width = 150
        self.height = 50
        self.game = game
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.textsurface = self.game.font.render(text, False, (0, 0, 0))
        self.image.blit(self.textsurface, (0, 0))

    def click(self):
        pass

class StartButton(Button):
    def __init__(self, text, game, x,y,color):
        super().__init__(text,game,x,y,color)

    def click(self):
        self.game.playing = True
        self.game.paused = False

class ContinueButton(Button):
    def __init__(self,text,game,x,y,color):
        super().__init__(text,game,x,y,color)

    def click(self):
        self.game.paused = False

class QuitButton(Button):
    def __init__(self,text,game,x,y,color):
        super().__init__(text,game,x,y,color)

    def click(self):
        if not self.game.playing:
            self.game.running = False
        else:
            """
            To do: Implement are you sure you wish to quit with a sprite box.
            """

            self.game.running = False

class Menu:
    def __init__(self, game):
        """
        A base class for handling menus
        :param game: Game()
        """
        self.game = game
        self.buttons = pygame.sprite.Group()


#
# self.camera.blit(pauseimage,(0,0))
# pygame.display.flip()

class Pause(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.image = pygame.Surface((settings.WIDTH, settings.HEIGHT))
        self.get_buttons()
        self.run()

    def get_buttons(self):
        self.buttons.add(ContinueButton("Continue", self.game, 20, 150, settings.BLUE))
        self.buttons.add(QuitButton("Quit", self.game, 420, 150, settings.GREEN))

    def run(self):
        if self.game.paused and self.game.playing:
            self.game.buttons = self.buttons
            self.image.fill(settings.WHITE)
            self.buttons.draw(self.image)
            self.game.camera.blit(self.image, (0, 0))
            pygame.display.flip()

class Start(Menu):
    def __init__(self,game):
        super().__init__(game)
        self.image = pygame.Surface((settings.WIDTH, settings.HEIGHT))
        self.get_buttons()
        self.run()


    def get_buttons(self):
        self.buttons.add(StartButton("New Game", self.game,20,150,settings.BLUE))
        self.buttons.add(QuitButton("Quit",self.game, 420,159,settings.BLUE))

    def run(self):
        self.game.buttons = self.buttons
        self.image.fill(settings.WHITE)
        self.buttons.draw(self.image)
        self.game.camera.blit(self.image, (0, 0))
        pygame.display.flip()
