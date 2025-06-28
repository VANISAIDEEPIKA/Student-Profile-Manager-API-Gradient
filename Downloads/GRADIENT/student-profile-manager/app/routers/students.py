# app/routers/students.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from typing import List

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

# ✅ Create student with all fields
@router.post("/", response_model=schemas.StudentOut)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    try:
        created_student = crud.create_student(db, student)
        return created_student
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ✅ List all students
@router.get("/", response_model=List[schemas.StudentOut])
def list_students(db: Session = Depends(get_db)):
    students = crud.get_students(db)
    if not students:
        print("⚠️ No students found in the database.")
    return students

# ✅ Get student by roll number
@router.get("/{roll_number}", response_model=schemas.StudentOut)
def get_student_by_roll(roll_number: str, db: Session = Depends(get_db)):
    student = crud.get_student_by_roll(db, roll_number)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
