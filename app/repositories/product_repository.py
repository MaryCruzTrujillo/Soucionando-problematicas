from app.models.product import Producto
from app.database import SessionLocal

class ProductRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get_all(self):
        return self.db.query(Producto).all()

    def get_by_id(self, product_id):
        return self.db.query(Producto).filter(Producto.id == product_id).first()

    def create(self, product_data):
        # Verifica si product_data es una lista y extrae el primer elemento
        if isinstance(product_data, list):
            product_data = product_data[0]  # Tomar el primer elemento si es una lista

        if not isinstance(product_data, dict):
            raise TypeError("product_data debe ser un diccionario")

        producto = Producto(**product_data)
        self.db.add(producto)
        self.db.commit()
        self.db.refresh(producto)
        return producto


    def update(self, product_id, product_data):
        producto = self.get_by_id(product_id)
        if not producto:
            return None
        for key, value in product_data.items():
            setattr(producto, key, value)
        self.db.commit()
        return producto

    def delete(self, product_id):
        producto = self.get_by_id(product_id)
        if producto:
            self.db.delete(producto)
            self.db.commit()
            return True
        return False
