import pygame


GRAVITY = pygame.Vector2(0, 1)
FPS = 60
WIDTH = 800
HEIGHT = 600
widget_size = (50, 50)
toolbar_size = .15

# make surface for buttons
surfaces = []
mode_list = ["cargo", "pin", "rope", "spring", "circle", "move", "delete", "rope_delete", "cargo_delete", "auto_rope",
             "rope_line", "ungravity", "circle_rope_line", "rect_rope_line", "curve_rope_line", "circle_broken",
             "circle_repulsive", "circle_magnetic", "rect_delete", "rect_delete_rope", "rect_rope", "highlighting",
             "gravity_manipulation",
             "cargo_magnetic", "cargo_repulsive", "cargo_distance", "cargo_approaching",
             "cargo_ungravity_magnetic", "cargo_ungravity_repulsive", "cargo_ungravity_distance",
             "cargo_ungravity_approaching", "pin_magnetic", "pin_repulsive", "pin_distance", "pin_approaching",
             "rectangle", "glowrow"]


surf = pygame.surface.Surface(widget_size)
pygame.draw.circle(surf, (255, 0, 0), (25, 25), 10)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.circle(surf, (0, 0, 255), (25, 25), 10)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.line(surf, (0, 255, 0), (0, 0), (50, 50), 5)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.line(surf, (0, 0, 255), (0, 0), (50, 50), 5)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.circle(surf, (80, 80, 80), (25, 25), 10)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.polygon(surf, (255, 255, 255), ((10, 10), (10, 40), (20, 30), (30, 40), (40, 30), (30, 20), (40, 10)))
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.polygon(surf, (100, 100, 100), ((10, 10), (10, 15), (15, 15), (15, 40), (35, 40), (35, 15), (40, 15),
                                            (40, 10)))
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.polygon(surf, (100, 100, 100), ((10, 10), (10, 15), (15, 15), (15, 40), (35, 40), (35, 15), (40, 15),
                                            (40, 10)))
pygame.draw.line(surf, (0, 255, 0), (0, 0), (50, 50), 5)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.polygon(surf, (100, 100, 100), ((10, 10), (10, 15), (15, 15), (15, 40), (35, 40), (35, 15), (40, 15),
                                            (40, 10)))
pygame.draw.circle(surf, (255, 0, 0), (26, 30), 8)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.line(surf, (0, 255, 0), (10, 10), (40, 40), 5)
pygame.draw.circle(surf, (255, 0, 0), (10, 10), 5)
pygame.draw.circle(surf, (255, 0, 0), (40, 40), 5)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.lines(surf, (0, 255, 0), False, ((10, 10), (15, 20), (25, 30), (35, 20), (40, 10)), 4)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.circle(surf, (120, 255, 120), (25, 25), 10)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
poss = [(20, 10), (10, 20), (10, 30), (20, 40), (30, 40), (40, 30), (40, 20),
        (30, 10)]
pygame.draw.lines(surf, (0, 255, 0), True, poss, 5)
for i in poss:
    pygame.draw.circle(surf, (255, 0, 0), i, 4)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
poss = [(10, 10), (10, 40), (40, 40), (40, 10)]
pygame.draw.lines(surf, (0, 255, 0), True, poss, 5)
for i in poss:
    pygame.draw.circle(surf, (255, 0, 0), i, 4)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
poss = [(10, 10), (20, 30), (30, 20), (40, 40), (40, 10)]
pygame.draw.lines(surf, (0, 255, 0), True, poss, 5)
for i in poss:
    pygame.draw.circle(surf, (255, 0, 0), i, 4)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.circle(surf, (120, 120, 120), (25, 25), 10)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.circle(surf, (199, 133, 198), (25, 25), 10)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.circle(surf, (133, 157, 199), (25, 25), 10)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.polygon(surf, (100, 100, 100), ((10, 10), (10, 15), (15, 15), (15, 40), (35, 40), (35, 15), (40, 15),
                                            (40, 10)))
pygame.draw.rect(surf, (200, 200, 200), (18, 20, 15, 15), 5)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.polygon(surf, (100, 100, 100), ((10, 10), (10, 15), (15, 15), (15, 40), (35, 40), (35, 15), (40, 15),
                                            (40, 10)))
pygame.draw.rect(surf, (200, 200, 200), (18, 20, 15, 15), 5)
pygame.draw.line(surf, (0, 255, 0), (0, 0), (50, 50), 5)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
poss = [(10, 10), (10, 40), (40, 40), (40, 10)]
pygame.draw.lines(surf, (0, 255, 0), True, poss, 5)
pygame.draw.line(surf, (0, 255, 0), (0, 0), (50, 50), 5)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
poss = [(10, 10), (10, 40), (40, 40), (40, 10)]
pygame.draw.lines(surf, (0, 255, 0), True, poss, 5)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
poss = [(40, 10), (10, 10), (10, 40), (40, 40), (40, 25), (25, 25)]
pygame.draw.lines(surf, (0, 255, 0), False, poss, 5)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.circle(surf, (120, 0, 0), (25, 25), 10)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.circle(surf, (120, 120, 0), (25, 25), 10)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.circle(surf, (120, 0, 200), (25, 25), 10)
surfaces.append(surf.copy())

# start
surf = pygame.surface.Surface(widget_size)
pygame.draw.circle(surf, (120, 0, 100), (25, 25), 10)
surfaces.append(surf.copy())
# end

surf = pygame.surface.Surface(widget_size)
pygame.draw.circle(surf, (120, 255, 200), (25, 25), 10)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.circle(surf, (200, 255, 120), (25, 25), 10)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.circle(surf, (60, 255, 180), (25, 25), 10)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.circle(surf, (120, 150, 120), (25, 25), 10)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.circle(surf, (0, 120, 255), (25, 25), 10)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.circle(surf, (150, 120, 255), (25, 25), 10)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.circle(surf, (80, 40, 150), (25, 25), 10)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.circle(surf, (100, 100, 200), (25, 25), 10)
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.rect(surf, (80, 80, 80), (5, 5, 40, 40))
surfaces.append(surf.copy())

surf = pygame.surface.Surface(widget_size)
pygame.draw.line(surf, (190, 190, 190), (0, 0), (50, 50), 5)
surfaces.append(surf.copy())
