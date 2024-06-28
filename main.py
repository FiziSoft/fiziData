from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import TruthDare, TruthDareCreate, TruthDareResponse, SessionLocal, Base, engine
import models

app = FastAPI()

# Создание всех таблиц
Base.metadata.create_all(bind=engine)

# Зависимость, создающая сессию базы данных для каждого запроса
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD функции
def get_truthdares(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TruthDare).offset(skip).limit(limit).all()

def create_truthdare(db: Session, truthdare: TruthDareCreate):
    db_truthdare = TruthDare(**truthdare.dict())
    db.add(db_truthdare)
    db.commit()
    db.refresh(db_truthdare)
    return db_truthdare

@app.post("/truthdares/", response_model=TruthDareResponse)
def create_truthdare_endpoint(truthdare: TruthDareCreate, db: Session = Depends(get_db)):
    return create_truthdare(db=db, truthdare=truthdare)

@app.get("/truthdares/", response_model=list[TruthDareResponse])
def read_truthdares(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    truthdares = get_truthdares(db, skip=skip, limit=limit)
    return truthdares
