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
from debug import debug


class Jogador(Character):
    def __init__(self, pos, health):
        super().__init__(100, pos, 5, 'tiles/player.png')
        self.import_player_assets()
        self.__inventory = Inventory()
        self.__weapon = None
        self.tamanho = [health*5,10]
        self.__light = Lanterna((self.hitbox.x, self.hitbox.y))
        self.__damage = 100


    # EXEMPLO:
    def attack(self):
        dmg_ctrl = DamageController()
        if not self.getAttackingStatus():
            self.setAttackTimer()
            if self.__weapon is None:
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
    

    #Se for tomar dano passar vida como parametro negativo
    def tomar_Dano_ou_curar_vida(self, vida):
        if self.getHealth() + vida > 100:
            self.setHealth(100)
        else:
            self.setHealth(self.getHealth() + vida)
        if self.getHealth() <= 0:
            self.die()
        elif self.getHealth() > 100:
            self.setHealth(100)
            
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
        if self.__weapon is not None:
            self.cooldowns(self.__weapon.getAttackCooldown())
        else:
            self.cooldowns()
        self.get_status()
        self.animate()
        self.__light.update()

    def getLight(self):
        return self.__light

    def get_weapon(self):
        return self.__weapon
    
    def die(self):
        pass
    