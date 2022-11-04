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

class Level:
    def __init__(self):
        
        # Pegar a tela
        self.selected_room = 0
        self.key = ''
        self.rooms = ROOMS
        self.display_surface = pygame.display.get_surface()
        self.create_map()
        # Cria grupos de sprites

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
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites], 'rock')
                elif col == 'p':
                    self.jogador = Jogador((x,y),[self.visible_sprites],self.obstacle_sprites, self.itens_sprites, [])
                elif col == 'b':
                    self.itens_sprites.append(Pilha(x,y,'tiles/pilha.png', [self.visible_sprites], 50))
                elif col == 'l':
                    door = Door(x,y, 'tiles/porta.png', [self.visible_sprites,self.obstacle_sprites])
                    self.door = door
                    self.itens_sprites.append(door)
                elif col == 'k':
                    key = Key(x,y,'tiles/key.png', [self.visible_sprites])
                    self.itens_sprites.append(key)
                    self.key = key
                elif col == 'el':
                    EnemyLowDMG((x,y), [self.visible_sprites, self.enemy_sprites], self.obstacle_sprites, self.jogador)
                elif col == 'eh':
                    EnemyHighDMG((x,y), [self.visible_sprites, self.enemy_sprites], self.obstacle_sprites, self.jogador)
        
                    
    def run(self):
        # Atualizar e desenhar sprites/jogo
        self.visible_sprites.custom_draw(self.jogador)
        self.jogador.draw()
        self.visible_sprites.update()
        self.enemy_sprites.update()
        self.chave()
        
        
    def chave(self):
        inventario = self.jogador.getInventory().getItemList()
        if self.key in inventario:
            inventario.remove(self.key)
            self.obstacle_sprites.remove(self.door)
            self.key = ''
        if self.door in inventario:
            inventario.remove(self.door)
            self.selected_room += 1
            self.create_map()
            

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        # Setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] / 2
        self.half_height = self.display_surface.get_size()[1] / 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, jogador):
        # Pegando offset
        self.offset.x = jogador.rect.centerx - self.half_width
        self.offset.y = jogador.rect.centery - self.half_height
        # Desenhando sprites
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
