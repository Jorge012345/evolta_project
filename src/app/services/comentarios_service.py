from sqlalchemy.orm import Session
from app.models.comentario import Comentario
from app.schemas.comentario import ComentarioCreate, ComentarioUpdate
from fastapi import UploadFile
import csv
from io import StringIO
from datetime import datetime
from app.schemas.prospecto import ProspectoCreate


def obtener_ultimo_comentario(db: Session, prospecto_id: int):
    return (
        db.query(Comentario)
        .filter(Comentario.prospecto_id == prospecto_id)
        .order_by(Comentario.fecha_creacion.desc())
        .first()
    )


def actualizar_comentario(db: Session, prospecto_id: int, comentario: ComentarioUpdate):
    db_comentario = (
        db.query(Comentario).filter(Comentario.prospecto_id == prospecto_id).first()
    )
    comentario.fecha_creacion = db_comentario.fecha_creacion
    comentario.prospecto_id = db_comentario.prospecto_id
    comentario.fecha_modificacion = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
    if db_comentario:
        for key, value in comentario.dict().items():
            setattr(db_comentario, key, value)
        db.commit()
        db.refresh(db_comentario)
    return db_comentario


def cargar_comentarios_csv(db: Session, edt: UploadFile):
    content = edt.file.read().decode("utf-8")
    reader = csv.DictReader(StringIO(content))
    for row in reader:
        comentario_data = ComentarioCreate(
            comentario_id=int(row["comentario_id"]),
            comentario_descripcion=row["comentario_descripcion"],
            detalle_comentario=row["detalle_comentario"],
            prospecto_id=int(row["prospecto_id"]),
            observacion=row["observacion"],
            usuario_creacion_id=int(row["usuario_creacion_id"]),
            fecha_creacion=row["fecha_creacion"],
            usuario_modificacion_id=int(row["usuario_modificacion_id"]),
            fecha_modificacion=row["fecha_modificacion"],
        )
        db_comentario = Comentario(**comentario_data.dict())
        db.add(db_comentario)
    db.commit()
    return {"message": "Comentarios cargados correctamente"}
