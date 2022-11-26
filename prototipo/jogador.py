import pygame
from inventory import Inventory
from lanterna import Lanterna
from character import Character
from damageController import DamageController
from settings import *
from support import import_folder
from weapon import Weapon
from math import sqrt
from hud import Hud


class Jogador(Character):
    def __init__(self, pos, obstacle_sprites, itens_sprites, enemies):
        super().__init__(110, pos, 5, 'tiles/player.png', obstacle_sprites)
        self.import_player_assets()

        self.__enemies = enemies

        self.itens_sprites = itens_sprites
        self.__hud = Hud()
        self.__inventory = Inventory()
        self.__weapon = None
        self.__light = Lanterna((self.hitbox.x, self.hitbox.y))
        self.__damage = 100

    # EXEMPLO:
    def attack(self, receiver=None):
        dmg_ctrl = DamageController()
        if self.__weapon == None:
            dmg_ctrl.meele_attack(self.__damage, 1000)
        else:
            msg = self.__weapon.attack()
            return msg

    def setWeapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.__weapon = weapon

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
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.setDirectionY(-1)
            self.setStatus('up')
        elif keys[pygame.K_DOWN] or keys[pygame.K_s] :
            self.setDirectionY(1)
            self.setStatus('down')
        else:
            self.setDirectionY(0)
            
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.setDirectionX(1)
            self.setStatus('right')
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.setDirectionX(-1)
            self.setStatus('left')
        else:
            self.setDirectionX(0)
        
        # Input de inventário        
        if keys[pygame.K_1]:
            self.__inventory.use_item(1, self)
        elif keys[pygame.K_2]:
            self.__inventory.use_item(2, self)
        elif keys[pygame.K_3]:
            self.__inventory.use_item(3, self)
        elif keys[pygame.K_4]:
            self.__inventory.use_item(4, self)
        elif keys[pygame.K_5]:
            self.__inventory.use_item(5, self)
        elif keys[pygame.K_6]:
            self.__inventory.use_item(6, self)
        elif keys[pygame.K_7]:
            self.__inventory.use_item(7, self)
        elif keys[pygame.K_8]:
            self.__inventory.use_item(8, self)
        elif keys[pygame.K_9]:
            self.__inventory.use_item(9, self)
            
        if keys[pygame.K_LCTRL]:
            self.__light.setStatus()

        
        #Input de ataques
        if keys[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            self.attack()   
            
    def get_status(self):
        #Idle status
        if self.getDirectionX() == 0 and self.getDirectionY() == 0:
            if not 'idle' in self.getStatus() and not 'attack' in self.getStatus():
                self.setStatus(self.getStatus() + '_idle')
        #Attack status
        if self.attacking:
            self.setDirectionX(0)
            self.setDirectionY(0)
            if not 'attack' in self.getStatus():
                if 'idle' in self.getStatus():
                    self.setStatus(self.getStatus().replace('_idle','_attack'))
                else:
                    self.setStatus(self.getStatus() + '_attack')
        else:
            if 'attack' in self.getStatus():
                self.setStatus(self.getStatus().replace('_attack',''))


        
                
        
    def draw(self):
        surface = pygame.display.get_surface()
        self.__light.draw(surface)
        self.__inventory.draw(surface)

        

    #classe Character(ABC)
    def animate(self):
        animation = self.animations[self.getStatus()]
        #Loop de animação por frame
        self.setFrameIndex(self.getFrameIndex() + self.getAnimationSpeed())
        # Verifica se o frame atual é maior que o número de frames
        if self.getFrameIndex() >= len(animation):
            self.setFrameIndex(0)
        
        # Setando o frame atual
        self.image = animation[int(self.getFrameIndex())]
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
            for sprite in self.getObstacleSprites():                
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.getDirectionX() > 0: # Se mover para a direita
                        self.hitbox.right = sprite.hitbox.left
                    if self.getDirectionX() < 0: # Se mover para a esquerda
                        self.hitbox.left = sprite.hitbox.right
            
            
            for item in self.itens_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    add = self.__inventory.add_item(item)
                    if add:
                        self.itens_sprites.remove(item)
                        item.exclui()

        if direction == 'vertical':
            for sprite in self.getObstacleSprites():
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.getDirectionY() > 0: # Se mover para baixo
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.getDirectionY() < 0: # Se mover para cima
                        self.hitbox.top = sprite.hitbox.bottom
            
            for item in self.itens_sprites:
                if item.hitbox.colliderect(self.hitbox):
                    add = self.__inventory.add_item(item)
                    if add:
                        self.itens_sprites.remove(item)
                        item.exclui()

    def enemy_kill(self, enemy):
        self.__enemies.remove(enemy)

    def getLight(self):
        return self.__light

    def get_weapon(self):
        return self.__weapon
    
    def die(self):
        pass
    