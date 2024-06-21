from sqlalchemy import Column, Integer, String
from app.database.db import Base


class Accion(Base):
    __tablename__ = "accion"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(100), nullable=False)
    icono = Column(String(50), nullable=False)
    prospecto_id = Column(Integer, index=True)
