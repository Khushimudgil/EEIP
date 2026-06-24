from services.retrieval_service import retrieve_context
from services.bm25_service import search_bm25
from services.fusion_service import reciprocal_rank_fusion



def hybrid_search(
    query,
    repo_id,
    top_k=10
):

    dense_results = retrieve_context(
        query=query,
        repo_id=repo_id,
        top_k=top_k
    )

    bm25_results = search_bm25(
        query=query,
        top_k=top_k
    )

    fused_results = reciprocal_rank_fusion(
    dense_results,
    bm25_results
    )

    return fused_results
