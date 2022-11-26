from singletonMeta import SingletonMeta
from math import sqrt


class DamageController(metaclass=SingletonMeta):

    def __init__(self):
        self.__enemies = None
        self.__player = None

    def update_characters(self, enemies, player):
        self.__enemies = enemies
        self.__player = player

    def meele_attack(self, damage, attack_range, enemy_sel='enemies'):
        if enemy_sel == 'enemies':
            enemies = self.__enemies
        else:
            enemies = [self.__player]
        for enemy in enemies:
            x, y = enemy.getPos()
            x1, y1 = self.__player.getPos()
            diffx = x - x1
            diffy = y - y1
            status = self.__player.getStatus()
            if (status == 'up' and diffy) > 0 or (status == 'down' and diffy) < 0 or (
                status == 'left' and diffx > 0) or (status == 'right' and diffx < 0):
                continue
            dist = sqrt((diffx)**2 + (diffy)**2)
            if dist <= attack_range:
                enemy.receiveDamage(damage)

    def projectile_damage(self, projectile, enemy):
        dmg = projectile.getDamage()
        # enemy.receiveDamage(dmg)