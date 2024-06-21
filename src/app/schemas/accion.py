from pydantic import BaseModel


class AccionBase(BaseModel):
    nombre: str
    descripcion: str
    icono: str
    prospecto_id: int


class AccionCreate(AccionBase):
    pass


class Accion(AccionBase):
    id: int

    class Config:
        orm_mode = True
