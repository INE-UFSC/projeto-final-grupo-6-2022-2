import pygame
from settings import *
from tile import Tile
from jogador import Jogador
from item import *
from key import Key
from door import Door
from pilha import Pilha
from enemyLowDMG import EnemyLowDMG
from enemyHighDMG import EnemyHighDMG
from ySortCameraGroup import YSortCameraGroup


class LevelBuilder:

    def __init__(self):
        # Pegar a tela
        self.selected_room = 0
        self.key = ''
        self.rooms = ROOMS
        self.display_surface = pygame.display.get_surface()
        self.create_map()

    def create_map(self):
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.itens_sprites = []
        self.enemy_sprites = pygame.sprite.Group()
        for row_index, row in enumerate(self.rooms[self.selected_room]):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    tile = Tile((x, y), 'rock')
                    self.visible_sprites.add(tile)
                    self.obstacle_sprites.add(tile)
                elif col == 'p':
                    self.jogador = Jogador((x, y), self.obstacle_sprites, self.itens_sprites,
                                           self.enemy_sprites)
                    self.visible_sprites.add(self.jogador)
                elif col == 'b':
                    battery = Pilha(x, y, 'tiles/pilha.png', 50)
                    self.itens_sprites.append(battery)
                    self.visible_sprites.add(battery)
                elif col == 'l':
                    door = Door(x, y, 'tiles/porta.png')
                    self.visible_sprites.add(door)
                    self.obstacle_sprites.add(door)
                    self.door = door
                    self.itens_sprites.append(door)
                elif col == 'k':
                    key = Key(x, y, 'tiles/key.png')
                    self.visible_sprites.add(key)
                    self.itens_sprites.append(key)
                    self.key = key
                elif col == 'el':
                    enemy = EnemyLowDMG((x, y), self.obstacle_sprites, self.jogador)
                    self.visible_sprites.add(enemy)
                    self.enemy_sprites.add(enemy)
                elif col == 'eh':
                    enemy = EnemyHighDMG((x, y), self.obstacle_sprites,
                                 self.jogador)
                    self.visible_sprites.add(enemy)
                    self.enemy_sprites.add(enemy)