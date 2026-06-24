from services.chat_service import (
    chat_with_repository
)

from services.repository_metadata_service import (
    get_repository_metadata
)

from services.bm25_service import (
    build_bm25_index
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


response = chat_with_repository(
    question="How is authentication implemented?",
    repo_id=1
)

print("\nANSWER:\n")
print(response["answer"])