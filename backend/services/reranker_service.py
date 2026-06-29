# from sentence_transformers import CrossEncoder

# reranker = CrossEncoder(
#     "cross-encoder/ms-marco-MiniLM-L-6-v2"
# )


# def rerank_results(
#     query,
#     chunks
# ):

#     pairs = []

#     for chunk in chunks:

#         pairs.append(
#             [
#                 query,
#                 chunk["code"]
#             ]
#         )

#     scores = reranker.predict(
#         pairs
#     )

#     for chunk, score in zip(
#         chunks,
#         scores
#     ):

#         chunk["rerank_score"] = float(score)

#     chunks.sort(
#         key=lambda x: x["rerank_score"],
#         reverse=True
#     )

#     return chunks

def rerank_results(query, chunks):

    """
    Temporary lightweight reranker.

    Since the results have already been fused using
    Reciprocal Rank Fusion (RRF), we simply return them.

    This avoids loading the CrossEncoder model, which
    exceeds Render Free memory limits.
    """

    return chunks