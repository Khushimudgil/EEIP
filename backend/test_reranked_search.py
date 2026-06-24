from services.repository_metadata_service import (
    get_repository_metadata
)

from services.bm25_service import (
    build_bm25_index
)

from services.hybrid_search_service import (
    hybrid_search
)

import hashlib


metadata = get_repository_metadata(
    "repos/fastapi"
)

all_chunks = []

for file_data in metadata:

    if "chunks" in file_data:

        all_chunks.extend(
            file_data["chunks"]
        )

for chunk in all_chunks:

    chunk["id"] = hashlib.md5(
        (
            chunk["file_path"]
            + chunk["name"]
        ).encode()
    ).hexdigest()

build_bm25_index(
    all_chunks
)

results = hybrid_search(
    query="authentication",
    repo_id=1
)

print(
    "\nTOP RESULTS:",
    len(results)
)

for item in results[:10]:

    chunk = item["chunk"]

    print("\n" + "=" * 60)

    print(
        "Chunk Name:",
        chunk["name"]
    )

    print(
        "Chunk Type:",
        chunk["type"]
    )

    print(
        "File:",
        chunk["file"]
    )

    print(
        "Cross Score:",
        item["cross_score"]
    )