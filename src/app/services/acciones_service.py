from sqlalchemy.orm import Session
from app.models.accion import Accion


def obtener_acciones(db: Session, prospecto_id: int):
    acciones = (
        db.query(Accion)
        .filter(Accion.prospecto_id == prospecto_id)
        .order_by(Accion.id.asc())
        .limit(5)
        .all()
    )
    return acciones
