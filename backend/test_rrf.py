from services.rrf_service import rrf_fusion


dense_results = [
    {
        "id": "A",
        "name": "chunk_a"
    },
    {
        "id": "B",
        "name": "chunk_b"
    }
]

bm25_results = [
    (
        {
            "id": "A",
            "name": "chunk_a"
        },
        8.5
    ),
    (
        {
            "id": "C",
            "name": "chunk_c"
        },
        7.2
    )
]

results = rrf_fusion(
    dense_results,
    bm25_results
)

for item in results:

    print(
        item["chunk"]["name"],
        item["score"]
    )