import pygame
from item import Item
from sound import Sound

class Key(Item):
    def  __init__(self, x, y, sprite):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(x, y, sprite)
        #self.__som = Sound('key')
    
    def use(self):
        print("usado chave")
        self.kill()
    
    def exclui(self):
        #self.__som.play()        
        self.kill()
