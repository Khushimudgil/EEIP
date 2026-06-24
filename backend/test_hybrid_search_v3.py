from services.repository_metadata_service import get_repository_metadata
from services.bm25_service import build_bm25_index
from services.hybrid_search_service import hybrid_search

import hashlib


# Step 1: Load repository metadata
metadata = get_repository_metadata(
    "repos/fastapi"
)

# Step 2: Extract chunks
all_chunks = []

for file_data in metadata:

    if "chunks" in file_data:
        all_chunks.extend(
            file_data["chunks"]
        )

# Step 3: Add unique IDs
for chunk in all_chunks:

    chunk["id"] = hashlib.md5(
        (
            chunk["file_path"]
            + chunk["name"]
        ).encode()
    ).hexdigest()

# Step 4: Build BM25 Index
build_bm25_index(
    all_chunks
)

print("BM25 INDEX BUILT")
print("TOTAL CHUNKS:", len(all_chunks))

# Step 5: Run Hybrid Search
results = hybrid_search(
    query="authentication",
    repo_id=1
)

# Step 6: Debug
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
        "Fusion Score:",
        item["score"]
    )