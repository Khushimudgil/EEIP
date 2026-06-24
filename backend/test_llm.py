from services.llm_service import generate_answer

response = generate_answer(
    "What is FastAPI?"
)

print(response)