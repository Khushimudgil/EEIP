import os
from dotenv import load_dotenv

from qdrant_client import QdrantClient
from qdrant_client.models import (
    VectorParams,
    Distance,
    PointStruct,
    Filter,
    FieldCondition,
    MatchValue
)

load_dotenv()

client = None


def get_client():
    global client

    if client is None:
        client = QdrantClient(
            url=os.getenv("QDRANT_URL"),
            api_key=os.getenv("QDRANT_API_KEY"),
            check_compatibility=False
        )

    return client


def create_collection():

    client = get_client()

    collections = client.get_collections()

    existing = [
        collection.name
        for collection in collections.collections
    ]

    if "repository_vectors" not in existing:

        client.create_collection(
            collection_name="repository_vectors",
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )

        print("Collection created")

    else:
        print("Collection already exists")

    try:
        client.create_payload_index(
            collection_name="repository_vectors",
            field_name="repo_id",
            field_schema="integer"
        )
        print("repo_id payload index created")
    except Exception as e:
        print("Index already exists:", e)


def save_embedding(
    repo_id,
    chunk,
    embedding
):

    client = get_client()

    chunk_id = abs(
        hash(
            chunk["file_path"]
            + chunk["name"]
            + chunk["type"]
        )
    ) % (10 ** 9)

    client.upsert(
        collection_name="repository_vectors",
        points=[
            PointStruct(
                id=chunk_id,
                vector=embedding,
                payload={
                    "id": str(chunk_id),

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

    client = get_client()

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