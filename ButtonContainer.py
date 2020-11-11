import pygame


class ButtonContainer:
    def __init__(self,buttons):
        self.width = 200
        self.height = len(self.buttons)*50
        self.buttons = buttons
        self.container = pygame.Surface([self.width, self.height])
    def form(self):

        for ind,but in enumerate(self.buttons):
            print(f"Button:{but} at index {ind}")