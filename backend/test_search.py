from services.embedding_service import generate_embedding
from services.qdrant_service import search_embeddings

query_embedding = generate_embedding("login")

results = search_embeddings(query_embedding)

print(results)