from enemy import Enemy
from math import sqrt
from enemyLowDMG import EnemyLowDMG


class EnemyHighDMG(Enemy):

    def __init__(self, pos):
        super().__init__(700, pos, 3, 'enemyhighdmg', 100)
        self.__confusion_counter = 0


    def reactToLight(self):
        posx, posy = self.getPlayerPos()
        diffx = posx - self.getPos()[0]
        diffy = posy - self.getPos()[1]
        dist = sqrt(diffx**2 + diffy**2)
        # RANGE DA LANTERNA:
        if (dist < 200) and self.getLightStatus():
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
        if dist < self.getRange() and not self.getLightStatus() and not self.getAttackingStatus():
            self.setAttackingStatus()
            self.setAttackTimer()
            self.attack()
            
    def die(self):

        self.__enemyLowDMG1 = EnemyLowDMG(self.getPos())
        self.__enemyLowDMG2 = EnemyLowDMG(pos = (self.getPos()[0] + 20, self.getPos()[1] + 20))
        self.__enemyLowDMG3 = EnemyLowDMG(pos = (self.getPos()[0] + 30, self.getPos()[1] + 30))

        self.spawn_enemy(self.__enemyLowDMG1)
        self.spawn_enemy(self.__enemyLowDMG2)
        self.spawn_enemy(self.__enemyLowDMG3)
        
        self.getSpawnEnemy()(self.__enemyLowDMG1)
        self.getSpawnEnemy()(self.__enemyLowDMG2)
        self.getSpawnEnemy()(self.__enemyLowDMG3)

        self.kill()

