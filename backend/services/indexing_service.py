from services.embedding_service import generate_embeddings
from services.qdrant_service import (
    create_collection,
    save_embedding
)
from services.bm25_service import build_bm25_index


def index_repository(repo_id, metadata):

    print("Indexing started")

    # Create Qdrant collection if it doesn't exist
    create_collection()

    all_chunks = []

    # Collect all valid chunks
    for file_data in metadata:

        if "chunks" not in file_data:
            continue

        print(
            f"File: {file_data['file']} | Chunks: {len(file_data['chunks'])}"
        )

        for chunk in file_data["chunks"]:

            code = chunk.get("code", "").strip()

            # Skip empty or tiny chunks
            if len(code.split()) < 20:
                continue

            all_chunks.append(chunk)

    print(f"Total chunks collected: {len(all_chunks)}")

    # Nothing to index
    if len(all_chunks) == 0:
        print("No valid chunks found.")
        return

    # Generate embeddings in batches
    texts = [
        chunk["code"]
        for chunk in all_chunks
    ]

    print("Generating embeddings...")

    embeddings = generate_embeddings(texts)

    print("Saving embeddings to Qdrant...")

    for chunk, embedding in zip(all_chunks, embeddings):

        save_embedding(
            repo_id=repo_id,
            chunk=chunk,
            embedding=embedding
        )

    print("Building BM25 index...")

    build_bm25_index(all_chunks)

    print("Repository indexed successfully.")