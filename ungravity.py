from cargo import CARGO
import pygame


class UN_GRAVITY(CARGO):
    def __init__(self, pos: pygame.Vector2, velocity: pygame.Vector2):
        super(UN_GRAVITY, self).__init__(pos, velocity)
        self.color = pygame.Color(120, 255, 120)
        self.dcolor = pygame.Color(120, 255, 120)

    def gravity(self, gravity: float) -> None:
        self.velocity *= 0.9
