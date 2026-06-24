def reciprocal_rank_fusion(
    dense_results,
    bm25_results,
    k=60
):

    scores = {}
    chunk_map = {}

    # Dense Results
    for rank, chunk in enumerate(
        dense_results,
        start=1
    ):

        chunk_id = str(
            abs(
                hash(
                    chunk["file"]
                    + chunk["name"]
                    + chunk["type"]
                )
            ) % (10**9)
        )

        chunk_map[chunk_id] = chunk

        scores[chunk_id] = (
            scores.get(chunk_id, 0)
            +
            1 / (k + rank)
        )

    # BM25 Results
    for rank, result in enumerate(
        bm25_results,
        start=1
    ):

        chunk = result[0]

        chunk_id = str(
            abs(
                hash(
                    chunk["file"]
                    + chunk["name"]
                    + chunk["type"]
                )
            ) % (10**9)
        )

        chunk_map[chunk_id] = chunk

        scores[chunk_id] = (
            scores.get(chunk_id, 0)
            +
            1 / (k + rank)
        )

    ranked = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    fused_results = []

    for chunk_id, score in ranked:

        chunk = chunk_map[chunk_id]

        chunk["rrf_score"] = score

        fused_results.append(chunk)

    return fused_results