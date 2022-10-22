import pygame
from inventory import Inventory
from settings import *

class Jogador(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, itens_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('prototipo/tiles/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)

        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.obstacle_sprites = obstacle_sprites
        self.itens_sprites = itens_sprites

        self.__inventory = Inventory()
        
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction.normalize()
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

        

    def update(self):
        self.input()
        self.move(self.speed)
    
    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # Se mover para a direita
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # Se mover para a esquerda
                        self.hitbox.left = sprite.hitbox.right
            
            for item in self.itens_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    add = self.__inventory.add_item(item)
                    if add:
                        item.exclui()
        
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # Se mover para baixo
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # Se mover para cima
                        self.hitbox.top = sprite.hitbox.bottom
            
            for item in self.itens_sprites:
                if item.hitbox.colliderect(self.hitbox):
                    add = self.__inventory.add_item(item)
                    if add:
                        item.exclui()
    