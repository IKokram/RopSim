import pygame
import camera


class MOUSE_INTERFACE:
    def __init__(self, camera_world: camera.CAMERA):
        self.camera = camera_world

    def transform_mouse_to_global_cords(self) -> pygame.Vector2:
        return pygame.Vector2(pygame.mouse.get_pos()) / self.camera.zoom + self.camera.pos
