from services.hybrid_search_service import hybrid_search


def run_summary_agent(
    question,
    repo_id
):

    return hybrid_search(
        query=question,
        repo_id=repo_id
    )