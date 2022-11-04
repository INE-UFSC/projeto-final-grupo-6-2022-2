from enemy import Enemy
from abc import ABC
import pygame
from math import sqrt


class EnemyLowDMG(Enemy):

    # balancear os valores de vida e velocidade:
    def __init__(self, pos, groups, obstacle_sprites, player):
        super().__init__(100, pos, 4, 'tiles/porta.png', 20, groups, obstacle_sprites, player)
        self.__range = 5

    # INACABADO:
    def die(self):
        self.kill()

    # INACABADO:
    def reactToLight(self):
        posx, posy = self.getPlayer().getPos()
        diffx = posx - self.getPos()[0]
        diffy = posy - self.getPos()[1]
        dist = sqrt(diffx**2 + diffy**2)
        print(dist)
        # RANGE DA VISAO DO INIMIGO:
        if dist < 100 and self.getPlayer().getLight().getStatus():
            print('teste')
            self.__awake = True
        # DECISAO EM Y:
            if diffy > 0:
                self.setDirectionY(1)
                self.setStatus('down')
            elif diffx == 0:
                self.setDirectionY(0)
            else:
                self.setDirectionY(-1)
                self.setStatus('up')
        # DECISAO EM X:
            if diffx > 0:
                self.setDirectionX(1)
                self.setStatus('right')
            elif diffx == 0:
                self.setDirectionX(0)
            else:
                self.setDirectionX(-1)
                self.setStatus('left')
        else: 
            self.__awake = False
            self.setDirectionX(0)
            self.setDirectionY(0)
        # DETECCAO DO AUTO_ATAQUE:
        if dist < self.__range and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            self.attack(self.getPlayer())
