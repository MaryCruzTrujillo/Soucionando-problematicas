from app.repositories.inventory_repository import InventoryRepository

class InventoryService:
    def __init__(self):
        self.repository = InventoryRepository()

    def get_all_inventory(self):
        return self.repository.get_inventory()

    def get_inventory_by_product(self, product_id):
        return self.repository.get_by_product_id(product_id)

    def update_inventory_stock(self, product_id, new_stock):
        return self.repository.update_stock(product_id, new_stock)

    def check_inventory_restock(self, product_id):
        return self.repository.check_restock(product_id)
