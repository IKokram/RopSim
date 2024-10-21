import example
import pygame


class PIN_DISTANCE(example.EXAMPLE):
    def __init__(self, pos: pygame.Vector2, velocity: pygame.Vector2):
        super(PIN_DISTANCE, self).__init__(pos, velocity, pygame.Color(80, 40, 150))

    def update_pos(self, time_scale: float) -> None:
        self.pos += self.velocity*time_scale

    def magnetic(self, cargos: list) -> None:
        for cargo in cargos:
            length = (self.pos-cargo.pos).length()
            if length:
                self.velocity -= (((cargo.pos-self.pos).normalize())/length**2)*1000
