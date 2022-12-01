import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, pos, sprite, direction, damage, speed):
        super().__init__()
        self.__sprite = self.image = pygame.image.load(sprite).convert_alpha()
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
