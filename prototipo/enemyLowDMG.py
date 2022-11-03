from enemy import Enemy
from abc import ABC
import pygame
from math import sqrt


class EnemyLowDMG(Enemy):

    # balancear os valores de vida e velocidade:
    def __init__(self, pos, sprite, groups, obstacle_sprites, player):
        super().__init__(100, pos, 4, sprite, 20, groups, obstacle_sprites, player)
        self.__range = 5

    # INACABADO:
    def die(self):
        self.kill()

    # INACABADO:
    def reactToLight(self):
        posx, posy = self.__player.getPos()
        diffx = posx - self.__posx
        diffy = posy - self.__posy
        dist = sqrt(diffx**2 + diffy**2)
        # RANGE DA VISAO DO INIMIGO:
        if dist < 100 and self.__player.getLight().getStatus():
            self.__awake = True
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
        else: 
            self.__awake = False
            self.direction.x = 0
            self.direction.y = 0
        # DETECCAO DO AUTO_ATAQUE:
        if dist < self.__range and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            self.attack(self.__player)
