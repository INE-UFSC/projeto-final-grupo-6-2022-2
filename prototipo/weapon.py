from item import Item


class Weapon(Item):
    def __init__(self, x, y, sprite, grupo, damage):
        super().__init__(self, x, y, sprite,grupo)
        self.__damage = damage

    def use(self, player):
        pass
