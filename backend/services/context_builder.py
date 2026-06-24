def build_context(
    reranked_results,
    max_chunks=5
):

    context = ""

    for chunk in reranked_results[:max_chunks]:

        context += (
            f"File: {chunk['file']}\n"
            f"Chunk: {chunk['name']}\n"
            f"Type: {chunk['type']}\n\n"
            f"{chunk['code']}\n"
            f"{'='*50}\n"
        )

    return context