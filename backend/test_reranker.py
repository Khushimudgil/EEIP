from services.repository_metadata_service import get_repository_metadata
from services.bm25_service import build_bm25_index
from services.hybrid_search_service import hybrid_search
from services.reranker_service import rerank_results

chunks = []

metadata = get_repository_metadata(
    "repos/repo_20"
)

for file_data in metadata:

    if "chunks" in file_data:

        chunks.extend(
            file_data["chunks"]
        )

build_bm25_index(chunks)

results = hybrid_search(
    query="authentication login",
    repo_id=20
)

reranked = rerank_results(
    "authentication login",
    results
)

print(reranked[:3])