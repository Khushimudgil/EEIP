# test_qdrant.py

from qdrant_client import QdrantClient

client = QdrantClient(
    host="localhost",
    port=6333
)

points = client.scroll(
    collection_name="repository_vectors",
    limit=5,
    with_payload=True
)

print(points)