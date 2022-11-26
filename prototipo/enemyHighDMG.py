from enemy import Enemy
import pygame
from math import sqrt


class EnemyHighDMG(Enemy):

    def __init__(self, pos, obstacle_sprites, player):
        super().__init__(700, pos, 3, 'tiles/rock.png', 100, obstacle_sprites, player)
        self.__confusion_counter = 0

    def die(self):
        self.kill()

    def reactToLight(self):
        posx, posy = self.getPlayer().getPos()
        diffx = posx - self.getPos()[0]
        diffy = posy - self.getPos()[1]
        dist = sqrt(diffx**2 + diffy**2)
        # RANGE DA LANTERNA:
        if (dist < 200) and self.getPlayer().getLight().getStatus():
            self.__awake = True
            self.__confusion_counter = 100
        # DECISAO EM Y:
            if diffy >= 0:
                self.setDirectionY(-1)
                self.setStatus('up')
            else:
                self.setDirectionY(1)
                self.setStatus('down')
        # DECISAO EM X:
            if diffx >= 0:
                self.setDirectionX(-1)
                self.setStatus('left')
            else:
                self.setDirectionX(1)
                self.setStatus('right')
        # CONTADOR PARA CICLOS CONFUSO:
        elif self.__confusion_counter > 0:
            self.__confusion_counter -= 1
        # FORA DO RANGE DA LANTERNA:
        elif dist < 400:
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
        # DETECCAO DO AUTO_ATAQUE (INACABADO - NAO ATACA COM A LANTERNA LIGADA):
        if dist < self.getRange() and not self.getPlayer().getLight().getStatus() and not self.getAttackingStatus():
            self.setAttackingStatus()
            self.setAttackTimer()
            self.attack()
            