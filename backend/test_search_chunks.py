# test_search_chunks.py

from services.embedding_service import generate_embedding
from services.qdrant_service import search_embeddings

query = "authentication login"

embedding = generate_embedding(query)

results = search_embeddings(embedding)

print(results)