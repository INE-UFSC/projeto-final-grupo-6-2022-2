from pilha import Pilha
from sword import MeleeWeapon
from projectileWeapon import ProjectileWeapon

from inventoryDAO import InventoryDAO

class InventoryTranslator:
    def __init__(self):
        self.__dao = InventoryDAO()
        
    def loadInventory(self):
        item_list = [None]*9
        for item in range(9):
            code_item = self.__dao.get(item)
            if code_item == 'pilha':
                item_list[item] = Pilha(0,0, 'tiles/pilha.png', 50)
            elif code_item == 'meleeweapon':
                pass
            elif code_item == 'projectileweapon':
                pass
            elif code_item == 'none':
                pass
        
        return item_list

    def saveInventory(self, item_list):
        for pos, item in enumerate(item_list):
            print(item)
            if isinstance(item, Pilha):
                self.__dao.add('pilha', pos)
            elif isinstance(item, MeleeWeapon):
                self.__dao.add('meleeweapon', pos)
            elif isinstance(item, ProjectileWeapon):
                self.__dao.add('projectileweapon', pos)
            else:
                self.__dao.add('none', pos)