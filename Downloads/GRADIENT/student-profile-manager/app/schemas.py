    # app/schemas.py

from pydantic import BaseModel, EmailStr, conint
from typing import Optional

# --------------------------- STUDENT ---------------------------
class StudentBase(BaseModel):
    name: str
    roll_number: str
    email: EmailStr
    age: conint(ge=10, le=100)
    year: int
    branch: str
    subject: str
    grade: str

class StudentCreate(StudentBase):
    pass

class StudentOut(StudentBase):
    id: int

    class Config:
        from_attributes = True

# --------------------------- SUBJECT ---------------------------
class SubjectBase(BaseModel):
    name: str

class SubjectCreate(SubjectBase):
    pass

class SubjectOut(SubjectBase):
    id: int

    class Config:
        from_attributes = True

# --------------------------- GRADE ---------------------------
class GradeCreate(BaseModel):
    student_id: int
    subject_id: int
    score: conint(ge=0, le=100)

class GradeOut(GradeCreate):
    id: int

    class Config:
        from_attributes = True

class GradeScaleBase(BaseModel):
    grade_letter: str
    min_score: int
    max_score: int

class GradeScaleCreate(GradeScaleBase):
    pass

class GradeScaleOut(GradeScaleBase):
    id: int

    class Config:
        from_attributes = True

# --------------------------- BRANCH ---------------------------
class BranchCreate(BaseModel):
    name: str
    full_form: str

class BranchOut(BaseModel):
    id: int
    name: str
    full_form: str

    class Config:
        from_attributes = True

# --------------------------- YEAR ---------------------------
class YearCreate(BaseModel):
    year: str

class YearOut(BaseModel):
    id: int
    year: str

    class Config:
        from_attributes = True
