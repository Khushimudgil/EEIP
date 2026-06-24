from services.embedding_service import generate_embedding

text = "def login(username,password)"

embedding = generate_embedding(text)

print(type(embedding))
print(len(embedding))
print(embedding[:5])