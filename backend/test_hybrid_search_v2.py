from services.repository_metadata_service import get_repository_metadata
from services.bm25_service import build_bm25_index
from services.hybrid_search_service import hybrid_search

import hashlib


# Step 1: Get repository metadata
metadata = get_repository_metadata(
    "repos/fastapi"
)

# Step 2: Extract all chunks
all_chunks = []

for file_data in metadata:

    if "chunks" in file_data:

        all_chunks.extend(
            file_data["chunks"]
        )

# Step 3: Add unique IDs to every chunk
for chunk in all_chunks:

    chunk["id"] = hashlib.md5(
        (
            chunk["file_path"]
            + chunk["name"]
        ).encode()
    ).hexdigest()

# Debug
print("TOTAL CHUNKS:", len(all_chunks))

print("\nFIRST CHUNK:")
print(all_chunks[0])

# Step 4: Build BM25 Index
build_bm25_index(
    all_chunks
)

# Step 5: Run Hybrid Search
results = hybrid_search(
    query="authentication",
    repo_id=1
)

# Step 6: Print Dense Results
print("\n==============================")
print("DENSE RESULTS")
print("==============================")

print("Total:", len(results["dense"]))

for result in results["dense"][:5]:

    print(result)
    print()

# Step 7: Print BM25 Results
print("\n==============================")
print("BM25 RESULTS")
print("==============================")

print("Total:", len(results["bm25"]))

for chunk, score in results["bm25"][:5]:

    print("Chunk Name:", chunk["name"])
    print("Chunk ID:", chunk["id"])
    print("Score:", score)
    print("-" * 40)

exit()