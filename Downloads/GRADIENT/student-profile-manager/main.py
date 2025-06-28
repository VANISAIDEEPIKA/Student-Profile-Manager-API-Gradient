import webbrowser
import logging
from fastapi import FastAPI
from app.routers import students, subjects, grades, branches, years
from app.database import Base, engine

# ✅ Enable debug logging for deeper tracing
logging.basicConfig(level=logging.DEBUG)

# ✅ Create database tables if they do not exist
Base.metadata.create_all(bind=engine)

# ✅ Initialize FastAPI app with title and description
app = FastAPI(
    title="Student Profile Manager API – Gradient",
    description="A full-stack REST API to manage students, subjects, grades, branches, and years.",
    version="1.0.0"
)

# ✅ Root health check endpoint
@app.get("/")
def root():
    return {"message": "Welcome to Student Profile Manager API 🎓 Use /docs to explore the API."}

# ✅ Include all routers
app.include_router(students.router)
app.include_router(subjects.router)
app.include_router(grades.router)
app.include_router(branches.router)
app.include_router(years.router)

# ✅ Run with auto-opening Swagger UI
if __name__ == '__main__':
    import uvicorn

    try:
        webbrowser.open("http://127.0.0.1:8001/docs")
    except Exception as e:
        logging.warning(f"Could not open browser automatically: {e}")

    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
