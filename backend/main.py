from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas
from .database import engine, get_db, Base

# Create tables if they don't exist
# In production, use Alembic migrations instead
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SAGARMITRA AI API",
    description="API for the free, open-source marine decision support system.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to SAGARMITRA AI Data API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# --- Users ---

@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/", response_model=List[schemas.UserResponse])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.User).offset(skip).limit(limit).all()

# --- Marine Advisories ---

@app.post("/advisories/", response_model=schemas.MarineAdvisoryResponse)
def create_advisory(advisory: schemas.MarineAdvisoryBase, db: Session = Depends(get_db)):
    db_adv = models.MarineAdvisory(**advisory.model_dump())
    db.add(db_adv)
    db.commit()
    db.refresh(db_adv)
    return db_adv

@app.get("/advisories/", response_model=List[schemas.MarineAdvisoryResponse])
def get_advisories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.MarineAdvisory).offset(skip).limit(limit).all()

# GIS processing routes (PFZ, Weather, Ocean Data) would go here
# e.g., @app.get("/pfz/latest")
