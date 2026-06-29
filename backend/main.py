from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.database import Base, engine

# Import every database model
from models.repository_db import RepositoryDB
from models.chat_history_db import ChatHistoryDB

from api.repository import router as repository_router
from api.search import router as search_router
from api.progress import router as progress_router
from api.dashboard import router as dashboard_router


# Create all database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Enterprise Engineering Intelligence Platform",
    description="AI-powered repository intelligence platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(repository_router)
app.include_router(search_router)
app.include_router(progress_router)
app.include_router(dashboard_router)


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