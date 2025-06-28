# 💡 Student Profile Manager API-Gradient

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-🚀-green)
![Kivy](https://img.shields.io/badge/Kivy-GUI-lightgrey)
![SQLite](https://img.shields.io/badge/Database-SQLite3-blue)
![Challenge](https://img.shields.io/badge/30DaysOfPython-COMPLETED-success)
![Status](https://img.shields.io/badge/Status-FINAL-blueviolet)

> 🌈 A full-stack academic profile management app powered by **FastAPI**, **SQLite**, and **Kivy GUI**  
> 🛠️ Built as part of my 30-day Python challenge with **Indian Data Club**

---

## 📌 Project Overview

This system allows users to:
- Add student records with full academic info
- Track grades, branches, years, and subjects
- View all records from a GUI frontend
- Store everything offline via SQLite

The project was split into two milestones:

| Day | Milestone        | Description                        |
|-----|------------------|------------------------------------|
| 29  | Mini Project     | Backend API with FastAPI & SQLite |
| 30  | Capstone Project | GUI Frontend with Kivy            |

---

## ✨ Features

✅ Add Students with validation  
✅ Select Branch, Year, Subject, Grade  
✅ View full records (Students, Subjects, Branches...)  
✅ Kivy-based tabbed UI  
✅ Swagger Docs (`/docs`) + ReDoc (`/redoc`)  
✅ All Python — no JavaScript or HTML needed  
✅ Works 100% offline 💻

---

## 💻 Tech Stack

| Category              | Tools/Technologies                            |
|-----------------------|-----------------------------------------------|
| 👩‍💻 Programming Language | Python 3.11                                   |
| 🧰 Backend Framework     | FastAPI, SQLAlchemy ORM, Pydantic             |
| 🗃️ Database              | SQLite3                                      |
| 🎨 GUI Framework         | Kivy                                         |
| 🛠️ Tools & IDE           | VS Code, Git, GitHub                         |
| 📘 API Docs              | Swagger UI, ReDoc                            |


---

## 📸 Application Screenshots

### 🖥️ Kivy GUI
![Kivy GUI](images/kivy_gui.png) 

### 📝 Swagger UI 
![Swagger UI](images/swagger_ui.png)





---
## 📁 Project Directory Structure

```bash
Student-Profile-Manager/
├── student-profile-manager/
│   ├── app/
│   │   ├── routers/
│   │   │   ├── students.py         # 🎓 Student CRUD routes
│   │   │   ├── grades.py           # 🧪 Grade logic
│   │   │   ├── years.py            # 🗓️ Academic year endpoints
│   │   │   ├── branches.py         # 🏫 Branch info (CSE, ECE, etc.)
│   │   │   └── subjects.py         # 📘 Subject details
│   │   └── __init__.py             # Module initializer
│   ├── student_profile_kivy_gui.py # 🖥️ Kivy GUI frontend
│   ├── main.py                     # 🚀 FastAPI app launcher
│   ├── seed_data.py                # 🌱 Pre-populates DB
│   ├── init_db.py                  # 🧱 DB table creator
│   ├── students.db                 # 🗃️ SQLite database file
│   ├── requirements.txt            # 📦 Project dependencies
│   └── ...
├── students.db                     # 🔁 (Duplicate backup / for testing)
└── README.md                       # 📄 You’re reading it!

## ⚙️ Setup & Run

### 🔁  Clone the Repo

```bash
git clone https://github.com/VANISAIDEEPIKA/Student-Profile-Manager-API-Gradient.git
cd Student-Profile-Manager-API-Gradient

# ⬇️ Install Dependencies
pip install -r requirements.txt

# 🧱 Initialize the Database
python init_db.py
python seed_data.py

# 🚀 Run Backend API (localhost:8001)
start "" uvicorn main:app --reload --port 8001

# 🖥️ Launch Kivy GUI (desktop app)
python student_profile_kivy_gui.py


 🌟 Project Highlights

- 🧠 Learned full-stack Python (FastAPI + Kivy) in 30 days  
- 🛠️ Wrote modular, clean backend with ORM models & dependency injection  
- 💻 Designed a working GUI — no web frontend needed  
- 🔗 Built a complete CRUD app usable offline  

