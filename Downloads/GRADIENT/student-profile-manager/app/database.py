# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager

# ✅ Database URL for local SQLite (file-based DB)
SQLALCHEMY_DATABASE_URL = "sqlite:///./students.db"

# ✅ Create engine for SQLite with thread check disabled
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# ✅ SessionLocal: used to create session per request
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ✅ Declarative base class for ORM models
Base = declarative_base()

# ✅ Dependency injection for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ OPTIONAL: Context manager for scripts/tests outside FastAPI
@contextmanager
def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
