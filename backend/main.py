from fastapi import FastAPI
print("1. FastAPI imported")

from fastapi.middleware.cors import CORSMiddleware
print("2. CORSMiddleware imported")

from database.database import Base, engine
print("3. Database imported")

# Import every database model
from models.repository_db import RepositoryDB
from models.chat_history_db import ChatHistoryDB
print("4. Database models imported")

from api.repository import router as repository_router
print("5. Repository router imported")

from api.search import router as search_router
print("6. Search router imported")

from api.progress import router as progress_router
print("7. Progress router imported")

from api.dashboard import router as dashboard_router
print("8. Dashboard router imported")

# Create all database tables
# Base.metadata.create_all(bind=engine)
print("9. Database tables created")

app = FastAPI(
    title="Enterprise Engineering Intelligence Platform",
    description="AI-powered repository intelligence platform",
    version="1.0.0"
)

print("10. FastAPI app created")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("11. Middleware added")

app.include_router(repository_router)
print("12. Repository router added")

app.include_router(search_router)
print("13. Search router added")

app.include_router(progress_router)
print("14. Progress router added")

app.include_router(dashboard_router)
print("15. Dashboard router added")

print("16. Application startup completed")


@app.get("/")
def home():
    return {
        "project": "EEIP",
        "status": "Running",
        "version": "1.0.0"
    }


@app.get("/project-info")
def project_info():
    return {
        "name": "Enterprise Engineering Intelligence Platform",
        "short_name": "EEIP",
        "purpose": "Repository Understanding and AI Engineering Assistance"
    }