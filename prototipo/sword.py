from weapon import Weapon
from singletonMeta import SingletonMeta


class Sword(metaclass=SingletonMeta, Weapon):

    def __init__(self, x, y, group):
        super().__init__(x, y, group, 'tiles/sw.png', 115, 1200)
        