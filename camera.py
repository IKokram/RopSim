import pygame


class CAMERA:
    def __init__(self):
        self.pos = pygame.Vector2(0, 0)
        self.zoom = 1

    def transform_global_to_pos(self, pos: pygame.Vector2) -> pygame.Vector2:
        return pos - self.pos

    def handle_keyboard(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.pos.x -= 15/self.zoom
        if keys[pygame.K_d]:
            self.pos.x += 15/self.zoom
        if keys[pygame.K_w]:
            self.pos.y -= 15/self.zoom
        if keys[pygame.K_s]:
            self.pos.y += 15/self.zoom
