from services.qdrant_service import client

client.delete_collection(
    collection_name="repository_vectors"
)

print("Collection deleted")