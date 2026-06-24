def rrf_fusion(
    dense_results,
    bm25_results,
    k=60
):

    scores = {}

    # Dense Results
    for rank, chunk in enumerate(
        dense_results,
        start=1
    ):

        chunk_id = chunk["id"]

        if chunk_id not in scores:

            scores[chunk_id] = {
                "chunk": {
                    "id": chunk["id"],
                    "file": chunk["file"],
                    "file_path": chunk["file_path"],
                    "name": chunk["name"],
                    "type": chunk["type"],
                    "code": chunk["code"]
                },
                "score": 0
            }

        scores[chunk_id]["score"] += (
            1 / (k + rank)
        )

    # BM25 Results
    for rank, (chunk, _) in enumerate(
        bm25_results,
        start=1
    ):

        chunk_id = chunk["id"]

        if chunk_id not in scores:

            scores[chunk_id] = {
                "chunk": {
                    "id": chunk["id"],
                    "file": chunk["file"],
                    "file_path": chunk["file_path"],
                    "name": chunk["name"],
                    "type": chunk["type"],
                    "code": chunk["code"]
                },
                "score": 0
            }

        scores[chunk_id]["score"] += (
            1 / (k + rank)
        )

    fused = sorted(
        scores.values(),
        key=lambda x: x["score"],
        reverse=True
    )

    return fused