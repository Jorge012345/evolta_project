from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProspectoBase(BaseModel):
    prospecto_id: Optional[int]
    prospecto_tipo_id: Optional[int]
    prospecto_descripcion: Optional[str]
    campo1: Optional[int]
    fecha_inicio: Optional[datetime]
    fecha_fin: Optional[datetime]
    fecha_creacion: Optional[datetime]
    fecha_modificacion: Optional[datetime]
    evento_id: Optional[int]
    otro_id: Optional[int]
    otro_id2: Optional[int]
    otro_id3: Optional[int]
    fecha_alguna: Optional[datetime]
    flag1: Optional[int]
    campo2: Optional[str]
    campo3: Optional[str]
    fecha_alguna2: Optional[datetime]
    otro_id4: Optional[int]
    fecha_alguna3: Optional[datetime]
    flag2: Optional[int]
    flag3: Optional[int]


class ProspectoCreate(ProspectoBase):
    pass


class ProspectoUpdate(ProspectoBase):
    pass


class Prospecto(ProspectoBase):
    prospecto_id: int

    class Config:
        orm_mode = True
