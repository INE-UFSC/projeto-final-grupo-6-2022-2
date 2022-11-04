from enemy import Enemy
import pygame
from math import sqrt


class EnemyHighDMG(Enemy):

    def __init__(self, pos, groups, obstacle_sprites, player):
        super().__init__(500, pos, 3, 'tiles/rock.png', 100, groups, obstacle_sprites,player)
        self.__range = 5
        self.__confusion_counter = 0

    # INACABADO:
    def die(self):
        self.kill()

    # INACABADO (DEVE SER AFETADO PELA LANTERNA E NAO PELO RANGE):
    def reactToLight(self):
        posx, posy = self.getPlayer().getPos()
        diffx = posx - self.__posx
        diffy = posy - self.__posy
        dist = sqrt(diffx**2 + diffy**2)
        # RANGE DA LANTERNA:
        if (dist < 20) and self.getPlayer().getLight().getStatus():
            self.__awake = True
            self.__confusion_counter = 5
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
        elif dist < 100:
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
        if dist < self.__range and not self.getPlayer().getLight().getStatus() and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            self.attack(self.getPlayer())
            