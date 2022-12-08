from inventoryDAO import InventoryDAO
from abstractPickable import AbstractPickable
from item import Item

class InventoryPickable(AbstractPickable):
    def __init__(self):
        super().__init__(InventoryDAO())
        
    def fromPickles(self):
        inventory = self.getDAO().get('inventory')
       
        for item in inventory.getItemList():
            if isinstance(item, Item):
                item.setImage(True)
        
        return inventory
        
    def toPickles(self, inventory):
        for item in inventory.getItemList():
            if isinstance(item, Item):
                item.setImage(False)
                
        self.getDAO().add(inventory)