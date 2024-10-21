import example
import pygame


class CARGO_UNGRAVITY_APPROACHING(example.EXAMPLE):
    def __init__(self, pos: pygame.Vector2, velocity: pygame.Vector2):
        super(CARGO_UNGRAVITY_APPROACHING, self).__init__(pos, velocity, pygame.Color(120, 150, 120))

    def physics_processing(self, obj: example.EXAMPLE, influence: float) -> None:
        if (obj.pos-self.pos).length() == 0: return
        self.velocity += (obj.pos-self.pos).normalize() * influence/2 * 0.1
        if self.velocity.length() < 0.001: self.velocity *= 0
        self.velocity *= 0.9

    def magnetic(self, cargos: list) -> None:
        for cargo in cargos:
            length = (self.pos-cargo.pos).length()
            if length:
                self.velocity += (((cargo.pos-self.pos).normalize())/length**2)*1000

    def update_pos(self, time_scale: float) -> None:
        self.pos += self.velocity * time_scale

