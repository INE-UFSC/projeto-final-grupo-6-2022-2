import pygame
from item import Item

class Inventory():
    def __init__(self):
        self.__item_list = [None]*9
    
    def draw(self, surface):
        self.image = pygame.image.load('prototipo/tiles/inventário.png').convert_alpha()
        surface.blit(self.image, (500,650))
        
        for pos,item in enumerate(self.__item_list):
            if isinstance(item, Item):
                item.draw(500, 650, pos, surface)
    
    def getItemList(self):
        return self.__item_list
    
    def use_item(self, id):
        if isinstance(self.__item_list[id-1], Item):
            self.__item_list[id-1].usar()
            self.__item_list[id-1] = None
    
    def add_item(self, item):
        for pos, espaco in enumerate(self.__item_list):
            if espaco == None:
                self.__item_list[pos] = item
                return True
        return False
