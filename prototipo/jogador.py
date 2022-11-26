import pygame
from inventory import Inventory
from lanterna import Lanterna
from character import Character
from damageController import DamageController
from support import import_folder
from weapon import Weapon
from hud import Hud
from debug import debug

class Jogador(Character):
    def __init__(self, pos, obstacle_sprites, itens_sprites, enemies, health):
        super().__init__(100, pos, 5, 'tiles/player.png', obstacle_sprites)
        self.import_player_assets()
        self.__enemies = enemies
        self.itens_sprites = itens_sprites
        self.__inventory = Inventory()
        self.__weapon = None
        self.tamanho = [health*5,10]
        self.__light = Lanterna((self.hitbox.x, self.hitbox.y))
        self.__damage = 100


    # EXEMPLO:
    def attack(self):
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
    def tomar_Dano_ou_curar_vida(self, vida):
        self.setHealth(self.getHealth + vida)
    def input(self):
        # Input de movimento
        # Se apertar J diminui a vida do player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_j]:
            self.setHealth(self.getHealth() - 1)
            print(self.getHealth())
        if keys[pygame.K_k]:
            self.setHealth(self.getHealth() + 1)
            print(self.getHealth())
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
        if self.getAttackingStatus():
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


    def animate(self):
        animation = self.animations[self.getStatus()]
        #Loop de animação por frame
	@@ -146,6 +154,7 @@ def animate(self):
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def update(self):
        self.cooldowns()
        self.get_status()
        self.animate()
        
    
