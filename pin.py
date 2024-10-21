import pygame
import example


class PIN(example.EXAMPLE):
    def __init__(self, pos: pygame.Vector2, velocity: pygame.Vector2) -> None:
        super(PIN, self).__init__(pos, velocity, pygame.Color(0, 0, 255))
