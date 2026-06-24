from database.database import SessionLocal
from models.embedding_db import EmbeddingDB


def save_embedding(content, embedding):

    db = SessionLocal()

    row = EmbeddingDB(
        content=content,
        embedding=str(embedding)
    )

    db.add(row)
    db.commit()

    db.close()