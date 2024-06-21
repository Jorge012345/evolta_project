from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class EventoBase(BaseModel):
    evento_id: Optional[int]
    evento_tipo_id: Optional[int]
    campo1: Optional[str]
    campo2: Optional[int]
    fecha_inicio: Optional[datetime]
    fecha_fin: Optional[datetime]
    fecha_creacion: Optional[datetime]
    fecha_modificacion: Optional[datetime]
    prospecto_id: Optional[int]
    otro_id: Optional[int]
    otro_id2: Optional[int]
    otro_id3: Optional[int]
    fecha_alguna: Optional[datetime]
    flag1: Optional[int]
    campo3: Optional[str]
    campo4: Optional[str]
    fecha_alguna2: Optional[datetime]
    otro_id4: Optional[int]
    fecha_alguna3: Optional[datetime]
    flag2: Optional[int]
    flag3: Optional[int]


class EventoCreate(EventoBase):
    pass


class Evento(EventoBase):
    evento_id: int

    class Config:
        orm_mode = True
