import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('tiles/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        # Função inflate para mudar o tamanho do retângulo
        self.hitbox = self.rect.inflate(0,-10)