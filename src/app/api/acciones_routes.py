from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.db import get_db
from app.schemas.accion import Accion as AccionSchema
from app.services.acciones_service import obtener_acciones

router = APIRouter()


@router.get("/acciones/primeras/{prospecto_id}", response_model=List[AccionSchema])
def obtener_primeras_acciones_route(prospecto_id: int, db: Session = Depends(get_db)):
    acciones = obtener_acciones(db, prospecto_id)

    return acciones
