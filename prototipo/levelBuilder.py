from settings import *
from tile import Tile
from jogador import Jogador
from item import *
from key import Key
from door import Door
from pilha import Pilha
from hud import Hud
from enemyLowDMG import EnemyLowDMG
from enemyHighDMG import EnemyHighDMG
from ySortCameraGroup import YSortCameraGroup


class LevelBuilder:

    def __init__(self):
        # Pegar a tela
        # self.__key = ''
        # self.display_surface = pygame.display.get_surface()
        # self.create_map()

        self.rooms = ROOMS

    def create_map(self, selected_room):
        self.__visible_sprites = YSortCameraGroup()
        self.__obstacle_sprites = pygame.sprite.Group()
        self.__hud = Hud()
        self.__itens_sprites = []
        self.__enemy_sprites = pygame.sprite.Group()
        for row_index, row in enumerate(self.rooms[selected_room]):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    tile = Tile((x, y), 'rock')
                    self.__visible_sprites.add(tile)
                    self.__obstacle_sprites.add(tile)
                elif col == 'p':
                    self.__player = Jogador((x, y), self.__obstacle_sprites, self.__itens_sprites, self.__enemy_sprites, 100)
                    self.__visible_sprites.add(self.__player)
                elif col == 'b':
                    battery = Pilha(x, y, 'tiles/pilha.png', 50)
                    self.__itens_sprites.append(battery)
                    self.__visible_sprites.add(battery)
                elif col == 'l':
                    door = Door(x, y, 'tiles/porta.png')
                    self.__visible_sprites.add(door)
                    self.__obstacle_sprites.add(door)
                    self.__door = door
                    self.__itens_sprites.append(door)
                elif col == 'k':
                    key = Key(x, y, 'tiles/key.png')
                    self.__visible_sprites.add(key)
                    self.__itens_sprites.append(key)
                    self.__key = key
                elif col == 'el':
                    enemy = EnemyLowDMG((x, y), self.__obstacle_sprites, self.__player)
                    self.__visible_sprites.add(enemy)
                    self.__enemy_sprites.add(enemy)
                elif col == 'eh':
                    enemy = EnemyHighDMG((x, y), self.__obstacle_sprites, self.__player)
                    self.__visible_sprites.add(enemy)
                    self.__enemy_sprites.add(enemy)

    def getKey(self):
        return self.__key

    def getDoor(self):
        return self.__door

    def getPlayer(self):
        return self.__player

    def getVisibleSprites(self):
        return self.__visible_sprites

    def getObstacleSprites(self):
        return self.__obstacle_sprites

    def getItensSprites(self):
        return self.__itens_sprites

    def getEnemySprites(self):
        return self.__enemy_sprites
    
    def getHud(self):
        return self.__hud