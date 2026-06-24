from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.repository import router as repository_router
from api.search import router as search_router
from api.progress import router as progress_router

app = FastAPI(
    title="Enterprise Engineering Intelligence Platform",
    description="AI-powered repository intelligence platform",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(repository_router)
app.include_router(search_router)
app.include_router(progress_router)


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