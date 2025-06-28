# app/routers/grades.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db

router = APIRouter(prefix="/grades", tags=["Grades"])

# ✅ Assign grade to student
@router.post("/", response_model=schemas.GradeOut)
def assign_grade(grade: schemas.GradeCreate, db: Session = Depends(get_db)):
    return crud.assign_grade(db, grade)

# ✅ Get grades for a specific student
@router.get("/student/{student_id}", response_model=list[schemas.GradeOut])
def get_grades_for_student(student_id: int, db: Session = Depends(get_db)):
    return crud.get_grades_for_student(db, student_id)

# ✅ Get all grade scales for view
@router.get("/", response_model=list[schemas.GradeScaleOut])
def get_grade_scales(db: Session = Depends(get_db)):
    return crud.get_grade_scales(db)
