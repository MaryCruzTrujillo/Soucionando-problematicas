from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Inventario(Base):
    __tablename__ = "inventarios"
    
    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    stock_actual = Column(Integer, nullable=False)
    demanda_proyectada = Column(Integer, nullable=False)
    nivel_reabastecimiento = Column(Integer, nullable=False, default=50)
    costo_mantenimiento = Column(Float, nullable=False)

    producto = relationship("Producto", back_populates="inventario")
