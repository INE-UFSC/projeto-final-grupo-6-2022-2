from character import Character
import pygame
from math import sqrt


class EnemyLowDMG(Character, pygame.sprite.Sprite):

    # CONFERIR NECESSIDADE:
    __enemy_counter = 0

    # balancear os valores de vida e velocidade:
    def __init__(self, pos, sprite):
        super().__init__(100, pos, 4, sprite)
        self.__range = 5

    # CONFERIR NECESSIDADE:
    @classmethod
    def spawn(cls):
        cls.__enemy_counter += 1

    def die(self):
        self.kill()

    # INACABADO
    def reactToLight(self, player):
        posx, posy = player.getPos()
        diffx = posx - self.__posx
        diffy = posy - self.__posy
        dist = sqrt(diffx**2 + diffy**2)
    # DECISAO EM Y:
        if diffy > 0:
            self.direction.x = 1
            self.status = 'down'
        elif diffx == 0:
            self.direction.x = 0
        else:
            self.direction.x = -1
            self.status = 'up'
    # DECISAO EM X:
        if diffx > 0:
            self.direction.x = 1
            self.status = 'right'
        elif diffx == 0:
            self.direction.x = 0
        else:
            self.direction.x = -1
            self.status = 'left'
    # DETECCAO DO AUTO_ATAQUE:
        if dist < self.__range:
            self.attack(player)
    
