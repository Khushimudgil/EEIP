from services.hybrid_search_service import hybrid_search
from services.reranker_service import rerank_results
from services.context_builder import build_context
from services.prompt_builder import build_prompt
from services.gemini_service import ask_gemini
from services.query_classifier import classify_query
from services.agent_router import route_agent



def answer_question(
    repo_id,
    question
):

    query_type = classify_query(
    question
    )

    hybrid_results = route_agent(
    query_type=query_type,
    question=question,
    repo_id=repo_id
    )

    reranked_results = rerank_results(
        question,
        hybrid_results
    )

    context = build_context(
        reranked_results
    )

    prompt = build_prompt(
        context,
        question
    )

    answer = ask_gemini(
        prompt
    )

    sources = []

    for chunk in reranked_results[:5]:

        sources.append(
            {
                "file": chunk.get("file"),
                "chunk": chunk.get("name"),
                "start_line": chunk.get("start_line"),
                "end_line": chunk.get("end_line")
            }
        )

    return {
    "query_type": query_type,
    "answer": answer,
    "sources": sources
}