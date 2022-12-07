import pygame
from item import Item
from settings import HEIGTH, WIDTH


class Inventory():
    def __init__(self):
        self.__item_list = [None]*9
        self.__image = pygame.image.load('tiles/inventario.png').convert_alpha()
        self.__rect = self.__image.get_rect()
        self.__x = (WIDTH-self.__rect[2])/2
        self.__y = HEIGTH-70
    
    def draw(self, surface):
        surface.blit(self.__image, (self.__x, self.__y))
        valor = self.__rect[2]/9
        for pos,item in enumerate(self.__item_list):
            if isinstance(item, Item):
                item.draw(self.__x, self.__y, valor, pos, surface)
    
    def setItemList(self, item_list):
        self.__item_list = item_list
    
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
