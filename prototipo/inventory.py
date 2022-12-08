import pygame
from item import Item
from settings import HEIGTH, WIDTH
from assetController import AssetController


class Inventory():
    def __init__(self):
        self.__item_list = [None]*9
        

    def setImage(self, load: bool):
        if not load:
            self.__image = None
        else:
            self.__image = AssetController().get_asset('inventario')

        for item in self.__item_list:
            if isinstance(item, Item):
                item.setImage(load)
    
    def getImage(self):
        return self.__image

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
