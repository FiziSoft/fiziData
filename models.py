from sqlalchemy import Column, Integer, String, Boolean, Enum, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from enum import Enum as PyEnum

DATABASE_URL = "postgresql://fizi:1234@localhost:5432/fizi_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class CategoryEnum(PyEnum):
    under_18 = "до 18"
    eighteen_plus = "18+"
    twenty_one_plus = "21+"

class TruthDare(Base):
    __tablename__ = "truthdares"

    id = Column(Integer, primary_key=True, index=True)
    body = Column(String, index=True)
    isTruth = Column(Boolean, default=True)
    isBoy = Column(Boolean, default=True)
    timerCount = Column(Integer, default=0)
    category = Column(Enum(CategoryEnum), default=CategoryEnum.under_18)
    rank = Column(Integer, default=0)

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    is_active = Column(Boolean, default=True)

class TruthDareBase(BaseModel):
    body: str
    isTruth: bool
    isBoy: bool
    timerCount: int
    category: CategoryEnum
    rank: int

class TruthDareCreate(TruthDareBase):
    pass

class TruthDareResponse(TruthDareBase):
    id: int

    class Config:
        orm_mode = True

class PlayerBase(BaseModel):
    name: str
    age: int
    is_active: bool

class PlayerCreate(PlayerBase):
    pass

class PlayerResponse(PlayerBase):
    id: int

    class Config:
        orm_mode = True
