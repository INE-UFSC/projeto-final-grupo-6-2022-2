from singletonMeta import SingletonMeta
from math import sqrt
from character import Character


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
            attacker = self.__player
        else:
            enemies = [self.__player]
            if isinstance(enemy_sel, Character):
                attacker = enemy_sel
            else:
                return 0
        for enemy in enemies:
            x, y = enemy.getPos()
            x1, y1 = attacker.getPos()
            diffx = x - x1
            diffy = y - y1
            status = attacker.getStatus()
            if (status == 'up' and diffy) > 0 or (status == 'down' and diffy) < 0 or (
                status == 'left' and diffx > 0) or (status == 'right' and diffx < 0):
                continue
            dist = sqrt((diffx)**2 + (diffy)**2)
            if dist <= attack_range:
                enemy.receiveDamage(damage)

    def projectile_damage(self, projectile, enemy):
        dmg = projectile.getDamage()
        # enemy.receiveDamage(dmg)
        
