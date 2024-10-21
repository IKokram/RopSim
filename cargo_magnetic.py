import pygame
import example


class CARGO_MAGNETIC(example.EXAMPLE):
    def __init__(self, pos: pygame.Vector2, velocity: pygame.Vector2) -> None:
        super(CARGO_MAGNETIC, self).__init__(pos, velocity, pygame.Color(120, 0, 0))

    def physics_processing(self, obj: example.EXAMPLE, influence: float) -> None:
        if (obj.pos-self.pos).length() == 0: return
        self.velocity += (obj.pos-self.pos).normalize() * influence/2 * 0.1
        if self.velocity.length() < 0.001: self.velocity *= 0
        self.velocity *= 0.9

    def gravity(self, gravity: pygame.Vector2) -> None:
        self.velocity += gravity

    def update_pos(self, time_scale: float) -> None:
        self.pos += self.velocity * time_scale

    def magnetic(self, cargos: list) -> None:
        for cargo in cargos:
            length = (self.pos-cargo.pos).length()
            if length:
                cargo.velocity -= (((cargo.pos-self.pos).normalize())/length**2)*1000
