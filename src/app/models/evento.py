from sqlalchemy import Column, Integer, BigInteger, Text, DateTime
from app.database.db import Base


class Evento(Base):
    __tablename__ = "evento"
    evento_id = Column(BigInteger, primary_key=True, index=True)
    evento_tipo_id = Column(BigInteger, nullable=True)
    campo1 = Column(Text, nullable=True)
    campo2 = Column(Integer, nullable=True)
    fecha_inicio = Column(DateTime, nullable=True)
    fecha_fin = Column(DateTime, nullable=True)
    fecha_creacion = Column(DateTime, nullable=True)
    fecha_modificacion = Column(DateTime, nullable=True)
    prospecto_id = Column(Integer, nullable=True)
    otro_id = Column(Integer, nullable=True)
    otro_id2 = Column(Integer, nullable=True)
    otro_id3 = Column(Integer, nullable=True)
    fecha_alguna = Column(DateTime, nullable=True)
    flag1 = Column(Integer, nullable=True)
    campo3 = Column(Text, nullable=True)
    campo4 = Column(Text, nullable=True)
    fecha_alguna2 = Column(DateTime, nullable=True)
    otro_id4 = Column(Integer, nullable=True)
    fecha_alguna3 = Column(DateTime, nullable=True)
    flag2 = Column(Integer, nullable=True)
    flag3 = Column(Integer, nullable=True)
