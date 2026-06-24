# test_qdrant_chunks.py

from qdrant_client import QdrantClient

client = QdrantClient(
    host="localhost",
    port=6333
)

points, _ = client.scroll(
    collection_name="repository_vectors",
    limit=5
)

for point in points:
    print(point.payload)
    print("-" * 50)