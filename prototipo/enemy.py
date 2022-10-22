from character import Character
from abc import abstractmethod


class Enemy(Character):

    def __init__(self, size: int, health: int, pos: tuple, speed: int, sprite: str, damage: int):
        super().__init__(size, health, pos, speed, sprite)
        self.__awake = False

    @abstractmethod
    def spawn(self, pos):
        pass

    @abstractmethod
    def reactToLight(self, light_pos):
        pass
    