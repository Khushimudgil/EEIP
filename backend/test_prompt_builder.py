from services.retrieval_service import retrieve_context
from services.context_builder import build_context
from services.prompt_builder import build_prompt


question = "How does authentication work?"


chunks = retrieve_context(
    query=question,
    repo_id=1,
    top_k=3
)

context = build_context(chunks)

prompt = build_prompt(
    context=context,
    question=question
)

print(prompt)