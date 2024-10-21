import pygame
import example


class CARGO(example.EXAMPLE):
    def __init__(self, pos: pygame.Vector2, velocity: pygame.Vector2) -> None:
        super(CARGO, self).__init__(pos, velocity, pygame.Color(255, 0, 0))

    def physics_processing(self, obj: example.EXAMPLE, influence: float) -> None:
        if (obj.pos-self.pos).length() == 0: return
        self.velocity += (obj.pos-self.pos).normalize() * (influence)

    def gravity(self, gravity: pygame.Vector2) -> None:
        self.velocity += gravity

    def update_pos(self, time_scale: float) -> None:
        self.pos += self.velocity * time_scale
        self.velocity *= 0.9
