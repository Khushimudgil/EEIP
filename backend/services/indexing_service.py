from services.embedding_service import generate_embedding
from services.qdrant_service import save_embedding
from services.bm25_service import build_bm25_index


def index_repository(repo_id, metadata):

    print("Indexing started")

    all_chunks = []

    for file_data in metadata:

        if "chunks" not in file_data:
            continue

        all_chunks.extend(
            file_data["chunks"]
        )

        print(
            f"File: {file_data['file']} "
            f"Chunks: {len(file_data['chunks'])}"
        )

        for chunk in file_data["chunks"]:

            print(
                f"Embedding: {chunk['name']}"
            )

            embedding = generate_embedding(
                chunk["code"]
            )

            save_embedding(
                repo_id,
                chunk,
                embedding
            )

    build_bm25_index(
        all_chunks
    )

    print("BM25 built")
    print("Repository indexed")