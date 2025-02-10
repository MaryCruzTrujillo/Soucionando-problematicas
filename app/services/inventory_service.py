from app.models.inventory import Inventario
from app.database import SessionLocal  # IMPORTA LA SESIÓN CORRECTAMENTE
from app.repositories.inventory_repository import InventoryRepository

class InventoryService:
    def __init__(self):
        self.repository = InventoryRepository()

    def get_all_inventory(self):
        return self.repository.get_inventory()

    def get_inventory_by_product(self, product_id):
        return self.repository.get_by_product_id(product_id)

    def update_inventory(self, product_id, new_data):
        return self.repository.update_inventory(product_id, new_data)

    def delete_inventory(self, product_id):
        return self.repository.delete_inventory(product_id)

    def check_inventory_restock(self, product_id):
        return self.repository.check_restock(product_id)

    def create_inventory(self, data):
        """ Crea un nuevo registro de inventario """
        db = SessionLocal()  # ASEGURA QUE SE CREA LA SESIÓN CORRECTAMENTE
        try:
            new_inventory = Inventario(
                producto_id=data["producto_id"],
                stock_actual=data["stock_actual"],
                demanda_proyectada=data["demanda_proyectada"],
                nivel_reabastecimiento=data.get("nivel_reabastecimiento", 50),  # DEFAULT 50
                costo_mantenimiento=data["costo_mantenimiento"]
            )
            db.add(new_inventory)
            db.commit()
            db.refresh(new_inventory)
            return new_inventory
        except Exception as e:
            db.rollback()
            print(f"❌ Error al crear el inventario: {e}")
            return None
        finally:
            db.close()  # CIERRA LA CONEXIÓN
