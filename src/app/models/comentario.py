from sqlalchemy import Column, Integer, String, Text, DateTime
from app.database.db import Base


class Comentario(Base):
    __tablename__ = "comentarios"
    comentario_id = Column(Integer, primary_key=True, index=True)
    comentario_descripcion = Column(String(100), nullable=True)
    detalle_comentario = Column(Text, nullable=True)
    prospecto_id = Column(Integer, index=True)
    observacion = Column(String(255), nullable=True)
    usuario_creacion_id = Column(Integer, nullable=True)
    fecha_creacion = Column(DateTime, nullable=True)
    usuario_modificacion_id = Column(Integer, nullable=True)
    fecha_modificacion = Column(DateTime, nullable=True)
