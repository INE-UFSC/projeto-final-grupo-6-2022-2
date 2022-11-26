from item import Item
from abc import ABC, abstractmethod


class Weapon(Item, ABC):
    def __init__(self, x, y, sprite):
        super().__init__(x, y, sprite)

    def use(self, player):
        player.setWeapon(self)

    @abstractmethod
    def attack(self):
        pass
