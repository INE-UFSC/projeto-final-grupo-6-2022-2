from settings import *
from tile import Tile, Chao
from jogador import Jogador
from item import *
from key import Key
from door import Door
from pilha import Pilha
from hud import Hud
from enemyLowDMG import EnemyLowDMG
from enemyHighDMG import EnemyHighDMG
from ySortCameraGroup import YSortCameraGroup
from damageController import DamageController
from Projectile import Projectile
from projectileWeapon import ProjectileWeapon
from meleeWeapon import MeleeWeapon


class LevelBuilder:

    def __init__(self):
        self.rooms = ROOMS

    def selected_floor(self, sala):
        if sala == 1:
            self.chao = pygame.image.load('tiles/chao.png').convert_alpha()
        if sala == 2:
            self.chao = pygame.image.load('tiles/chao2.png').convert_alpha()
        return self.chao
    

    def create_map(self, selected_room):
        self.__dmg_ctrl = DamageController()
        self.__visible_sprites = YSortCameraGroup()
        self.__obstacle_sprites = pygame.sprite.Group()
        self.__hud = Hud()
        self.__item_sprites = []
        self.__enemy_sprites = pygame.sprite.Group()
        self.__projectile_sprites = pygame.sprite.Group()
        self.__chao = Chao((0,0), f'tiles/chao{selected_room}.png')
        self.__visible_sprites.add(self.__chao)
        for row_index, row in enumerate(self.rooms[selected_room]):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    tile = Tile((x, y), 'parede_vertical_esquerda')
                    self.__visible_sprites.add(tile)
                    self.__obstacle_sprites.add(tile)
                elif col == 'm':
                    tile = Tile((x, y), 'parede_quina_direita_cima')
                    self.__visible_sprites.add(tile)
                    self.__obstacle_sprites.add(tile)
                elif col == 'n':
                    tile = Tile((x, y), 'parede_quina_esquerda_baixo')
                    self.__visible_sprites.add(tile)
                    self.__obstacle_sprites.add(tile)
                elif col == 'o':
                    tile = Tile((x, y), 'parede_quina_direita_baixo')
                    self.__visible_sprites.add(tile)
                    self.__obstacle_sprites.add(tile)
                elif col == 'j':
                    tile = Tile((x, y), 'parede_quina_esquerda_cima')
                    self.__visible_sprites.add(tile)
                    self.__obstacle_sprites.add(tile)
                elif col == 'a':
                    tile = Tile((x, y), 'parede')
                    self.__visible_sprites.add(tile)
                    self.__obstacle_sprites.add(tile)
                elif col == 'z':
                    tile = Tile((x, y), 'parede_com_corrente')
                    self.__visible_sprites.add(tile)
                    self.__obstacle_sprites.add(tile)
                elif col == 'i':
                    tile = Tile((x, y), 'parede_com_vaso')
                    self.__visible_sprites.add(tile)
                    self.__obstacle_sprites.add(tile)
                if col == 'q':
                    tile = Tile((x, y), 'parede_vertical_direita')
                    self.__visible_sprites.add(tile)
                    self.__obstacle_sprites.add(tile)
                elif col == 'h':
                    tile = Tile((x, y), 'parede_horizontal_baixo')
                    self.__visible_sprites.add(tile)
                    self.__obstacle_sprites.add(tile)
                if col == 'y':
                    tile = Tile((x, y), 'parede_horizontal_cima')
                    self.__visible_sprites.add(tile)
                    self.__obstacle_sprites.add(tile)
                elif col == 'p':
                    self.__player = Jogador((x, y), 100)
                    self.__visible_sprites.add(self.__player)
                elif col == 'b':
                    battery = Pilha(x, y, 'tiles/pilha.png', 50)
                    self.__item_sprites.append(battery)
                    self.__visible_sprites.add(battery)
                elif col == 'l':
                    door = Door(x, y, 'tiles/porta.png')
                    self.__visible_sprites.add(door)
                    self.__obstacle_sprites.add(door)
                    self.__door = door
                    self.__item_sprites.append(door)
                elif col == 'v':
                    tile = Tile((x, y), 'barril')
                    self.__visible_sprites.add(tile)
                    self.__obstacle_sprites.add(tile)
                elif col == 'c':
                    tile = Tile((x, y), 'porta_cima')
                    self.__visible_sprites.add(tile)
                    self.__obstacle_sprites.add(tile)
                elif col == 'k':
                    key = Key(x, y, 'tiles/key.png')
                    self.__visible_sprites.add(key)
                    self.__item_sprites.append(key)
                    self.__key = key
                elif col == 'el':
                    enemy = EnemyLowDMG((x, y))
                    self.__visible_sprites.add(enemy)
                    self.__enemy_sprites.add(enemy)
                elif col == 'eh':
                    enemy = EnemyHighDMG((x, y))
                    self.__visible_sprites.add(enemy)
                    self.__enemy_sprites.add(enemy)
                elif col.endswith('-lrwpn'):
                    name, damage, shot_speed, cooldown, type = col.split('-')
                    damage, shot_speed, cooldown = int(damage), int(shot_speed), int(cooldown)
                    weapon = ProjectileWeapon(x, y, name, damage, shot_speed, cooldown)
                    self.__visible_sprites.add(weapon)
                    self.__item_sprites.append(weapon)
                elif col.endswith('-mlwpn'):
                    name, dmg, _range, cooldown, type = col.split('-')
                    dmg, _range, cooldown = int(dmg), int(_range), int(cooldown)
                    weapon = MeleeWeapon(x, y, name, dmg, _range, cooldown)
                    self.__visible_sprites.add(weapon)
                    self.__item_sprites.append(weapon)
        self.__dmg_ctrl.update_characters(self.__enemy_sprites, self.__player)

    def add_projectile(self, sprite, dmg, shot_speed):
        pos = self.__player.getPos()
        # status = self.__player.getFrameIndex()
        status = self.__player.getStatus()
        # arrumar para o index:
        if status == 'up' or status == 'up_idle':
            direction = (0, -1)
        elif status == 'down' or status == 'down_idle':
            direction = (0, 1)
        elif status == 'left' or status == 'left_idle':
            direction = (-1, 0)
        elif status == 'right' or status == 'right_idle':
            direction = (1, 0)
        else:
            return 0
        projectile = Projectile(pos, sprite, direction, dmg, shot_speed)
        self.__visible_sprites.add(projectile)
        self.__projectile_sprites.add(projectile)

    def getKey(self):
        return self.__key

    def getDoor(self):
        return self.__door

    def getPlayer(self):
        return self.__player

    def getProjectileSprites(self):
        return self.__projectile_sprites

    def getVisibleSprites(self):
        return self.__visible_sprites

    def getObstacleSprites(self):
        return self.__obstacle_sprites

    def getItemSprites(self):
        return self.__item_sprites

    def getEnemySprites(self):
        return self.__enemy_sprites

    def getHud(self):
        return self.__hud
