from item import Item
from abc import ABC, abstractmethod


class Weapon(Item, ABC):
    def __init__(self, x, y, sprite, cooldown):
        super().__init__(x, y, sprite)
        self.__attack_cooldown = cooldown

    def use(self, player):
        player.setWeapon(self)

    def getAttackCooldown(self):
        return self.__attack_cooldown

    @abstractmethod
    def attack(self):
        pass
