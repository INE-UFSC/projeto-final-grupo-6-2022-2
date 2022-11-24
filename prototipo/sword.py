from weapon import Weapon
from damageController import DamagaController


class MeleeWeapon(Weapon):

    def __init__(self, x, y, name, dmg, _range):
        super().__init__(x, y, f'tiles/{name}.png')
        self.__damage = dmg
        self.__range = _range

    def getRange(self):
        return self.__range

    def getDamage(self):
        return self.__damage

    def attack(self):
        dmg_ctrl = DamagaController()
        dmg_ctrl.meele_attack(self.getDamage(), self.getRange())
