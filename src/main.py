from fastapi import FastAPI, Request, Response, Depends
from sqlalchemy.orm import Session
from app.database.db import engine, Base, SessionLocal
from app.api.acciones_routes import router as acciones_router
from app.api.comentarios_routes import router as comentarios_router
from app.api.eventos_routes import router as eventos_router

# Crear todas las tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir las rutas
app.include_router(acciones_router, prefix="/api")
app.include_router(comentarios_router, prefix="/api")
app.include_router(eventos_router, prefix="/api")


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


def get_db(request: Request):
    return request.state.db


@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
