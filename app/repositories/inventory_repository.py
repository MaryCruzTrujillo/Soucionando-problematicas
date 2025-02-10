from app.models.inventory import Inventario
from app.database import SessionLocal

class InventoryRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get_inventory(self):
        return self.db.query(Inventario).all()

    def get_by_product_id(self, product_id):
        return self.db.query(Inventario).filter(Inventario.producto_id == product_id).first()

    def update_stock(self, product_id, new_stock):
        inventory = self.get_by_product_id(product_id)
        if not inventory:
            return None
        inventory.stock_actual = new_stock
        self.db.commit()
        return inventory

    def check_restock(self, product_id):
        inventory = self.get_by_product_id(product_id)
        if inventory and inventory.stock_actual <= inventory.nivel_reabastecimiento:
            return True  # Necesita reabastecimiento
        return False
