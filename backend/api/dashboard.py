from fastapi import APIRouter

from database.database import SessionLocal

from models.repository_db import RepositoryDB
from models.chat_history_db import ChatHistoryDB

from qdrant_client import QdrantClient

router = APIRouter()

client = QdrantClient(
    host="localhost",
    port=6333
)


@router.get("/dashboard-stats")
def dashboard_stats():

    db = SessionLocal()

    try:

        # Total repositories
        repositories = db.query(
            RepositoryDB
        ).count()

        # Total AI queries
        ai_queries = db.query(
            ChatHistoryDB
        ).count()

        # Total embeddings in Qdrant
        try:

            embeddings = client.count(
                collection_name="repository_vectors"
            ).count

        except Exception:

            embeddings = 0

        return {

            "repositories": repositories,

            "files_parsed": 0,

            "embeddings": embeddings,

            "ai_queries": ai_queries

        }

    finally:

        db.close()