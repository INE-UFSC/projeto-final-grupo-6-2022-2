from item import Item
from abc import ABC


class Weapon(ABC, Item):
    def __init__(self, x, y, group, sprite, damage, range):
        super().__init__(x, y, sprite, group)
        self.__damage = damage
        self.__range = range

    def use(self, player):
        player.setWeapon(self)

    def getRange(self):
        return self.__range

    def getDamage(self):
        return self.__damage
