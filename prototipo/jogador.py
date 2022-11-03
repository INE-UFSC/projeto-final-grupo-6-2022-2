import pygame
from inventory import Inventory
from lanterna import Lanterna
from character import Character
from settings import *
from support import import_folder

class Jogador(Character):
    def __init__(self, pos, groups, obstacle_sprites, itens_sprites):
        super().__init__(30,pos, 5, 'tiles/player.png', groups, obstacle_sprites)
        self.import_player_assets()

        self.itens_sprites = itens_sprites

        self.__inventory = Inventory()
        self.__light = Lanterna((self.hitbox.x, self.hitbox.y))
        self.__damage = 100

    def attack(self, enemy):
        enemy.receiveDamage(self.__damage)

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
            self.__direction.y = -1
            self.__status = 'up'
        elif keys[pygame.K_DOWN]:
            self.__direction.y = 1
            self.__status = 'down'
        else:
            self.__direction.y = 0
            
        if keys[pygame.K_RIGHT]:
            self.__direction.x = 1
            self.__status = 'right'
        elif keys[pygame.K_LEFT]:
            self.__direction.x = -1
            self.__status = 'left'
        else:
            self.__direction.x = 0
        
        # Input de inventário        
        if keys[pygame.K_1]:
            self.__inventory.use_item(1)
        elif keys[pygame.K_2]:
            self.__inventory.use_item(2)
        elif keys[pygame.K_3]:
            self.__inventory.use_item(3)
        elif keys[pygame.K_4]:
            self.__inventory.use_item(4)
        elif keys[pygame.K_5]:
            self.__inventory.use_item(5)
        elif keys[pygame.K_6]:
            self.__inventory.use_item(6)
        elif keys[pygame.K_7]:
            self.__inventory.use_item(7)
        elif keys[pygame.K_8]:
            self.__inventory.use_item(8)
        elif keys[pygame.K_9]:
            self.__inventory.use_item(9)
            
        if keys[pygame.K_LCTRL]:
            self.__light.setStatus()
        
        #Input de ataques
        if keys[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            self.attack()   
            
    def get_status(self):
        #Idle status
        if self.__direction.x == 0 and self.__direction.y == 0:
            if not 'idle' in self.__status and not 'attack' in self.__status:
                self.__status = self.__status + '_idle'
        #Attack status
        if self.attacking:
            self.__direction.x = 0
            self.__direction.y = 0
            if not 'attack' in self.__status:
                if 'idle' in self.__status:
                    self.__status = self.__status.replace('_idle','_attack')
                else:
                    self.__status = self.__status + '_attack'
        else:
            if 'attack' in self.__status:
                self.__status = self.__status.replace('_attack','')

    def draw(self):
        surface = pygame.display.get_surface()
        self.__light.draw(surface)
        self.__inventory.draw(surface)
        

    #classe Character(ABC)
    def animate(self):
        animation = self.animations[self.__status]
        #Loop de animação por frame
        self.__frame_index += self.__animation_speed
        # Verifica se o frame atual é maior que o número de frames
        if self.__frame_index >= len(animation):
            self.__frame_index = 0
        
        # Setando o frame atual
        self.image = animation[int(self.__frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)
        
    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.__light.update()
        self.move(self.getSpeed())
    
    #classe Character(ABC)
    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.__obstacle_sprites:                
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.__direction.x > 0: # Se mover para a direita
                        self.hitbox.right = sprite.hitbox.left
                    if self.__direction.x < 0: # Se mover para a esquerda
                        self.hitbox.left = sprite.hitbox.right
            
            
            for item in self.itens_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    add = self.__inventory.add_item(item)
                    if add:
                        self.itens_sprites.remove(item)
                        item.exclui()

        if direction == 'vertical':
            for sprite in self.__obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.__direction.y > 0: # Se mover para baixo
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.__direction.y < 0: # Se mover para cima
                        self.hitbox.top = sprite.hitbox.bottom
            
            for item in self.itens_sprites:
                if item.hitbox.colliderect(self.hitbox):
                    add = self.__inventory.add_item(item)
                    if add:
                        self.itens_sprites.remove(item)
                        item.exclui()

    def getLight(self):
        return self.__light
    
    def die(self):
        pass
    