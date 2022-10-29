from character import Character
from abc import abstractmethod


class Enemy(Character):

    def __init__(self, health: int, pos: tuple, speed: int, sprite: str, damage: int, groups):
        super().__init__(health, pos, speed, sprite, groups)
        self.__awake = False
        self.__damage = damage

    @abstractmethod
    def spawn(self, pos):
        pass

    @abstractmethod
    def reactToLight(self, light_pos):
        pass
    