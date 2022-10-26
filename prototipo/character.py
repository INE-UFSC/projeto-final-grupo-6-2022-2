from abc import ABC, abstractmethod
from math import sqrt
import pygame


class Character(ABC):

    def __init__(self, health: int, pos: tuple, speed: int, sprite: str):
        self.__health = health
        self.__speed = speed
        self.__diagonal_speed = speed/sqrt(2)
        self.__posx = pos[0]
        self.__posy = pos[1]
        # PLANEJAR COMO LIDAR COM EXCECOES:
        self.__sprite = self.image = pygame.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        # CONFERIR COMO LIDAR COM OS PARAMETROS DE INFLATE:
        self.hitbox = self.rect.inflate(0,-26)

    def getPos(self):
        return (self.__posx, self.__posy)

    def getHealth(self):
        return self.__health

    def receiveDamage(self, damage: int):
        if isinstance(damage, int):
            if self.__health <= damage:
                self.die()
            else:
                self.__health -= damage

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def die(self):
        pass

    @abstractmethod
    def attack(self, receiver):
        pass
