from qdrant_client import QdrantClient

client = QdrantClient(
    host="localhost",
    port=6333
)

info = client.get_collection(
    collection_name="repository_vectors"
)

print(info)