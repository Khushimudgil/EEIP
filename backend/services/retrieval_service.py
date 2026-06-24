from services.embedding_service import generate_embedding
from services.qdrant_service import search_embeddings


def retrieve_context(
    query: str,
    repo_id: int,
    top_k: int = 10
):

    query_embedding = generate_embedding(
        query
    )

    results = search_embeddings(
        embedding=query_embedding,
        repo_id=repo_id,
        limit=top_k
    )

    chunks = []

    for point in results.points:

        chunks.append(
            {
                "id": point.payload.get("id"),

                "score": point.score,

                "file": point.payload.get("file"),
                "file_path": point.payload.get("file_path"),

                "name": point.payload.get("chunk_name"),
                "type": point.payload.get("chunk_type"),

                "start_line": point.payload.get(
                    "start_line"
                ),
                "end_line": point.payload.get(
                    "end_line"
                ),

                "code": point.payload.get("code")
            }
        )

    return chunks