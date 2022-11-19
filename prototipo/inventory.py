import pygame
from item import Item
from settings import HEIGTH, WIDTH


class Inventory():
    def __init__(self):
        self.__item_list = [None]*9
        self.image = pygame.image.load('tiles/inventário.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.x = (WIDTH-self.rect[2])/2
        self.y = HEIGTH-70
    
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        valor = self.rect[2]/9
        for pos,item in enumerate(self.__item_list):
            if isinstance(item, Item):
                item.draw(self.x, self.y, valor, pos, surface)
    
    def getItemList(self):
        return self.__item_list
    
    def use_item(self, id, jogador):
        if isinstance(self.__item_list[id-1], Item):
            self.__item_list[id-1].use(jogador)
            self.__item_list[id-1] = None
    
    def add_item(self, item):
        for pos, espaco in enumerate(self.__item_list):
            if espaco == None:
                self.__item_list[pos] = item
                return True
        return False
