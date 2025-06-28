from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from typing import List
from app import models, schemas, database

router = APIRouter(
    prefix="/years",
    tags=["Years"]
)

@router.get("/", response_model=List[schemas.YearOut])
def get_years(db: Session = Depends(database.get_db)):
    years = db.query(models.Year).all()
    return years  # ✅ Ensure you return a list, not None
