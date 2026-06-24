from fastapi import APIRouter
from pydantic import BaseModel
from services.embedding_service import generate_embedding
from services.qdrant_service import search_embeddings


router = APIRouter()


class SearchRequest(BaseModel):
    query: str


@router.post("/search")
def search(request: SearchRequest):

    query_embedding = generate_embedding(request.query)

    results = search_embeddings(query_embedding)

    return {
        "matches": [
            {
                "repo_id": point.payload["repo_id"],
                "file": point.payload["file"],
                "function": point.payload["function"],
                "score": point.score
            }
            for point in results.points
        ]
    }