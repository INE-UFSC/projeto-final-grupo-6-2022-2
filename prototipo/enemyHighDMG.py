from enemy import Enemy
import pygame
from math import sqrt


class EnemyHighDMG(Enemy):

    def __init__(self, pos, sprite):
        super().__init__(500, pos, 3, sprite, 100)
        self.__range = 5

    # INACABADO:
    def die(self):
        self.kill()

    # INACABADO (DEVE SER AFETADO PELA LANTERNA E NAO PELO RANGE):
    def reactToLight(self, player):
        posx, posy = player.getPos()
        diffx = posx - self.__posx
        diffy = posy - self.__posy
        dist = sqrt(diffx**2 + diffy**2)
        # RANGE DA LANTERNA:
        if (dist < 20) and player.lanterna.getStatus():
        # DECISAO EM Y:
            if diffy >= 0:
                self.direction.x = -1
                self.status = 'up'
            else:
                self.direction.x = 1
                self.status = 'down'
        # DECISAO EM X:
            if diffx >= 0:
                self.direction.x =  -1
                self.status = 'left'
            else:
                self.direction.x = 1
                self.status = 'right'
        # FORA DO RANGE DA LANTERNA:
        else:
            if dist < 100:
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
        # DETECCAO DO AUTO_ATAQUE (INACABADO - NAO ATACA COM A LANTERNA LIGADA):
        if dist < self.__range:
            self.attack(player)