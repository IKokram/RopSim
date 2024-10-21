import pygame
from circle import CIRCLE
import example


class CIRCLE_BROKEN(CIRCLE):
    def __init__(self, pos: pygame.Vector2, radius: float):
        super(CIRCLE_BROKEN, self).__init__(pos, radius)
        self.color = pygame.Color(120, 120, 120)

    def handle_collision(self, cargo: example.EXAMPLE):
        directory = self.is_collision(cargo.pos)
        if directory:
            directory *= -1
            cargo.velocity = directory * cargo.velocity.length() * 0.2
            cargo.pos = directory * (self.radius + 5) + self.pos
