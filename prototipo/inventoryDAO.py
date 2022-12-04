from DAO import DAO

class InventoryDAO(DAO):
    def __init__(self):
        super().__init__('inventory.pkl')
        
    def add(self, item_type: str, slot: int):
        if isinstance(item_type, str) and isinstance(slot, int):
            super().add(f'iteminventory{slot}', item_type)

    def get(self, key):
        return super().get(f'iteminventory{key}')