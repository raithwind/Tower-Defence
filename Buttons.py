import pygame

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