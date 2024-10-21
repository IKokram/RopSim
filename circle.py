import pygame

import example


class CIRCLE:
    def __init__(self, pos: pygame.Vector2, radius: float):
        self.radius = radius
        self.pos = pos
        self.color = pygame.Color(80, 80, 80)

    def is_collision(self, pos: pygame.Vector2) -> pygame.Vector2:
        return (pos - self.pos).normalize() if (self.pos - pos).length() < self.radius + 5 and (self.pos - pos).length() != 0 else None

    def handle_collision(self, cargo: example.EXAMPLE):
        direction = self.is_collision(cargo.pos)
        if direction:
            cargo.velocity = direction * cargo.velocity.length() * 0.9
            cargo.pos = direction * (self.radius + 5) + self.pos
