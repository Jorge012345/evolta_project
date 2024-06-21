from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.schemas.comentario import (
    Comentario as ComentarioSchema,
    ComentarioCreate,
    ComentarioUpdate,
)
from app.services.comentarios_service import (
    obtener_ultimo_comentario,
    actualizar_comentario,
    cargar_comentarios_csv,
)
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/comentarios/ultimo/{prospecto_id}", response_model=ComentarioSchema)
def obtener_ultimo_comentario_route(prospecto_id: int, db: Session = Depends(get_db)):
    comentario = obtener_ultimo_comentario(db, prospecto_id)
    if not comentario:
        raise HTTPException(status_code=404, detail="Comentario not found")
    return comentario


@router.put("/comentarios/actualizar/{prospecto_id}", response_model=ComentarioSchema)
def actualizar_comentario_route(
    prospecto_id: int, comentario: ComentarioUpdate, db: Session = Depends(get_db)
):
    comentario = actualizar_comentario(db, prospecto_id, comentario)
    if not comentario:
        raise HTTPException(status_code=404, detail="Comentario not found")
    return comentario


@router.post("/comentarios/cargar_csv", status_code=201)
def cargar_comentarios_csv_route(
    edt: UploadFile = File(...), db: Session = Depends(get_db)
):
    try:
        cargar_comentarios_csv(db, edt)
        return JSONResponse(
            status_code=201, content={"message": "Comentarios cargados correctamente"}
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
