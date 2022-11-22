import pygame
from item import Item

class Door(Item):
    def __init__(self, x, y, sprite):
        super().__init__(x, y, sprite)
        
    def use(self, jogador):
        pass
    