import example
import pygame


class PIN_REPULSIVE(example.EXAMPLE):
    def __init__(self, pos: pygame.Vector2, velocity: pygame.Vector2):
        super(PIN_REPULSIVE, self).__init__(pos, velocity, pygame.Color(150, 120, 255))

    def magnetic(self, cargos: list) -> None:
        for cargo in cargos:
            length = (cargo.pos-self.pos).length()
            if length:
                cargo.velocity -= (((self.pos-cargo.pos).normalize())/length**2)*1000
