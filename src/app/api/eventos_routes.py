from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.schemas.evento import Evento as EventoSchema, EventoCreate
from app.services.eventos_service import crear_evento

router = APIRouter()


@router.post("/eventos/registrar", response_model=EventoSchema, status_code=201)
def registrar_evento(evento: EventoCreate, db: Session = Depends(get_db)):
    return crear_evento(db, evento)
