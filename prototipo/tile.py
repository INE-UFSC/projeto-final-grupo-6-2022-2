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

        self.image = pygame.image.load(filepath).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
    