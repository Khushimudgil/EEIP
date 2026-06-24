from qdrant_client import QdrantClient
from qdrant_client.models import (
    VectorParams,
    Distance,
    PointStruct,
    Filter,
    FieldCondition,
    MatchValue
)

client = QdrantClient(
    host="localhost",
    port=6333
)


def create_collection():

    collections = client.get_collections()

    existing = [
        collection.name
        for collection in collections.collections
    ]

    if "repository_vectors" in existing:
        print("Collection already exists")
        return

    client.create_collection(
        collection_name="repository_vectors",
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        )
    )

    print("Collection created")


def save_embedding(
    repo_id,
    chunk,
    embedding
):

    chunk_id = str(
        abs(
            hash(
                chunk["file_path"]
                + chunk["name"]
                + chunk["type"]
            )
        ) % (10**9)
    )

    client.upsert(
        collection_name="repository_vectors",
        points=[
            PointStruct(
                id=int(chunk_id),

                vector=embedding,

                payload={
                "id": chunk_id,

                "repo_id": repo_id,

                "file": chunk["file"],
                "file_path": chunk["file_path"],

                "language": chunk["language"],

                "class_name": chunk["class_name"],
                "function_name": chunk["function_name"],

                "chunk_type": chunk["type"],
                "chunk_name": chunk["name"],

                "start_line": chunk["start_line"],
                "end_line": chunk["end_line"],

                "code": chunk["code"]
                }
            )
        ]
    )

    print("Embedding saved")


def search_embeddings(
    embedding,
    repo_id,
    limit=10
):

    results = client.query_points(
        collection_name="repository_vectors",

        query=embedding,

        query_filter=Filter(
            must=[
                FieldCondition(
                    key="repo_id",
                    match=MatchValue(
                        value=repo_id
                    )
                )
            ]
        ),

        limit=limit
    )

    return results