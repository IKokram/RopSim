import example
import pygame


class PIN_MAGNETIC(example.EXAMPLE):
    def __init__(self, pos: pygame.Vector2, velocity: pygame.Vector2):
        super(PIN_MAGNETIC, self).__init__(pos, velocity, pygame.Color(0, 120, 255))

    def magnetic(self, cargos: list) -> None:
        for cargo in cargos:
            length = (self.pos-cargo.pos).length()
            if length:
                cargo.velocity -= (((cargo.pos-self.pos).normalize())/length**2)*1000
