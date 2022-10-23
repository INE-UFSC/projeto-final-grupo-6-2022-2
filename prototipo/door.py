import pygame
from tile import Tile

class Door(Tile):
    def __init__(self, pos, groups, tipo):
        super().__init__(pos, groups, tipo)