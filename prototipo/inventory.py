import pygame
from item import Item

class Inventory:
    def __init__(self):
        self.__item_list = [None]*9
    
    def getItemList(self):
        return self.__item_list
    
    def use_item(self, id):
        self.__item_list[id-1].usar()
        self.__item_list.pop(id-1)
    
    def add_item(self, item):
        for pos,item in enumerate(self.__item_list):
            if item == None:
                self.__item_list[pos] = item
                return True
        return False
