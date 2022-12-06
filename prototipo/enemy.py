from character import Character
from abc import abstractmethod
from damageController import DamageController


class Enemy(Character):
    def __init__(self, health: int, pos: tuple, speed: int, sprite: str, damage: int):
        super().__init__(health, pos, speed, sprite)
        self.__player_pos = ()
        self.__light_status = False
        self.__awake = False
        self.__damage = damage
        self.__range = 400

    def attack(self):
        dmg_ctrl = DamageController()
        dmg_ctrl.melee_attack(self.__damage, self.__range, self)

    def update(self):
        self.cooldowns()
        self.reactToLight()

    def light_info_update(self, player_pos: tuple, light_status: bool):
        self.__player_pos = player_pos
        self.__light_status = light_status

    def getPlayerPos(self):
        return self.__player_pos

    def getLightStatus(self):
        return self.__light_status

    def die(self):
        self.kill()

    @abstractmethod
    def reactToLight(self):
        pass

    def getRange(self):
        return self.__range
