import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, sprite):
        super().__init__()
        self.image = sprite
        self.rect = self.image.get_rect(topleft = pos)
        # Função inflate para mudar o tamanho do retângulo
        self.hitbox = self.rect.inflate(0,-10)

    def getHitbox(self):
        return self.hitbox

class Chao(pygame.sprite.Sprite):
    def __init__(self, pos, filepath):
        super().__init__()

        self.__image = pygame.__image.load(filepath).convert_alpha()
        self.__rect = self.__image.get_rect(topleft = pos)

    def getRect(self):
        return self.__rect

    def getImage(self):
        return self.__image

    def setImage(self, image):
        self.__image = image
    