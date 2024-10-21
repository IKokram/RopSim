import pygame
import example
from cargo import CARGO


class GLOWROW:
    def __init__(self, length: float, connection1: example.EXAMPLE, connection2: example.EXAMPLE,
                 rigidity: float) -> None:
        self.color = pygame.Color(190, 190, 190)
        self.length = length
        self.connection1 = connection1
        self.connection2 = connection2
        self.rigidity = rigidity
        
        self.last_pos1 = self.connection1.pos
        self.last_pos2 = self.connection2.pos

    def physics_processing(self, cargos: list, disp, cam) -> None:
        p1 = self.connection1.pos
        p2 = self.connection2.pos
        length = (p1-p2).length()

        previous_p1 = self.last_pos1
        previous_p2 = self.last_pos2

        direct = (p2-p1)/length

        p1 = p1 - direct*5
        p2 = p2 + direct*5

        length = (p1-p2).length()

        for cargo in cargos:
            if id(cargo) == id(self.connection1) or id(cargo) == id(self.connection2): continue
            pc = cargo.pos

            scal = (pc-p1).dot(p2-p1)/length
            vec_new = direct * scal
            vec_norm = pc-(p1+vec_new)

            apc = cargo.pos + cargo.velocity
            ascal = (apc-p1).dot(p2-p1)/length
            avec_new = direct * ascal
            avec_norm = apc-(p1+avec_new)

            if not ((scal < 0 and ascal < 0) or (scal > length and ascal > length)):

                if avec_norm.dot(vec_norm) <= 0:
                    cargo.velocity += cargo.velocity.length() * vec_norm.normalize()
                    cargo.pos = p1+vec_new + vec_norm.normalize()*5
                
                elif vec_norm.length() <= 5:
                    cargo.velocity += cargo.velocity.length() * vec_norm.normalize()
                    cargo.pos = p1+vec_new + vec_norm.normalize()*5
                
                elif avec_norm.length() <= 5:
                    cargo.velocity += cargo.velocity.length() * vec_norm.normalize()
                    cargo.pos = p1+vec_new + vec_norm.normalize()*5
        



        self.last_pos1 = self.connection1.pos
        self.last_pos2 = self.connection2.pos
            

