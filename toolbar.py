import pygame

import button
from button import BUTTON
from config import widget_size


class TOOLBAR:
    def __init__(self):
        self.buttons = []
        self.scroll = 0
        self.last_ind_found = None

    def scroll_change(self, i) -> None:
        self.scroll += i
        self.scroll = max(0, min(self.scroll, len(self.buttons)-1))

    def get_button_pos_from_index(self, index: int) -> pygame.Vector2:
        lvl_btn = int(index/self.count_widget_on_lvl())
        count_btn = index % self.count_widget_on_lvl()
        return pygame.Vector2(count_btn*widget_size[0], lvl_btn*widget_size[1])

    @staticmethod
    def count_widget_on_lvl() -> int:
        return pygame.display.get_window_size()[0]//widget_size[1]

    @staticmethod
    def count_lvl_on_toolbox() -> int:
        return pygame.display.get_window_size()[1]//widget_size[0]

    def max_count_widget(self):
        return self.count_widget_on_lvl() * self.count_lvl_on_toolbox()

    @staticmethod
    def transform_to_local_pos(pos: pygame.Vector2) -> pygame.Vector2:
        return pygame.Vector2(pos[0]*widget_size[0], pos[1]*widget_size[1])

    @staticmethod
    def transform_to_toolbar_pos(pos: pygame) -> pygame.Vector2:
        return pygame.Vector2(pos.x // widget_size[0], pos.y // widget_size[1])

    def get_button_index_from_button(self, btn: BUTTON) -> int:
        for ind, key in enumerate(self.buttons):
            if id(ind) == id(btn):
                return key

    def get_index_button_from_pos(self, pos: pygame.Vector2) -> int:
        p = self.transform_to_toolbar_pos(pos)
        lvl = self.count_widget_on_lvl()
        return int(p.y * lvl + p.x) + self.scroll

    def get_button_from_pos(self, pos: pygame.Vector2) -> BUTTON:
        count = self.get_index_button_from_pos(pos)
        if count < len(self.buttons):
            self.last_ind_found = count
            return self.buttons[count]
