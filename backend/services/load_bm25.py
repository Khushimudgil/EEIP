
from services.repository_metadata_service import (
    get_repository_metadata
)

from services.bm25_service import (
    build_bm25_index
)

def load_bm25(repo_path):

    metadata = get_repository_metadata(
        repo_path
    )

    chunks = []

    for file_data in metadata:

        if "chunks" in file_data:

            chunks.extend(
                file_data["chunks"]
            )

    build_bm25_index(chunks)

    print("BM25 Ready")