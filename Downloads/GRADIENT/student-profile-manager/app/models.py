from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# --------------------------- STUDENT ---------------------------
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    roll_number = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    age = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    branch = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    grade = Column(String, nullable=False)

    grades = relationship("Grade", back_populates="student", cascade="all, delete")

# --------------------------- SUBJECT ---------------------------
class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False, index=True)

    grades = relationship("Grade", back_populates="subject", cascade="all, delete")

# --------------------------- GRADE ---------------------------
class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"), nullable=False)
    score = Column(Integer, nullable=False)

    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")
class GradeScale(Base):
    __tablename__ = "grade_scales"

    id = Column(Integer, primary_key=True, index=True)
    grade_letter = Column(String, unique=True, nullable=False, index=True)
    min_score = Column(Integer, nullable=False)
    max_score = Column(Integer, nullable=False)


class Branch(Base):
    __tablename__ = "branches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False, index=True)
    full_form = Column(String, nullable=False)

class Year(Base):
    __tablename__ = "years"

    id = Column(Integer, primary_key=True, index=True)
    year = Column(String, unique=True, nullable=False, index=True)


