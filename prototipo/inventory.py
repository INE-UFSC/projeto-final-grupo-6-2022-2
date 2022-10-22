import pygame
from item import Item

class Inventory:
    def __init__(self):
        self.__item_list = [None]*9
    
    def getItemList(self):
        return self.__item_list
    
    def use_item(self, id):
        if isinstance(self.__item_list[id-1], Item):
            self.__item_list[id-1].usar()
            print(self.__item_list)
            self.__item_list[id-1] = None
            print(self.__item_list)
    
    def add_item(self, item):
        for pos, espaco in enumerate(self.__item_list):
            if espaco == None:
                self.__item_list[pos] = item
                return True
        return False
