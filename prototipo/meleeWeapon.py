from weapon import Weapon
from damageController import DamageController
from assetController import AssetController


class MeleeWeapon(Weapon):

    def __init__(self, x, y, name, dmg, _range, cooldown):
        super().__init__(x, y, AssetController().get_asset(name), cooldown)
        self.__damage = dmg
        self.__range = _range

    def getRange(self):
        return self.__range

    def getDamage(self):
        return self.__damage

    def attack(self, attack_direction):
        dmg_ctrl = DamageController()
        dmg_ctrl.melee_attack(self.__damage, self.__range, attack_direction)
