import pygame
from inventory import Inventory
from lanterna import Lanterna
from settings import *
from support import import_folder

class Jogador(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, itens_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('tiles/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)
        # Grapihcs setup
        self.import_player_assets()
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.obstacle_sprites = obstacle_sprites
        # Movimento
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = 0

        self.itens_sprites = itens_sprites

        self.__inventory = Inventory()
        #self.__lanterna = Lanterna()


    def import_player_assets(self):
        character_path = 'graphics/player/'
        self.animations = {'up': [],'down': [],'left': [],'right': [],
            'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
            'right_attack':[],'left_attack':[],'up_attack':[],'down_attack':[]}
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
        
        
    def getInventory(self):
        return self.__inventory

    def input(self):
        # Input de movimento
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0
            
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0
        
        # Input de inventário        
        if keys[pygame.K_1]:
            self.__inventory.use_item(1)
        if keys[pygame.K_2]:
            self.__inventory.use_item(2)
        if keys[pygame.K_3]:
            self.__inventory.use_item(3)
        if keys[pygame.K_4]:
            self.__inventory.use_item(4)
        if keys[pygame.K_5]:
            self.__inventory.use_item(5)
        if keys[pygame.K_6]:
            self.__inventory.use_item(6)
        if keys[pygame.K_7]:
            self.__inventory.use_item(7)
        if keys[pygame.K_8]:
            self.__inventory.use_item(8)
        if keys[pygame.K_9]:
            self.__inventory.use_item(9)
        
        #Input de ataques
        if keys[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            print('ataque')
            
    def get_status(self):
        #Idle status
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'
        #Attack status
        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle','_attack')
                else:
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack','')

    #classe Character(ABC)e
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction.normalize()
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def draw(self):
        surface = pygame.display.get_surface()
        self.__inventory.draw(surface)
        #self.__lanterna.draw(self.hitbox, surface)

    #classe Character(ABC)
    def animate(self):
        animation = self.animations[self.status]
        #Loop de animação por frame
        self.frame_index += self.animation_speed
        # Verifica se o frame atual é maior que o número de frames
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        # Setando o frame atual
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)
        
    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)
    
    #classe Character(ABC)
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
                        self.itens_sprites.remove(item)
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
                        self.itens_sprites.remove(item)
                        item.exclui()
    
    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time > self.attack_cooldown:
                self.attacking = False
