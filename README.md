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

---

 🌟 Project Highlights

- 🧠 Learned full-stack Python (FastAPI + Kivy) in 30 days  
- 🛠️ Wrote modular, clean backend with ORM models & dependency injection  
- 💻 Designed a working GUI — no web frontend needed  
- 🔗 Built a complete CRUD app usable offline
 
---
## 📚 What I Learned in 30 Days

I didn’t just *code* — I built something that connects all the concepts I’ve learned. Check out how this one project mapped to the 23/30 challenge days:

| ✅ **Day** | **Topic**               | **How it was covered in this project**                  |
|:----------:|-------------------------|---------------------------------------------------------|
| **00**     | Git, IDEs, VS Code      | VS Code for development, Git for version control       |
| **01**     | Python Basics           | Entire project uses core Python                        |
| **02**     | Variables & Data Types  | Used in Pydantic models and user inputs                |
| **03**     | Lists, Tuples, Dicts    | API request/response payloads                          |
| **04**     | Control Structures      | Validation, conditionals in backend logic              |
| **05**     | Functions               | CRUD functions, FastAPI routes, Kivy handlers          |
| **06**     | Modules & Packages      | Clean modular structure: `routers/`, `schemas/`, etc. |
| **07**     | File Handling           | SQLite DB file via SQLAlchemy                          |
| **08**     | OOP Part 1              | Pydantic & SQLAlchemy class-based models              |
| **09**     | OOP Part 2              | Inheritance in SQLAlchemy & Kivy                       |
| **10**     | Exception Handling      | Try-excepts for error-proof logic                      |
| **13**     | Data Structures         | Dicts, lists, and models to manage records             |
| **15**     | Decorators              | FastAPI’s `@app.get`, `@app.post`, etc.               |
| **17**     | Context Managers        | DB session handling using `with` blocks                |
| **19**     | Multithreading          | `threading.Thread` for Kivy + FastAPI                  |
| **20**     | Networking              | REST APIs via FastAPI                                  |
| **23**     | Kivy GUI                | Full desktop frontend with spinners & tabs             |
| **24**     | Dataclasses             | Pydantic mimics dataclasses for validation             |
| **25**     | Pydantic                | Strong validation for all input data                   |
| **26**     | FastAPI APIs            | Complete CRUD for all entities                         |
| **27**     | SQLAlchemy ORM          | Modeled Students, Subjects, Grades, etc.              |
| **28**     | Clean Code              | Structured architecture, readable and scalable         |
| **29**     | Mini Project            | FastAPI backend built from scratch                     |
| **30**     | Capstone Project        | Final integration + polish + docs ✅                   |

---

## 🔁 How It All Came Together

🛠️ **Project:** *Student Profile Manager – Gradient*  
🔁 **Day 29:** FastAPI Backend – *Mini Project*  
🎨 **Day 30:** Kivy GUI Frontend – *Capstone Project*

This wasn’t just a project — it was a *culmination*. A real, usable full-stack app built entirely in Python.





