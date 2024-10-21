import pygame
import example


class ROPE:
    def __init__(self, length: float, connection1: example.EXAMPLE, connection2: example.EXAMPLE,
                 rigidity: float) -> None:
        self.color = pygame.Color(0, 255, 0)
        self.length = length
        self.connection1 = connection1
        self.connection2 = connection2
        self.rigidity = rigidity

    def physics_processing(self) -> None:
        length = (self.connection2.pos-self.connection1.pos).length()
        if length > self.length:
            self.connection1.physics_processing(self.connection2, self.rigidity*(length-self.length))
            self.connection2.physics_processing(self.connection1, self.rigidity*(length-self.length))
