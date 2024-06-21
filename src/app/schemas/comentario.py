from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ComentarioBase(BaseModel):
    comentario_descripcion: Optional[str]
    detalle_comentario: Optional[str]
    prospecto_id: Optional[int]
    observacion: Optional[str]
    usuario_creacion_id: Optional[int]
    fecha_creacion: Optional[datetime]
    usuario_modificacion_id: Optional[int]
    fecha_modificacion: Optional[datetime]


class ComentarioCreate(ComentarioBase):
    pass


class ComentarioUpdate(ComentarioBase):
    pass


class Comentario(ComentarioBase):
    comentario_id: int

    class Config:
        orm_mode = True
