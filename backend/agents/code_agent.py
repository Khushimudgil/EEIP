from services.hybrid_search_service import hybrid_search


def run_code_agent(
    question,
    repo_id
):

    results = hybrid_search(
        query=question,
        repo_id=repo_id
    )

    if not results:
        return {
            "answer": "Function or class not found in repository.",
            "sources": []
        }

    return results