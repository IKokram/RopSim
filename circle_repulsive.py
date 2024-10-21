import pygame
from circle import CIRCLE
from example import EXAMPLE


class CIRCLE_REPULSIVE(CIRCLE):
    def __init__(self, pos: pygame.Vector2, radius: float):
        super(CIRCLE_REPULSIVE, self).__init__(pos, radius)
        self.color = pygame.Color(199, 133, 198)

    def handle_collision(self, cargo: EXAMPLE):
        directory = self.is_collision(cargo.pos)
        if directory:
            cargo.velocity += directory*2
