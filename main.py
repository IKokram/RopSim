import pygame
import math
import example
from rope import ROPE
from cargo import CARGO
from pin import PIN
from spring import SPRING
from circle import CIRCLE
from camera import CAMERA
from config import *
from mouse_interface import MOUSE_INTERFACE
from button import BUTTON
from toolbar import TOOLBAR
from create_rope import CREATE_ROPE
from example import EXAMPLE
from ungravity import UN_GRAVITY
from circle_broken import CIRCLE_BROKEN
from circle_repulsive import CIRCLE_REPULSIVE
from circle_magnetic import CIRCLE_MAGNETIC
from pin_magnetic import PIN_MAGNETIC
from pin_repulsive import PIN_REPULSIVE
from pin_distance import PIN_DISTANCE
from pin_approaching import PIN_APPROACHING
from cargo_ungravity_magnetic import CARGO_UNGRAVITY_MAGNETIC
from cargo_ungravity_repulsive import CARGO_UNGRAVITY_REPULSIVE
from cargo_ungravity_distance import CARGO_UNGRAVITY_DISTANCE
from cargo_ungravity_approaching import CARGO_UNGRAVITY_APPROACHING
from cargo_magnetic import CARGO_MAGNETIC
from cargo_repulsive import CARGO_REPULSIVE
from cargo_distance import CARGO_DISTANCE
from cargo_approaching import CARGO_APPROACHING
from rectangle import RECTANGLE
from glowrow import GLOWROW
import time

pygame.init()

# lists of objects
cargos = []
ropes = []
circles = []

# toolbar
toolbar = TOOLBAR()

# display
display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

# clock
clock = pygame.time.Clock()

# camera
camera = CAMERA()


# function
def make_glowrow(con1: example.EXAMPLE, con2: example.EXAMPLE) -> None:
    ropes.append(GLOWROW((con1.pos - con2.pos).length(), con1, con2, 1))

def make_any_cargo(obj, *args) -> None:
    cargos.append(obj(*args, pygame.Vector2(0, 0)))


def make_any_rope(obj, *args) -> None:
    ropes.append(obj(*args, 1))


def make_ungravity(pos: pygame.Vector2):
    cargos.append(UN_GRAVITY(pos, pygame.Vector2(0, 0)))


def make_circle(pos: pygame.Vector2, radius: float) -> None:
    circles.append(CIRCLE(pos, radius))


def make_circle_broken(pos: pygame.Vector2, radius: float) -> None:
    circles.append(CIRCLE_BROKEN(pos, radius))


def make_cargo(pos: pygame.Vector2) -> None:
    cargos.append(CARGO(pos, pygame.Vector2(0, 0)))


def make_rope(con1: example.EXAMPLE, con2: example.EXAMPLE) -> None:
    ropes.append(ROPE((con1.pos - con2.pos).length(), con1, con2, 1))


def make_pin(pos: pygame.Vector2) -> None:
    cargos.append(PIN(pos, pygame.Vector2(0, 0)))


def make_spring(con1: example.EXAMPLE, con2: example.EXAMPLE):
    ropes.append(SPRING((con1.pos - con2.pos).length(), con1, con2, 1))


def change_to(mode: str) -> None:
    global type_used_block
    type_used_block = mode


def get_click_cargo(pos: pygame.Vector2) -> example.EXAMPLE:
    for i in cargos:
        if (pos - pygame.Vector2(i.pos)).length() * camera.zoom < 5 * camera.zoom:
            return i


def get_click_circles(pos: pygame.Vector2) -> CIRCLE:
    for i in circles:
        if type(i) == RECTANGLE:
            if i.is_collision(mouse_interface.transform_mouse_to_global_cords(), pygame.Vector2(0, 0))[1]:
                return i
        if (pos - pygame.Vector2(i.pos)).length() * camera.zoom < i.radius * camera.zoom:
            return i


def reset() -> None:
    global cargos, ropes, circles, rope_creator, pos_for_curve, pos_last_click, moved_list
    pos_for_curve = []
    cargos = []
    ropes = []
    moved_list = []
    circles = []
    rope_creator.plural_connect_object = []
    pos_last_click = None
    rope_creator.first_connect_object = None


def find_rope_with_objs(obj1: EXAMPLE, obj2: EXAMPLE):
    for ind, key in enumerate(ropes):
        if (key.connection1 == obj1 and key.connection2 == obj2) or (
                key.connection1 == obj2 and key.connection2 == obj1):
            return ind, rope


def find_obj_from_pos(pos: pygame.Vector2) -> tuple:
    for i in range(len(cargos)):
        if (pos - pygame.Vector2(cargos[i].pos)).length() * camera.zoom < 5 * camera.zoom:
            return i, CARGO

    for i in range(len(circles)):
        if type(circles[i]) == CIRCLE:
            if (pos - pygame.Vector2(circles[i].pos)).length() * camera.zoom < circles[i].radius * camera.zoom:
                return i, CIRCLE
        elif type(circles[i]) == RECTANGLE:
            if (circles[i].pos_start.x * camera.zoom <= pos.x * camera.zoom <= circles[i].pos_end.x * camera.zoom) and\
                (circles[i].pos_start.y * camera.zoom <= pos.y * camera.zoom <= circles[i].pos_end.y * camera.zoom):
                return i, CIRCLE


def delete_rope_connection(obj: example.EXAMPLE) -> None:
    deles = []
    for ind, key in enumerate(ropes):
        if id(key.connection1) == id(obj) or id(key.connection2) == id(obj):
            deles.append(ind)

    for ind, key in enumerate(deles):
        ropes.pop(key - ind)


def delete_object(pos: pygame.Vector2) -> None:
    global rope_creator
    date = find_obj_from_pos(pos)
    if not date: return
    if date[1] == CIRCLE:
        circles.pop(date[0])
    else:
        delete_rope_connection(cargos[date[0]])
        cargos.pop(date[0])


def set_last_used_rope_or_cargo() -> None:
    global type_used_block, last_cargo, last_rope
    match type_used_block:
        case "cargo":
            last_cargo = CARGO
        case "cargo_ungravity_magnetic":
            last_cargo = CARGO_UNGRAVITY_MAGNETIC
        case "cargo_ungravity_repulsive":
            last_cargo = CARGO_UNGRAVITY_REPULSIVE
        case "cargo_ungravity_distance":
            last_cargo = CARGO_UNGRAVITY_DISTANCE
        case "cargo_ungravity_approaching":
            last_cargo = CARGO_UNGRAVITY_APPROACHING
        case "pin_magnetic":
            last_cargo = PIN_MAGNETIC
        case "pin_repulsive":
            last_cargo = PIN_REPULSIVE
        case "pin_distance":
            last_cargo = PIN_DISTANCE
        case "pin_approaching":
            last_cargo = PIN_APPROACHING
        case "pin":
            last_cargo = PIN
        case "ungravity":
            last_cargo = UN_GRAVITY
        case "cargo_magnetic":
            last_cargo = CARGO_MAGNETIC
        case "cargo_repulsive":
            last_cargo = CARGO_REPULSIVE
        case "cargo_distance":
            last_cargo = CARGO_DISTANCE
        case "cargo_approaching":
            last_cargo = CARGO_APPROACHING
        case "rope":
            last_rope = ROPE
        case "glowrow":
            last_rope = GLOWROW
        case "spring":
            last_rope = SPRING

def make_rope_line(pos1: pygame.Vector2, pos2: pygame.Vector2) -> None:
    vec = pos2-pos1
    if vec.length() == 0: return
    norm = vec.normalize()
    count = max(int(vec.length())//100, 2)
    length = vec.length()//count

    for i in range(count+1):
        make_any_cargo(last_cargo, norm*i*length+pos1)
        r = rope_creator.connect_object(cargos[-1])
        if r:
            make_any_rope(last_rope, (r[0].pos-r[1].pos).length(), *r)
            rope_creator.connect_object(cargos[-1])


def connect_cargo_rope(mas: list, rope_type) -> None:
    for i in range(len(mas)):
        for j in range(i):
            if i == j: continue
            make_any_rope(rope_type, (mas[+ i].pos - mas[j].pos).length(), mas[i], mas[j])


def make_circle_rope_line(pos: pygame.Vector2, radius: float) -> None:
    alpha = 0
    step = math.pi * 2 / max(radius//100, 8)
    c = 0
    while alpha < math.pi * 2:
        c += 1
        s_x = round(pos.x + math.cos(alpha) * radius)
        s_y = round(pos.y + math.sin(alpha) * radius)
        make_any_cargo(last_cargo, pygame.Vector2(s_x, s_y))
        alpha += step

    start_count = len(cargos)-c

    connect_cargo_rope([cargos[i+start_count] for i in range(c)], last_rope)

def make_rect_rope_line(pos1: pygame.Vector2, pos2: pygame.Vector2):
    make_any_cargo(last_cargo, pos1)
    make_any_cargo(last_cargo, pos2)
    make_any_cargo(last_cargo, pygame.Vector2(pos1.x, pos2.y))
    make_any_cargo(last_cargo, pygame.Vector2(pos2.x, pos1.y))
    connect_cargo_rope([cargos[len(cargos)-4+i] for i in range(4)], last_rope)


def make_curve_rope_line(list_pos: list):
    start_pos = len(cargos)
    for pos in list_pos:
        make_any_cargo(last_cargo, pos)

    connect_cargo_rope([cargos[i+start_pos] for i in range(len(list_pos))], last_rope)


def make_circle_repulsive(pos: pygame.Vector2, radius: float) -> None:
    circles.append(CIRCLE_REPULSIVE(pos, radius))


def make_circle_magnetic(pos: pygame.Vector2, radius: float) -> None:
    circles.append(CIRCLE_MAGNETIC(pos, radius))


def make_rectangle(pos_start: pygame.Vector2, pos_end: pygame.Vector2):
    circles.append(RECTANGLE(pos_start, pos_end))


def get_all_object_in_rect(pos1, pos2):
    xmi, xma = min(pos1.x, pos2.x), max(pos1.x, pos2.x)
    ymi, yma = min(pos1.y, pos2.y), max(pos1.y, pos2.y)
    buf = []
    for i in cargos+circles:
        if xmi <= i.pos.x <= xma and ymi <= i.pos.y <= yma:
            buf.append(i)

    return buf


def get_all_cargo_in_rect(pos1, pos2):
    xmi, xma = min(pos1.x, pos2.x), max(pos1.x, pos2.x)
    ymi, yma = min(pos1.y, pos2.y), max(pos1.y, pos2.y)
    buf = []
    for i in cargos:
        if xmi <= i.pos.x <= xma and ymi <= i.pos.y <= yma:
            buf.append(i)

    return buf


def find_obj(obj) -> tuple:
    for i in range(len(cargos)):
        if id(obj) == id(cargos[i]):
            return i, CARGO

    for i in range(len(circles)):
        if id(obj) == id(circles[i]):
            return i, CIRCLE


def is_cargo_type(obj: type) -> bool:
    return obj == CARGO or obj == PIN or obj == UN_GRAVITY or obj == PIN_APPROACHING or\
           obj == CARGO_MAGNETIC or obj == CARGO_REPULSIVE or obj == CARGO_DISTANCE or\
           obj == CARGO_APPROACHING or obj == CARGO_UNGRAVITY_MAGNETIC or obj == CARGO_UNGRAVITY_REPULSIVE or\
           obj == CARGO_UNGRAVITY_DISTANCE or obj == CARGO_UNGRAVITY_APPROACHING or obj == PIN_MAGNETIC or\
           obj == PIN_REPULSIVE or obj == PIN_DISTANCE


# mouse interface
mouse_interface = MOUSE_INTERFACE(camera)

# rope creator
rope_creator = CREATE_ROPE()

# variable
moved = pygame.Vector2()
pos_for_curve = []
moved_list = []
time_scale = 1
time_stop = False
type_used_block = "move"
previous_pos_moved = None
pos_last_click = pygame.Vector2()
last_rope = None
last_cargo = None
gravity_scale = 1
gradient_detector = [(100, 100, 100), (0, 255, 0), (200, 255, 0), (200, 200, 0), (255, 120, 0), (255, 0, 0)]
# make button for toolbar
for i in range(len(mode_list)):
    b = BUTTON(surfaces[i % len(surfaces)], change_to, mode_list[i])
    toolbar.buttons.append(b)


last_time = time.time()
# main loop
while True:
    delta = time.time() - last_time
    last_time = time.time()
    window_size = pygame.display.get_window_size()
    mouse_pos_as_toolbar = window_size[1] - window_size[1] * toolbar_size

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                time_stop = not time_stop
            if event.key == pygame.K_m:
                GRAVITY = pygame.Vector2(0, 1)
            if event.key == pygame.K_o:
                time_scale = max(0, time_scale-1)
            if event.key == pygame.K_p:
                time_scale = min(5, time_scale+1)
            if event.key == pygame.K_k:
                gravity_scale = max(0, gravity_scale-1)
            if event.key == pygame.K_l:
                gravity_scale = min(5, gravity_scale+1)
            if event.key == pygame.K_f and pos_for_curve:
                make_curve_rope_line(pos_for_curve)
                pos_for_curve = []
            if event.key == pygame.K_v:
                moved_list = []
            if event.key == pygame.K_q and rope_creator.first_connect_object:
                rope_creator.first_connect_object.reset_color()
                rope_creator.first_connect_object = None
            if event.key == pygame.K_q and rope_creator.plural_connect_object:
                [i.reset_color() for i in rope_creator.plural_connect_object]
                rope_creator.plural_connect_object = []
            if event.key == pygame.K_e and rope_creator.plural_connect_object and (last_rope or
                    (type_used_block == "rope" or type_used_block == "spring")):
                if type_used_block == "rope":
                    connect_cargo_rope(rope_creator.plural_connect_object, ROPE)
                elif type_used_block == "spring":
                    connect_cargo_rope(rope_creator.plural_connect_object, SPRING)
                elif type_used_block == "glowrow":
                    connect_cargo_rope(rope_creator.plural_connect_object, GLOWROW)
                else:
                    connect_cargo_rope(rope_creator.plural_connect_object, last_rope)

                [i.reset_color() for i in rope_creator.plural_connect_object]
                rope_creator.plural_connect_object = []

            if event.key == pygame.K_r:
                reset()

        if event.type == pygame.MOUSEBUTTONDOWN and (event.button != 4 and event.button != 5):
            if pygame.mouse.get_pos()[1] >= mouse_pos_as_toolbar:
                m = pygame.Vector2(pygame.mouse.get_pos()) - pygame.Vector2(0, mouse_pos_as_toolbar)
                now_button = toolbar.get_index_button_from_pos(m)
                if now_button == toolbar.last_ind_found:
                    toolbar.last_ind_found = None
                    type_used_block = None
                else:
                    b = toolbar.get_button_from_pos(m)
                    if b:
                        arg = b.args[0]
                        if "delete" in arg:
                            if rope_creator.first_connect_object:
                                rope_creator.first_connect_object.reset_color()
                            if rope_creator.plural_connect_object:
                                [i.reset_color() for i in rope_creator.plural_connect_object]
                            moved_list = []
                            rope_creator.plural_connect_object = []
                            rope_creator.first_connect_object = None
                        pos_for_curve = []
                        set_last_used_rope_or_cargo()
                        b.click_do()

            else:
                match type_used_block:
                    case "cargo":
                        make_cargo(mouse_interface.transform_mouse_to_global_cords())
                    case "pin":
                        make_pin(mouse_interface.transform_mouse_to_global_cords())
                    case "pin_magnetic":
                        make_any_cargo(PIN_MAGNETIC, mouse_interface.transform_mouse_to_global_cords())
                    case "pin_repulsive":
                        make_any_cargo(PIN_REPULSIVE, mouse_interface.transform_mouse_to_global_cords())
                    case "pin_distance":
                        make_any_cargo(PIN_DISTANCE, mouse_interface.transform_mouse_to_global_cords())
                    case "pin_approaching":
                        make_any_cargo(PIN_APPROACHING, mouse_interface.transform_mouse_to_global_cords())
                    case "cargo_ungravity_magnetic":
                        make_any_cargo(CARGO_UNGRAVITY_MAGNETIC, mouse_interface.transform_mouse_to_global_cords())
                    case "cargo_ungravity_repulsive":
                        make_any_cargo(CARGO_UNGRAVITY_REPULSIVE, mouse_interface.transform_mouse_to_global_cords())
                    case "cargo_ungravity_distance":
                        make_any_cargo(CARGO_UNGRAVITY_DISTANCE, mouse_interface.transform_mouse_to_global_cords())
                    case "cargo_ungravity_approaching":
                        make_any_cargo(CARGO_UNGRAVITY_APPROACHING, mouse_interface.transform_mouse_to_global_cords())
                    case "cargo_magnetic":
                        make_any_cargo(CARGO_MAGNETIC, mouse_interface.transform_mouse_to_global_cords())
                    case "cargo_repulsive":
                        make_any_cargo(CARGO_REPULSIVE, mouse_interface.transform_mouse_to_global_cords())
                    case "cargo_distance":
                        make_any_cargo(CARGO_DISTANCE, mouse_interface.transform_mouse_to_global_cords())
                    case "cargo_approaching":
                        make_any_cargo(CARGO_APPROACHING, mouse_interface.transform_mouse_to_global_cords())
                    case "rope":
                        con1 = get_click_cargo(mouse_interface.transform_mouse_to_global_cords())
                        resul = rope_creator.connect_object(con1)
                        if resul and con1:
                            if rope_creator.plural_connect_object:
                                for i in resul:
                                    if i:
                                        make_rope(con1, i)
                                        i.reset_color()
                                rope_creator.plural_connect_object = []
                            else:
                                make_rope(*resul)
                    case "spring":
                        con1 = get_click_cargo(mouse_interface.transform_mouse_to_global_cords())
                        resul = rope_creator.connect_object(con1)
                        if resul and con1:
                            if rope_creator.plural_connect_object:
                                for i in resul:
                                    if i:
                                        make_spring(con1, i)
                                        i.reset_color()
                                rope_creator.plural_connect_object = []
                            else:
                                if resul:
                                    make_spring(*resul)
                    case "glowrow":
                        con1 = get_click_cargo(mouse_interface.transform_mouse_to_global_cords())
                        resul = rope_creator.connect_object(con1)
                        if resul and con1:
                            if rope_creator.plural_connect_object:
                                for i in resul:
                                    if i:
                                        make_spring(con1, i)
                                        i.reset_color()
                                rope_creator.plural_connect_object = []
                            else:
                                if resul:
                                    make_glowrow(*resul)
                    case "rectangle" | "circle" | "circle_broken" | "circle_repulsive" | "circle_magnetic" | "rect_delete" | "rect_delete_rope" | "rect_rope" | "highlighting" | "gravity_manipulation":
                        pos_last_click = mouse_interface.transform_mouse_to_global_cords()
                    case "move":
                        moved = get_click_cargo(mouse_interface.transform_mouse_to_global_cords())
                        if moved is None:
                            moved = get_click_circles(mouse_interface.transform_mouse_to_global_cords())
                    case "delete":
                        reset()
                    case "rope_delete":
                        con1 = get_click_cargo(mouse_interface.transform_mouse_to_global_cords())
                        resul = rope_creator.connect_object(con1)
                        if resul:
                            rope = find_rope_with_objs(*resul)
                            if rope:
                                ropes.pop(rope[0])
                    case "cargo_delete":
                        delete_object(mouse_interface.transform_mouse_to_global_cords())
                    case "auto_rope":
                        if last_rope and last_cargo:
                            make_any_cargo(last_cargo, mouse_interface.transform_mouse_to_global_cords())
                            resul = rope_creator.connect_object(cargos[-1])
                            if resul:
                                make_any_rope(last_rope, (resul[0].pos-resul[1].pos).length(), *resul)
                                rope_creator.connect_object(cargos[-1])
                    case "rope_line" | "rect_rope_line" | "circle_rope_line":
                        if last_rope and last_cargo:
                            pos_last_click = mouse_interface.transform_mouse_to_global_cords()
                    case "ungravity":
                        make_ungravity(mouse_interface.transform_mouse_to_global_cords())
                    case "curve_rope_line":
                        if last_rope and last_cargo:
                            if pos_for_curve and\
                                    (pos_for_curve[0] - mouse_interface.transform_mouse_to_global_cords()).length() <= 5/camera.zoom:
                                make_curve_rope_line(pos_for_curve)
                                pos_for_curve = []
                            else:
                                pos_for_curve.append(mouse_interface.transform_mouse_to_global_cords())

        if event.type == pygame.MOUSEBUTTONUP and (event.button != 4 and event.button != 5):
            if pygame.mouse.get_pos()[1] < mouse_pos_as_toolbar:
                if type_used_block == "circle" and pos_last_click:
                    make_circle(pos_last_click, (pos_last_click - mouse_interface.transform_mouse_to_global_cords()).length())

                if type_used_block == "circle_broken" and pos_last_click:
                    make_circle_broken(pos_last_click,
                                (pos_last_click - mouse_interface.transform_mouse_to_global_cords()).length())

                if type_used_block == "circle_repulsive" and pos_last_click:
                    make_circle_repulsive(pos_last_click,
                                       (pos_last_click - mouse_interface.transform_mouse_to_global_cords()).length())

                if type_used_block == "circle_magnetic" and pos_last_click:
                    make_circle_magnetic(pos_last_click,
                                       (pos_last_click - mouse_interface.transform_mouse_to_global_cords()).length())

                if type_used_block == "rope_line" and pos_last_click:
                    make_rope_line(pos_last_click, mouse_interface.transform_mouse_to_global_cords())

                if type_used_block == "circle_rope_line" and pos_last_click:
                    make_circle_rope_line(pos_last_click, (pos_last_click - mouse_interface.transform_mouse_to_global_cords()).length())

                if type_used_block == "rect_rope_line" and pos_last_click:
                    make_rect_rope_line(pos_last_click, mouse_interface.transform_mouse_to_global_cords())

                if type_used_block == "rect_delete" and pos_last_click:
                    for i in get_all_object_in_rect(pos_last_click, mouse_interface.transform_mouse_to_global_cords()):
                        res = find_obj(i)
                        if res[1] == CARGO:
                            delete_rope_connection(i)
                            cargos.pop(res[0])
                        if res[1] == CIRCLE:
                            circles.pop(res[0])

                if type_used_block == "rect_delete_rope" and pos_last_click:
                    for i in get_all_cargo_in_rect(pos_last_click, mouse_interface.transform_mouse_to_global_cords()):
                        res = find_obj(i)
                        delete_rope_connection(i)

                if type_used_block == "rect_rope" and pos_last_click:
                    for i in get_all_cargo_in_rect(pos_last_click, mouse_interface.transform_mouse_to_global_cords()):
                        rope_creator.add_to_plural(i)

                if type_used_block == "highlighting" and pos_last_click:
                    moved_list += get_all_object_in_rect(pos_last_click, mouse_interface.transform_mouse_to_global_cords())
                    moved_list = list(set(moved_list))

                if type_used_block == "gravity_manipulation" and pos_last_click:
                    if (pos_last_click - mouse_interface.transform_mouse_to_global_cords()).length() != 0:
                        GRAVITY = (mouse_interface.transform_mouse_to_global_cords() - pos_last_click).normalize()

                if type_used_block == "rectangle":
                    make_rectangle(pos_last_click, mouse_interface.transform_mouse_to_global_cords())

                if is_cargo_type(type(moved)) and previous_pos_moved:
                    moved.velocity += (moved.pos - previous_pos_moved) / camera.zoom
                if moved and previous_pos_moved:
                    for i in moved_list:
                        if id(i) != id(moved) and is_cargo_type(type(i)):
                            i.velocity += (moved.pos - previous_pos_moved) / camera.zoom

                pos_last_click = None
                moved = None

            else:
                pass

        if event.type == pygame.MOUSEWHEEL:
            if pygame.mouse.get_pos()[1] >= mouse_pos_as_toolbar:
                toolbar.scroll_change(event.y)
            else:
                Bzoom = camera.zoom
                camera.zoom += event.y * 0.1
                camera.zoom = round(max(0.1, min(camera.zoom, 5)), 1)
                screen_size = pygame.display.get_window_size()
                Ww = (screen_size[0]/Bzoom-screen_size[0]/camera.zoom)/2
                Hh = (screen_size[1]/Bzoom-screen_size[1]/camera.zoom)/2
                Cw, Ch = 0, 0
                if Bzoom - camera.zoom != 0 and event.y > 0 :
                    Cw = (pygame.mouse.get_pos()[0]-screen_size[0]/2)/camera.zoom
                    Ch = (pygame.mouse.get_pos()[1]-screen_size[1]/2)/camera.zoom

                camera.pos += pygame.Vector2(Ww+Cw, Hh+Ch)

    camera.handle_keyboard()

    # physics proces
    display.fill((0, 0, 0))
    if not time_stop:
        for rope in ropes:
            if type(rope) == GLOWROW:
                rope.physics_processing(cargos, display, camera)
            else:
                rope.physics_processing()

        for cargo in cargos:
            if id(cargo) != id(moved):
                cargo.gravity(GRAVITY*gravity_scale)
                cargo.magnetic(cargos)

        for cargo in cargos:
            if cargo in moved_list:
                cargo.velocity *= 0
            cargo.update_pos(time_scale)

        for cargo in cargos:
            for circle in circles:
                if id(cargo) == id(moved):
                    continue

                if type(cargo) == PIN:
                    continue

                if cargo in moved_list:
                    continue

                circle.handle_collision(cargo)

    if moved:
        previous_pos_moved = moved.pos
        if type(moved) == RECTANGLE:
            moved.set_new_pos(mouse_interface.transform_mouse_to_global_cords())
        else:
            moved.pos = mouse_interface.transform_mouse_to_global_cords()

        distance = (moved.pos - previous_pos_moved).length()

        if distance > 0:
            direct = (moved.pos - previous_pos_moved).normalize()
            for i in moved_list:
                if id(i) != id(moved):
                    if type(i) == RECTANGLE:
                        i.set_new_pos(distance*direct+i.pos)
                    else:
                        i.pos = i.pos + distance*direct
                        if is_cargo_type(type(i)):
                            i.velocity *= 0
        else:
            for i in moved_list:
                if id(i) != id(moved) and is_cargo_type(type(i)):
                    i.pos -= i.velocity
                    i.velocity *= 0

    # drawing
    #display.fill((0, 0, 0))

    for circle in circles:
        if type(circle) == RECTANGLE:
            pygame.draw.rect(display, circle.color, circle.get_rect_to_draw(camera))
        else:
            pygame.draw.circle(display, circle.color, (circle.pos - camera.pos) * camera.zoom,
                               circle.radius * camera.zoom)

    for cargo in cargos:
        pygame.draw.circle(display, cargo.color, (cargo.pos - camera.pos) * camera.zoom, 5 * camera.zoom)

    for rope in ropes:
        pygame.draw.line(display, rope.color, (rope.connection1.pos - camera.pos) * camera.zoom,
                         (rope.connection2.pos - camera.pos) * camera.zoom)

    if pos_last_click:
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        last_transform_pos = (pos_last_click-camera.pos)*camera.zoom
        match type_used_block:
            case "circle" | "circle_rope_line" | "circle_broken" | "circle_repulsive" | "circle_magnetic":
                pygame.draw.circle(display, (50, 50, 50), (pos_last_click - camera.pos) * camera.zoom,
                                   (pos_last_click - mouse_interface.transform_mouse_to_global_cords()).length() * camera.zoom)
            case "rope_line" | "gravity_manipulation":
                pygame.draw.line(display, (50, 50, 50), (pos_last_click-camera.pos)*camera.zoom, mouse_pos)
            case "rect_rope_line" | "rect_delete" | "rect_delete_rope" | "rect_rope" | "highlighting":
                pygame.draw.lines(display, (50, 50, 50), True, (last_transform_pos, (last_transform_pos.x, mouse_pos.y),
                                                                mouse_pos, (mouse_pos.x, last_transform_pos.y)), 5)
            case "rectangle":
                pygame.draw.polygon(display, (50, 50, 50), (last_transform_pos, (last_transform_pos.x, mouse_pos.y),
                                                                mouse_pos, (mouse_pos.x, last_transform_pos.y)))

    if len(pos_for_curve) > 1:
        buf = [(i-camera.pos)*camera.zoom for i in pos_for_curve]
        pygame.draw.lines(display, (80, 80, 80), False, buf, 5)
    elif pos_for_curve:
        pygame.draw.circle(display, (80, 80, 80), (pos_for_curve[0]-camera.pos)*camera.zoom, 5)

    for i in moved_list:
        if type(i) in [CARGO, PIN, UN_GRAVITY]:
            pygame.draw.circle(display, (200, 200, 200), (i.pos-camera.pos)*camera.zoom, 8*camera.zoom,
                               int(3/camera.zoom))
        if type(i) in [CIRCLE, CIRCLE_MAGNETIC, CIRCLE_BROKEN, CIRCLE_REPULSIVE]:
            pygame.draw.circle(display, (200, 200, 200), (i.pos-camera.pos)*camera.zoom, (i.radius+3)*camera.zoom,
                               int(3/camera.zoom))
        if type(i) in [RECTANGLE]:
            pygame.draw.rect(display, (200, 200, 200), i.get_rect_to_draw(camera), int(3/camera.zoom))

    pygame.draw.rect(display, gradient_detector[int(time_scale)], (20, 20, 20, 20))
    pygame.draw.rect(display, gradient_detector[int(gravity_scale)], (20, 40, 20, 20))

    # стоит сделать отдельный метод для этого
    # draw toolbar
    pygame.draw.rect(display, (100, 100, 100), (0, mouse_pos_as_toolbar, window_size[0], window_size[1]))

    i = 0
    j = 0
    now = (i + j * toolbar.count_widget_on_lvl())
    while len(toolbar.buttons) > now + toolbar.scroll and now < toolbar.max_count_widget():
        b = toolbar.buttons[now + toolbar.scroll]

        display.blit(b.img, (i * widget_size[0], j * widget_size[1] + mouse_pos_as_toolbar))

        j += (i + 1) // toolbar.count_widget_on_lvl()
        i = (i + 1) % toolbar.count_widget_on_lvl()
        now = (i + j * toolbar.count_widget_on_lvl())

    if (not toolbar.last_ind_found is None) and toolbar.last_ind_found - toolbar.scroll >= 0:
        pos_last_found = toolbar.get_button_pos_from_index(toolbar.last_ind_found - toolbar.scroll)
        pos_last_founds = pygame.Vector2(pos_last_found[0], pos_last_found[1] + mouse_pos_as_toolbar)
        pygame.draw.rect(display, (255, 200, 200),
                         (pos_last_founds.x, pos_last_founds.y, widget_size[0], widget_size[1]), 5)

    m1 = pygame.Vector2(pygame.mouse.get_pos())
    m1 = toolbar.transform_to_toolbar_pos(pygame.Vector2(m1.x, m1.y - mouse_pos_as_toolbar))
    m1 = pygame.Vector2(m1.x * widget_size[0], m1.y * widget_size[1] + mouse_pos_as_toolbar)

    if pygame.mouse.get_pos()[1] >= mouse_pos_as_toolbar:
        pygame.draw.rect(display, (255, 0, 0), (m1.x, m1.y, widget_size[0], widget_size[1]), 5)

    pygame.display.flip()
    clock.tick(FPS)
