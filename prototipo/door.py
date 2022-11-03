import pygame
from item import Item

class Door(Item):
    def  __init__(self, x, y, sprite,grupo):
        super().__init__(x, y, sprite, grupo)
        
    def usar(self, jogador):
        pass
    