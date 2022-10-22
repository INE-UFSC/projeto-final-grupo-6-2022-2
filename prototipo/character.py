from abc import ABC, abstractmethod
from math import sqrt


class Character(ABC):

    def __init__(self, size: int, health: int, pos: tuple, speed: int):
        self.__size = size
        self.__health = health
        self.__speed = speed
        self.__diagonal_speed = speed/sqrt(2)
        self.__posx = pos[0]
        self.__posy = pos[1]

    def getPos(self):
        return (self.__posx, self.__posy)

    def getHealth(self):
        return self.__health

    def receiveDamage(self, damage: int):
        if isinstance(damage, int):
            self.__health -= damage

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def die(self):
        pass

