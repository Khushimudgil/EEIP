
from agents.summary_agent import run_summary_agent
from agents.search_agent import run_search_agent
from agents.code_agent import run_code_agent


def route_agent(
    query_type,
    question,
    repo_id
):

    if query_type == "SUMMARY":
        return run_summary_agent(
            question,
            repo_id
        )

    if query_type == "CODE":
        return run_code_agent(
            question,
            repo_id
        )

    return run_search_agent(
        question,
        repo_id
    )