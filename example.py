import pygame


class EXAMPLE:
    def __init__(self, pos: pygame.Vector2, velocity: pygame.Vector2, color: pygame.Color) -> None:
        self.color = color
        self.pos = pos
        self.velocity = velocity
        self.dcolor = color

    def reset_color(self):
        self.color = self.dcolor

    def physics_processing(self, obj, influence: float) -> None:
        pass

    def gravity(self, gravity: pygame.Vector2) -> None:
        pass

    def magnetic(self, cargos: list) -> None:
        pass

    def update_pos(self, time_scale: float) -> None:
        pass
