from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Producto(Base):
    __tablename__ = "productos"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    ventas = Column(Integer, nullable=False)
    inventario = relationship("Inventario", back_populates="producto", uselist=False)
    descripcion = Column(String(500)) 
