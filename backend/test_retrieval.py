from services.retrieval_service import retrieve_context

results = retrieve_context(
    query="authentication",
    repo_id=22
)

print(results[0])