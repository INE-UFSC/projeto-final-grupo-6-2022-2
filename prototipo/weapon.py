from item import Item


class Weapon(Item):
    def __init__(self, x, y, sprite, grupo, damage, range):
        super().__init__(self, x, y, sprite,grupo)
        self.__damage = damage
        self.__range = range

    def use(self, player):
        player.setWeapon(self)

    def getRange(self):
        return self.__range

    def getDamage(self):
        return self.__damage
