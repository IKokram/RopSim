import pygame
from example import EXAMPLE


class CREATE_ROPE:
    def __init__(self):
        self.first_connect_object = None
        self.plural_connect_object = []

    def add_to_plural(self, obj: EXAMPLE):
        for i in self.plural_connect_object:
            if id(obj) == id(i):
                return
        obj.color = pygame.Color(120, 120, 120) + obj.dcolor
        self.plural_connect_object.append(obj)

    def connect_plural(self, obj: EXAMPLE):
        for ind, key in enumerate(self.plural_connect_object):
            if id(obj) == id(key):
                obj.reset_color()
                self.plural_connect_object.pop(ind)
                return
        return self.plural_connect_object

    def connect_object(self, obj: EXAMPLE):
        if self.plural_connect_object:
            return self.connect_plural(obj)
        if id(obj) == id(self.first_connect_object):
            if self.first_connect_object:
                self.first_connect_object.reset_color()
                self.first_connect_object = None
        elif obj and self.first_connect_object:
            self.first_connect_object.reset_color()
            c = self.first_connect_object
            self.first_connect_object = None
            return c, obj
        else:
            if obj:
                self.first_connect_object = obj
                obj.color += pygame.Color(120, 120, 120)
