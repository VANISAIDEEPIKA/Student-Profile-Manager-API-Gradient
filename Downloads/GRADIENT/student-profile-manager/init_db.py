from app.database import engine, Base
from app import models

def init():
    print("🔄 Creating all tables as per models.py...")
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized and tables created successfully.")

if __name__ == "__main__":
    init()
