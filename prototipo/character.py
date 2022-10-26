from abc import ABC, abstractmethod
from math import sqrt
import pygame


class Character(ABC, pygame.sprite.Sprite):

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

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction.normalize()
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

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

    @abstractmethod
    def collision(self, direction):
        pass
