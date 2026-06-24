# test_qdrant_save.py

from services.embedding_service import generate_embedding
from services.qdrant_service import save_embedding

text = "FastAPI login function"

embedding = generate_embedding(text)

save_embedding(
    repo_id=1,
    file_name="auth.py",
    function_name="login",
    embedding=embedding
)