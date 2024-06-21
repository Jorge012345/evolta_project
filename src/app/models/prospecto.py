from sqlalchemy import Column, Integer, BigInteger, Text, DateTime
from app.database.db import Base


class Prospecto(Base):
    __tablename__ = "prospectos"
    prospecto_id = Column(BigInteger, primary_key=True, index=True)
    prospecto_tipo_id = Column(BigInteger, nullable=True)
    prospecto_descripcion = Column(Text, nullable=True)
    campo1 = Column(Integer, nullable=True)
    fecha_inicio = Column(DateTime, nullable=True)
    fecha_fin = Column(DateTime, nullable=True)
    fecha_creacion = Column(DateTime, nullable=True)
    fecha_modificacion = Column(DateTime, nullable=True)
    evento_id = Column(Integer, nullable=True)
    otro_id = Column(Integer, nullable=True)
    otro_id2 = Column(Integer, nullable=True)
    otro_id3 = Column(Integer, nullable=True)
    fecha_alguna = Column(DateTime, nullable=True)
    flag1 = Column(Integer, nullable=True)
    campo2 = Column(Text, nullable=True)
    campo3 = Column(Text, nullable=True)
    fecha_alguna2 = Column(DateTime, nullable=True)
    otro_id4 = Column(Integer, nullable=True)
    fecha_alguna3 = Column(DateTime, nullable=True)
    flag2 = Column(Integer, nullable=True)
    flag3 = Column(Integer, nullable=True)
