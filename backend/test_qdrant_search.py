# test_qdrant_search.py

from services.embedding_service import generate_embedding
from services.qdrant_service import search_embeddings

embedding = generate_embedding(
    "user authentication login"
)

results = search_embeddings(embedding)

for point in results.points:
    print("Repo:", point.payload["repo_id"])
    print("File:", point.payload["file"])
    print("Function:", point.payload["function"])
    print("Score:", point.score)