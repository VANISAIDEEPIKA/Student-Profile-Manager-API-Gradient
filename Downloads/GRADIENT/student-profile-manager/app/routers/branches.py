from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/branches", tags=["Branches"])

@router.post("/", response_model=schemas.BranchOut)
def create_branch(branch: schemas.BranchCreate, db: Session = Depends(get_db)):
    return crud.create_branch(db, branch)

@router.get("/", response_model=list[schemas.BranchOut])
def list_branches(db: Session = Depends(get_db)):
    return crud.get_branches(db)
