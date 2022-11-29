from abc import ABC, abstractmethod
from math import sqrt
import pygame


class Character(ABC, pygame.sprite.Sprite):
    def __init__(self, health: int, pos: tuple, speed: int, sprite: str):
        super().__init__()
        self.__health = health
        self.__speed = speed
        self.__posx = pos[0]
        self.__posy = pos[1]
        # PLANEJAR COMO LIDAR COM EXCECOES:
        self.__sprite = self.image = pygame.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        # CONFERIR COMO LIDAR COM OS PARAMETROS DE INFLATE:
        self.hitbox = self.rect.inflate(0,-26)
        self.__status = 'down'
        self.__frame_index = 0
        self.__animation_speed = 0.15
        self.__direction = pygame.math.Vector2()
        
        self.__attacking = False
        self.__attack_cooldown = 400
        self.__attack_time = 0

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.__attacking:
            if current_time - self.__attack_time > self.__attack_cooldown:
                self.__attacking = False

    def getAttackingStatus(self):
        return self.__attacking

    def setAttackingStatus(self):
        self.__attacking = True

    def setAttackTimer(self):
        self.__attack_time = pygame.time.get_ticks()

    def getSpeed(self):
        return self.__speed
    
    def getPos(self):
        return (self.hitbox.x, self.hitbox.y)

    def getHealth(self):
        return self.__health
    
    def setHealth(self, health):
        if isinstance(health, int):
            self.__health = health

    def getDirectionMagnitude(self):
        return self.__direction.magnitude()

    def getDirectionX(self):
        return self.__direction.x

    def setDirectionX(self, x):
        self.__direction.x = x

    def getDirectionY(self):
        return self.__direction.y

    def setDirectionY(self, y):
        self.__direction.y = y

    def directionNormalize(self):
        self.__direction.normalize_ip()
    
    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        self.__status = status

    def setFrameIndex(self, frame_index):
        if isinstance(frame_index, int) or isinstance(frame_index, float):
            self.__frame_index = frame_index

    def getFrameIndex(self):
        return self.__frame_index
    
    def getAnimationSpeed(self):
        return self.__animation_speed

    def getObstacleSprites(self):
        return self.__obstacle_sprites

    def receiveDamage(self, damage: int):
        if isinstance(damage, int):
            if self.__health <= damage:
                self.die()
            else:
                self.__health -= damage

    @abstractmethod
    def die(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def update(self):
        pass
