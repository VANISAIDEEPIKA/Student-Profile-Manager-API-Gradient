# app/crud.py

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app import models, schemas
from typing import List, Optional

# -------------------- STUDENT CRUD --------------------
def create_student(db: Session, student_data: schemas.StudentCreate) -> models.Student:
    print("📦 Preparing to add student...")

    if db.query(models.Student).filter(models.Student.email == student_data.email).first():
        raise ValueError(f"🚫 Email '{student_data.email}' is already in use.")

    if db.query(models.Student).filter(models.Student.roll_number == student_data.roll_number).first():
        raise ValueError(f"🚫 Roll number '{student_data.roll_number}' already exists.")

    new_student = models.Student(**student_data.dict())

    try:
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        print("✅ Student saved to DB!")
        return new_student
    except IntegrityError as e:
        db.rollback()
        print("❌ Integrity Error while saving student.")
        raise ValueError("Failed to add student due to integrity constraints.") from e

def get_students(db: Session) -> List[models.Student]:
    students = db.query(models.Student).all()
    print(f"👀 Retrieved {len(students)} students from the database.")
    return students

def get_student_by_id(db: Session, student_id: int) -> Optional[models.Student]:
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_student_by_roll(db: Session, roll_number: str) -> Optional[models.Student]:
    return db.query(models.Student).filter(models.Student.roll_number == roll_number).first()

def get_student_by_email(db: Session, email: str) -> Optional[models.Student]:
    return db.query(models.Student).filter(models.Student.email == email).first()

# -------------------- SUBJECT CRUD --------------------
def create_subject(db: Session, subject_data: schemas.SubjectCreate) -> models.Subject:
    subject = models.Subject(**subject_data.dict())
    db.add(subject)
    db.commit()
    db.refresh(subject)
    return subject

def get_subjects(db: Session) -> List[models.Subject]:
    subjects = db.query(models.Subject).all()
    print(f"👀 Retrieved {len(subjects)} subjects from the database.")
    return subjects

# -------------------- GRADE CRUD --------------------
def assign_grade(db: Session, grade_data: schemas.GradeCreate) -> models.Grade:
    grade = models.Grade(**grade_data.dict())
    db.add(grade)
    db.commit()
    db.refresh(grade)
    print(f"✅ Assigned grade with ID {grade.id}")
    return grade

def get_grades_for_student(db: Session, student_id: int) -> List[models.Grade]:
    grades = db.query(models.Grade).filter(models.Grade.student_id == student_id).all()
    print(f"👀 Retrieved {len(grades)} grades for student {student_id}.")
    return grades

def get_grade_scales(db: Session) -> List[models.GradeScale]:
    grade_scales = db.query(models.GradeScale).all()
    print(f"👀 Retrieved {len(grade_scales)} grade scales from the database.")
    return grade_scales

# -------------------- BRANCH CRUD --------------------
def create_branch(db: Session, branch_data: schemas.BranchCreate) -> models.Branch:
    branch = models.Branch(**branch_data.dict())
    db.add(branch)
    db.commit()
    db.refresh(branch)
    return branch

def get_branches(db: Session) -> List[models.Branch]:
    branches = db.query(models.Branch).all()
    print(f"👀 Retrieved {len(branches)} branches from the database.")
    return branches

# -------------------- YEAR CRUD --------------------
def create_year(db: Session, year_data: schemas.YearCreate) -> models.Year:
    year = models.Year(**year_data.dict())
    db.add(year)
    db.commit()
    db.refresh(year)
    return year

def get_years(db: Session) -> List[models.Year]:
    years = db.query(models.Year).all()
  