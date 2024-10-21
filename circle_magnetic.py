import pygame
from example import EXAMPLE
from circle_repulsive import CIRCLE_REPULSIVE


class CIRCLE_MAGNETIC(CIRCLE_REPULSIVE):
    def __init__(self, pos: pygame.Vector2, radius: float):
        super(CIRCLE_MAGNETIC, self).__init__(pos, radius)
        self.color = pygame.Color(133, 157, 199)

    def is_collision(self, pos: pygame.Vector2) -> pygame.Vector2:
        return (self.pos - pos).normalize() if (self.pos - pos).length() < self.radius + 5 else None
