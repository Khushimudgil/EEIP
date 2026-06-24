from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

texts = [
    "clone repository from github",
    "parse python files",
    "store metadata in database"
]

embeddings = model.encode(texts)

query = "how to save repository information"

query_embedding = model.encode([query])

scores = cosine_similarity(
    query_embedding,
    embeddings
)

print(scores)