from services.embedding_service import generate_embedding
from database.embedding_repository import save_embedding

text = "user login authentication"

vector = generate_embedding(text)

save_embedding(text, vector)

print("Embedding Saved")
