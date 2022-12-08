from DAO import DAO

class InventoryDAO(DAO):
    def __init__(self):
        super().__init__('inventory.pkl')
        
    def add(self, inventory):
        super().add(f'inventory', inventory)

    def get(self, key):
        return super().get(f'inventory')