from sqlalchemy.orm import Session
from app.models.evento import Evento
from app.schemas.evento import EventoCreate
from datetime import datetime


def crear_evento(db: Session, evento: EventoCreate):
    evento.fecha_creacion = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
    evento.fecha_modificacion = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
    db_evento = Evento(**evento.dict())
    db.add(db_evento)
    db.commit()
    db.refresh(db_evento)
    return db_evento
