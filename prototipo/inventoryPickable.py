from inventoryDAO import InventoryDAO
from abstractPickable import AbstractPickable

class InventoryPickable(AbstractPickable):
    def __init__(self):
        super().__init__(InventoryDAO())
        
    def fromPickles(self):
        inventory = self.getDAO().get('inventory')
        inventory.setImage(True)
        return inventory
        
    def toPickles(self, inventory):
        inventory.setImage(False)
        self.getDAO().add(inventory)