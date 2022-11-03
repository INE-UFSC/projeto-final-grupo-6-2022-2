from enemy import Enemy
import pygame
from math import sqrt


class EnemyHighDMG(Enemy):

    def __init__(self, pos, sprite, groups, obstacle_sprites, player):
        super().__init__(500, pos, 3, sprite, 100, groups, obstacle_sprites,player)
        self.__range = 5
        self.__confusion_counter = 0

    # INACABADO:
    def die(self):
        self.kill()

    # INACABADO (DEVE SER AFETADO PELA LANTERNA E NAO PELO RANGE):
    def reactToLight(self):
        posx, posy = self.__player.getPos()
        diffx = posx - self.__posx
        diffy = posy - self.__posy
        dist = sqrt(diffx**2 + diffy**2)
        # RANGE DA LANTERNA:
        if (dist < 20) and self.__player.getLight().getStatus():
            self.__awake = True
            self.__confusion_counter = 5
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
        # CONTADOR PARA CICLOS CONFUSO:
        elif self.__confusion_counter > 0:
            self.__confusion_counter -= 1
        # FORA DO RANGE DA LANTERNA:
        elif dist < 100:
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
        # DETECCAO DO AUTO_ATAQUE (INACABADO - NAO ATACA COM A LANTERNA LIGADA):
        if dist < self.__range and not self.__player.getLight().getStatus() and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            self.attack(self.__player)
            