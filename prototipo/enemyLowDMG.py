from enemy import Enemy
from abc import ABC
import pygame
from math import sqrt


class EnemyLowDMG(Enemy):

    # balancear os valores de vida e velocidade:
    def __init__(self, pos, obstacle_sprites, player):
        super().__init__(200, pos, 4, 'tiles/porta.png', 20, obstacle_sprites, player)

    def die(self):
        self.kill()

    def reactToLight(self):
        posx, posy = self.getPlayer().getPos()
        diffx = posx - self.getPos()[0]
        diffy = posy - self.getPos()[1]
        dist = sqrt(diffx**2 + diffy**2)
        # RANGE DA VISAO DO INIMIGO:
        if dist < 110 and self.getPlayer().getLight().getStatus():
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
        if dist < self.getRange() and not self.getAttackingStatus():
            self.setAttackingStatus()
            self.setAttackTimer()
            self.attack()
