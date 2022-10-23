import pygame
from settings import *
from tile import Tile
from jogador import Jogador
from item import *


class Level:
    def __init__(self):
        
        # Pegar a tela
        self.selected_room = 0
        self.rooms = [ROOM1, ROOM2]
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.itens_sprites = []
        self.display_surface = pygame.display.get_surface()
        self.create_map()
        # Cria grupos de sprites

    def create_map(self):
        for row_index, row in enumerate(self.rooms[self.selected_room]):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
                elif col == 'p':
                    self.jogador = Jogador((x,y),[self.visible_sprites],self.obstacle_sprites, self.itens_sprites)
                elif col == 'b':
                    self.itens_sprites.append(Item(x,y,'tiles/pilha.png', [self.visible_sprites]))
        
    def run(self):
        # Atualizar e desenhar sprites/jogo
        self.visible_sprites.custom_draw(self.jogador)
        self.jogador.draw()
        self.visible_sprites.update()

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
