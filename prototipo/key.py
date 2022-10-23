import pygame
from item import Item

class Key(Item):
    def  __init__(self, x, y, sprite,grupo):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(x, y, sprite, grupo)
    
    def usar(self):
        print("usado chave")
        self.kill()
    
    def exclui(self):
        
        self.kill()
