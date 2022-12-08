import pygame
from inventory import Inventory
from lanterna import Lanterna
from character import Character
from damageController import DamageController
from assetController import AssetController
from support import import_folder
from weapon import Weapon
from inventoryPickable import InventoryPickable


class Jogador(Character):
    def __init__(self, pos):
        super().__init__(100, pos, 5, AssetController().get_asset('player'))
        self.import_player_assets()
        self.__inventory = Inventory()
        self.__weapon = None
        self.tamanho = [500, 10]
        self.__light = Lanterna((self.hitbox.x, self.hitbox.y))
        self.__damage = 100

    def attack(self):
        dmg_ctrl = DamageController()
        if not self.getAttackingStatus():
            self.setAttackTimer()
            if self.__weapon is None:
                    dmg_ctrl.melee_attack(self.__damage, 100, self.get_status())
            else:
                projectile = self.__weapon.attack(self.getStatus())
                if projectile is not None:
                    projectile.setPos(self.getPos())
                return projectile

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


    def animate(self):
        animation = self.animations[self.getStatus()]
        self.setFrameIndex(self.getFrameIndex() + self.getAnimationSpeed())
        if self.getFrameIndex() >= len(animation):
            self.setFrameIndex(0)
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
    
    def loadInventory(self):
        self.__inventory = InventoryPickable().fromPickles()

    def saveInventory(self):
        InventoryPickable().toPickles(self.__inventory)

    def getLight(self):
        return self.__light

    def get_weapon(self):
        return self.__weapon
    
    def die(self):
        pass
    