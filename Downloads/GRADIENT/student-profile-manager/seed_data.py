from app.database import SessionLocal
from app import models

db = SessionLocal()

# ✅ Full B.Tech & MBA Branches with Full Forms
branches = [
    ("CSE", "Computer Science and Engineering"),
    ("IT", "Information Technology"),
    ("ECE", "Electronics and Communication Engineering"),
    ("EEE", "Electrical and Electronics Engineering"),
    ("ME", "Mechanical Engineering"),
    ("CE", "Civil Engineering"),
    ("AIML", "Artificial Intelligence and Machine Learning"),
    ("CS", "Cyber Security"),
    ("DS", "Data Science"),
    ("ECM", "Electronics and Computer Engineering"),
    ("MBA-FIN", "MBA - Finance"),
    ("MBA-MKT", "MBA - Marketing"),
    ("MBA-HR", "MBA - Human Resources"),
    ("MBA-OPS", "MBA - Operations Management"),
    ("MBA-BA", "MBA - Business Analytics"),
]

for code, full_form in branches:
    if not db.query(models.Branch).filter(models.Branch.name == code).first():
        branch = models.Branch(name=code, full_form=full_form)
        db.add(branch)

# ✅ Seed Subjects
subjects_btech = [
    "Data Structures",
    "Operating Systems",
    "Database Management Systems",
    "Computer Networks",
    "Machine Learning",
    "Artificial Intelligence",
    "Web Technologies",
    "Cloud Computing"
]

subjects_mba = [
    "Financial Management",
    "Marketing Management",
    "Human Resource Management",
    "Business Analytics",
    "Strategic Management"
]

all_subjects = [f"B.Tech - {sub}" for sub in subjects_btech] + [f"MBA - {sub}" for sub in subjects_mba]

for s in all_subjects:
    if not db.query(models.Subject).filter(models.Subject.name == s).first():
        subject = models.Subject(name=s)
        db.add(subject)

db.commit()
db.close()

print("✅ Seeded years and subjects with clear B.Tech and MBA distinction.")

# ✅ Years
years = [
    "B.Tech Year 1",
    "B.Tech Year 2",
    "B.Tech Year 3",
    "B.Tech Year 4",
    "MBA Year 1",
    "MBA Year 2"
]
for y in years:
    if not db.query(models.Year).filter(models.Year.year == y).first():
        year = models.Year(year=y)
        db.add(year)

        db.commit()
db.close()

print("✅ Seeded years successfully.")


# ✅ Seed Grade Scales
grade_scales = [
    ("O", 90, 100),
    ("A+", 80, 89),
    ("A", 70, 79),
    ("B+", 60, 69),
    ("B", 50, 59),
    ("C", 40, 49),
    ("P", 35, 39),
    ("F", 0, 34)
]

for letter, min_s, max_s in grade_scales:
    if not db.query(models.GradeScale).filter(models.GradeScale.grade_letter == letter).first():
        gs = models.GradeScale(grade_letter=letter, min_score=min_s, max_score=max_s)
        db.add(gs)

db.commit()
db.close()

print("✅ Database seeded with full JNTUH branches, subjects, and years.")
