import pygame


class BUTTON:
    def __init__(self, img: pygame.surface, command, *args):
        self.img = img
        self.command = command
        self.args = args

    def click_do(self):
        if self.command:
            if self.args:
                self.command(*self.args)
            else:
                self.command()
