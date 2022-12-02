import pygame
from damageController import DamageController


class Projectile(pygame.sprite.Sprite):

    def __init__(self, pos, sprite, direction, damage, speed):
        super().__init__()
        self.__sprite = self.image = pygame.image.load(sprite).convert_alpha()
        pos = list(pos)
        pos[0] += direction[0]*25
        pos[1] += direction[1]*50
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -5)
        self.__damage = damage
        self.__direction = pygame.math.Vector2()
        self.__direction.x = direction[0]
        self.__direction.y = direction[1]
        self.__speed = speed

    def getDamage(self):
        return self.__damage

    def getSpeed(self):
        return self.__speed

    def getDirectionMagnitude(self):
        return self.__direction.magnitude()

    def getDirection(self):
        return self.__direction.x, self.__direction.y

    def directionNormalize(self):
        self.__direction.normalize_ip()

    def hit(self, enemy):
        DamageController().projectile_damage(self, enemy)
        self.kill()
