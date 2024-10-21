import pygame
from circle import CIRCLE
import example
import camera


class RECTANGLE(CIRCLE):
    def __init__(self, pos_start: pygame.Vector2, pos_end: pygame.Vector2):
        super(RECTANGLE, self).__init__(pos_start, 0)

        rector = [[min(pos_start.x, pos_end.x), max(pos_start.x, pos_end.x)],
                  [min(pos_start.y, pos_end.y), max(pos_start.y, pos_end.y)]]
        self.pos_start = pygame.Vector2(rector[0][0], rector[1][0])
        self.pos_end = pygame.Vector2(rector[0][1], rector[1][1])
        self.center = (self.pos_end-self.pos_start)/ 2 + self.pos_start
        self.pos = self.center

    def get_rect_to_draw(self, camera: camera.CAMERA) -> pygame.Rect:
        if self.pos_start.y > self.pos_end.y:
            self.pos_start.y, self.pos_end.y = self.pos_end.y, self.pos_start.y

        if self.pos_start.x > self.pos_end.x:
            self.pos_start.x, self.pos_end.x = self.pos_end.x, self.pos_start.x

        rect = pygame.Rect((self.pos_start-camera.pos)*camera.zoom, (
                abs(self.pos_start.x - self.pos_end.x)*camera.zoom,
                abs(self.pos_start.y - self.pos_end.y)*camera.zoom)
            )

        return rect

    def set_new_pos(self, pos: pygame.Vector2):
        a = self.center - self.pos_start
        b = self.center - self.pos_end
        self.center = pos
        self.pos_end = self.center + b
        self.pos_start = self.center + a
        self.pos = self.center

    def is_collision(self, pos: pygame.Vector2, vel: pygame.Vector2):
        d = (pos - self.center)
        length = d.length() - 5
        direct = d.normalize()

        vec = length*direct
        normal = pygame.Vector2(0, 0)
        inside = False
        if abs(vec.x) <= abs(self.pos_start.x-self.center.x) and abs(vec.y) <= abs(self.pos_start.y-self.center.y):
            inside = True
            pref_pos = -vel + pos
            if min(self.pos_start.x, self.pos_end.x) >= pref_pos.x:
                normal += pygame.Vector2(-1, 0)
            elif max(self.pos_start.x, self.pos_end.x) <= pref_pos.x:
                normal += pygame.Vector2(1, 0)
            if min(self.pos_start.y, self.pos_end.y) >= pref_pos.y:
                normal += pygame.Vector2(0, -1)
            elif max(self.pos_start.y, self.pos_end.y) <= pref_pos.y:
                normal += pygame.Vector2(0, 1)

        return normal, inside

    def handle_collision(self, cargo: example.EXAMPLE) -> None:
        direction, col = self.is_collision(cargo.pos, cargo.velocity)
        if col:

            if direction.length() != 0:
                if direction.x != 0:
                    cargo.velocity.x *= -0.9
                if direction.y != 0:
                    cargo.velocity.y *= -0.9
            cargo.pos += cargo.velocity

            if self.pos_start.x+5 < cargo.pos.x < self.pos_end.x-5:
                if self.center.y - cargo.pos.y > 0:
                    cargo.pos.y = min(self.pos_start.y, self.pos_end.y)-5
                else:
                    cargo.pos.y = max(self.pos_start.y, self.pos_end.y)+5
            elif self.pos_start.y+5 < cargo.pos.y < self.pos_end.y-5:
                if self.center.x - cargo.pos.x > 0:
                    cargo.pos.x = min(self.pos_start.x, self.pos_end.x)-5
                else:
                    cargo.pos.x = max(self.pos_start.x, self.pos_end.x)+5
