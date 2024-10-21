import rope
import example
import pygame


class SPRING(rope.ROPE):
    def __init__(self, length: float, connection1: example.EXAMPLE, connection2: example.EXAMPLE,
                 rigidity: float) -> None:
        super(SPRING, self).__init__(length, connection1, connection2, rigidity)
        self.color = pygame.Color(0, 0, 255)
        self.length = round(self.length, 1)

    def physics_processing(self) -> None:
        length = round((self.connection2.pos - self.connection1.pos).length(), 1)
        if (length - self.length) != 0:
            self.connection1.physics_processing(self.connection2, self.rigidity * (length - self.length))
            self.connection2.physics_processing(self.connection1, self.rigidity * (length - self.length))
